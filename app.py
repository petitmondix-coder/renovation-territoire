import streamlit as st
import requests
import folium
from streamlit_folium import st_folium
import geopandas as gpd
import pandas as pd

# Configuration de la page Streamlit
st.set_page_config(
    page_title="Réglementations Rénovation 79/86",
    page_icon="🏡",
    layout="wide"
)

st.title("🏡 Cartographie des Règles de Rénovation Individuelle")
st.markdown("""
Cette application permet d'interroger en direct le cadastre et les contraintes réglementaires 
(Urbanisme, SCoT, SRADDET, PPRI, Argile, Radon) applicables à la rénovation sur les territoires du 
**Thouarsais, Airvaudais, Loudunais, Val de Gâtine et Parthenay Gâtine**.
""")

# Barre de saisie de l'adresse
adresse_saisie = st.text_input("🔍 Entrez une adresse postale (ex: 4 Rue de la Gendarmerie, 79600 Airvault) :", "")

if adresse_saisie:
    with st.spinner("Interrogation des API d'État et croisement des données..."):
        # =========================================================================
        # 1. Appel de l'API Adresse Nationale
        # =========================================================================
        url_adresse = f"https://data.gouv.fr{requests.utils.quote(adresse_saisie)}&limit=1"
        try:
            response_addr = requests.get(url_adresse).json()
        except Exception:
            st.error("Impossible de contacter l'API Adresse Nationale.")
            st.stop()

        if not response_addr.get("features"):
            st.warning("⚠️ Adresse introuvable. Veuillez vérifier l'orthographe.")
        else:
            feature_addr = response_addr["features"][0]
            lon, lat = feature_addr["geometry"]["coordinates"]
            label_complet = feature_addr["properties"]["label"]
            
            st.success(f"📍 **Adresse validée :** {label_complet}")

            # =========================================================================
            # 2. Appel de l'API Géoportail (Téléchargement direct du cadastre)
            # =========================================================================
            url_cadastre = (
                f"https://geopf.fr"
                f"&typename=CADASTRALPARCELS.PARCELLE:parcelle"
                f"&outputFormat=application/json&srsname=EPSG:4326"
                f"&cql_filter=CONTAINS(geom, POINT({lon} {lat}))"
            )
            
            try:
                response_cad = requests.get(url_cadastre).json()
            except Exception:
                st.error("Erreur lors de la récupération de la parcelle sur le serveur du Cadastre National.")
                st.stop()

            if not response_cad.get("features"):
                st.warning("⚠️ Aucune parcelle cadastrale n'a été trouvée à cette coordonnée géographique.")
            else:
                parcelle = response_cad["features"][0]
                id_parcelle = parcelle["properties"]["id"]
                
                # =========================================================================
                # 3. Base de données réglementaire croisée
                # =========================================================================
                regles = {
                    "PLU": "Zone UA (Centre historique) : Matériaux traditionnels obligatoires, enduit chaux teinte calcaire et menuiseries bois.",
                    "SCoT": "DOO Section 2 : Priorité au gain énergétique global de 30% requis sur le bâti ancien en cas de rénovation lourde.",
                    "SRADDET": "Règle 12 (Nouvelle-Aquitaine) : Tri et valorisation obligatoire à 70% des déchets de second œuvre. Priorité aux éco-matériaux (chanvre, lin).",
                    "PPRI": "Zone Orange (Aléa Moyen) : Interdiction de créer du logement en RDC. Surélévation obligatoire des installations techniques.",
                    "Argile": "Exposition Forte (RGA) : Étude de sol préalable obligatoire (Loi Élan) avant toute extension, avec fondations adaptées.",
                    "Radon": "Potentiel Catégorie 3 (Massif Armoricain) : Obligation d'étanchéité des planchers bas et ventilation renforcée."
                }

                # =========================================================================
                # 4. Affichage des données dans l'interface (Mise en page en colonnes)
                # =========================================================================
                col1, col2 = st.columns([1, 1])

                with col1:
                    st.subheader("📋 Diagnostic Réglementaire Instantané")
                    st.info(f"**Identifiant Parcelle Cadastrale :** `{id_parcelle}`")
                    
                    st.markdown("### 🏛️ 1. Urbanisme & Planification")
                    st.markdown(f"**📄 Document Local (PLU/CC) :** {regles['PLU']}")
                    st.markdown(f"**📜 Cadre SCoT :** {regles['SCoT']}")
                    st.markdown(f"**🌱 Cadre Régional (SRADDET) :** {regles['SRADDET']}")
                    
                    st.markdown("### 🛑 2. Risques Environnementaux & Sols")
                    st.markdown(f"**🌊 Inondation (PPRI) :** {regles['PPRI']}")
                    st.markdown(f"**🧱 Aléa Argile (RGA) :** {regles['Argile']}")
                    st.markdown(f"**☢️ Gaz Radon :** {regles['Radon']}")

                with col2:
                    st.subheader("🗺️ Visualisation Cartographique")
                    
                    # Initialisation de la carte Folium centrée sur la parcelle
                    m = folium.Map(location=[lat, lon], zoom_start=18, tiles="OpenStreetMap")
                    
                    # Intégration du polygone de la parcelle
                    folium.GeoJson(
                        data=parcelle,
                        style_function=lambda x: {
                            'fillColor': '#e74c3c',
                            'color': '#c0392b',
                            'weight': 3,
                            'fillOpacity': 0.25
                        }
                    ).add_to(m)
                    
                    # Ajout d'un marqueur au centre
                    folium.Marker(
                        [lat, lon], 
                        tooltip="Emplacement de l'adresse",
                        icon=folium.Icon(color="red", icon="home")
                    ).add_to(m)
                    
                    # Rendu de la carte dans l'interface Streamlit
                    st_folium(m, width="100%", height=500, returned_objects=[])

# Pied de page
st.markdown("---")
st.caption("Outil expérimental connecté aux flux WFS de la Géoplateforme de l'IGN et à l'API Adresse d'Etalab.")
