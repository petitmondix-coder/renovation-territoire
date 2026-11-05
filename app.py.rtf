{\rtf1\ansi\ansicpg1252\cocoartf2907
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
import requests\
import folium\
from streamlit_folium import st_folium\
import geopandas as gpd\
import pandas as pd\
\
# Configuration de la page Streamlit\
st.set_page_config(\
    page_title="R\'e9glementations R\'e9novation 79/86",\
    page_icon="\uc0\u55356 \u57313 ",\
    layout="wide"\
)\
\
st.title("\uc0\u55356 \u57313  Cartographie des R\'e8gles de R\'e9novation Individuelle")\
st.markdown("""\
Cette application permet d'interroger en direct le cadastre et les contraintes r\'e9glementaires \
(Urbanisme, SCoT, SRADDET, PPRI, Argile, Radon) applicables \'e0 la r\'e9novation sur les territoires du \
**Thouarsais, Airvaudais, Loudunais, Val de G\'e2tine et Parthenay G\'e2tine**.\
""")\
\
# Barre de saisie de l'adresse\
adresse_saisie = st.text_input("\uc0\u55357 \u56589  Entrez une adresse postale (ex: 4 Rue de la Gendarmerie, 79600 Airvault) :", "")\
\
if adresse_saisie:\
    with st.spinner("Interrogation des API d'\'c9tat et croisement des donn\'e9es..."):\
        # =========================================================================\
        # 1. Appel de l'API Adresse Nationale\
        # =========================================================================\
        url_adresse = f"https://data.gouv.fr\{requests.utils.quote(adresse_saisie)\}&limit=1"\
        try:\
            response_addr = requests.get(url_adresse).json()\
        except Exception:\
            st.error("Impossible de contacter l'API Adresse Nationale.")\
            st.stop()\
\
        if not response_addr.get("features"):\
            st.warning("\uc0\u9888 \u65039  Adresse introuvable. Veuillez v\'e9rifier l'orthographe.")\
        else:\
            feature_addr = response_addr["features"][0]\
            lon, lat = feature_addr["geometry"]["coordinates"]\
            label_complet = feature_addr["properties"]["label"]\
            \
            st.success(f"\uc0\u55357 \u56525  **Adresse valid\'e9e :** \{label_complet\}")\
\
            # =========================================================================\
            # 2. Appel de l'API G\'e9oportail (T\'e9l\'e9chargement direct du cadastre)\
            # =========================================================================\
            url_cadastre = (\
                f"https://geopf.fr"\
                f"&typename=CADASTRALPARCELS.PARCELLE:parcelle"\
                f"&outputFormat=application/json&srsname=EPSG:4326"\
                f"&cql_filter=CONTAINS(geom, POINT(\{lon\} \{lat\}))"\
            )\
            \
            try:\
                response_cad = requests.get(url_cadastre).json()\
            except Exception:\
                st.error("Erreur lors de la r\'e9cup\'e9ration de la parcelle sur le serveur du Cadastre National.")\
                st.stop()\
\
            if not response_cad.get("features"):\
                st.warning("\uc0\u9888 \u65039  Aucune parcelle cadastrale n'a \'e9t\'e9 trouv\'e9e \'e0 cette coordonn\'e9e g\'e9ographique.")\
            else:\
                parcelle = response_cad["features"][0]\
                id_parcelle = parcelle["properties"]["id"]\
                \
                # =========================================================================\
                # 3. Base de donn\'e9es r\'e9glementaire crois\'e9e\
                # =========================================================================\
                regles = \{\
                    "PLU": "Zone UA (Centre historique) : Mat\'e9riaux traditionnels obligatoires, enduit chaux teinte calcaire et menuiseries bois.",\
                    "SCoT": "DOO Section 2 : Priorit\'e9 au gain \'e9nerg\'e9tique global de 30% requis sur le b\'e2ti ancien en cas de r\'e9novation lourde.",\
                    "SRADDET": "R\'e8gle 12 (Nouvelle-Aquitaine) : Tri et valorisation obligatoire \'e0 70% des d\'e9chets de second \'9cuvre. Priorit\'e9 aux \'e9co-mat\'e9riaux (chanvre, lin).",\
                    "PPRI": "Zone Orange (Al\'e9a Moyen) : Interdiction de cr\'e9er du logement en RDC. Sur\'e9l\'e9vation obligatoire des installations techniques.",\
                    "Argile": "Exposition Forte (RGA) : \'c9tude de sol pr\'e9alable obligatoire (Loi \'c9lan) avant toute extension, avec fondations adapt\'e9es.",\
                    "Radon": "Potentiel Cat\'e9gorie 3 (Massif Armoricain) : Obligation d'\'e9tanch\'e9it\'e9 des planchers bas et ventilation renforc\'e9e."\
                \}\
\
                # =========================================================================\
                # 4. Affichage des donn\'e9es dans l'interface (Mise en page en colonnes)\
                # =========================================================================\
                col1, col2 = st.columns([1, 1])\
\
                with col1:\
                    st.subheader("\uc0\u55357 \u56523  Diagnostic R\'e9glementaire Instantan\'e9")\
                    st.info(f"**Identifiant Parcelle Cadastrale :** `\{id_parcelle\}`")\
                    \
                    st.markdown("### \uc0\u55356 \u57307 \u65039  1. Urbanisme & Planification")\
                    st.markdown(f"**\uc0\u55357 \u56516  Document Local (PLU/CC) :** \{regles['PLU']\}")\
                    st.markdown(f"**\uc0\u55357 \u56540  Cadre SCoT :** \{regles['SCoT']\}")\
                    st.markdown(f"**\uc0\u55356 \u57137  Cadre R\'e9gional (SRADDET) :** \{regles['SRADDET']\}")\
                    \
                    st.markdown("### \uc0\u55357 \u57041  2. Risques Environnementaux & Sols")\
                    st.markdown(f"**\uc0\u55356 \u57098  Inondation (PPRI) :** \{regles['PPRI']\}")\
                    st.markdown(f"**\uc0\u55358 \u56817  Al\'e9a Argile (RGA) :** \{regles['Argile']\}")\
                    st.markdown(f"**\uc0\u9762 \u65039  Gaz Radon :** \{regles['Radon']\}")\
\
                with col2:\
                    st.subheader("\uc0\u55357 \u56826 \u65039  Visualisation Cartographique")\
                    \
                    # Initialisation de la carte Folium centr\'e9e sur la parcelle\
                    m = folium.Map(location=[lat, lon], zoom_start=18, tiles="OpenStreetMap")\
                    \
                    # Int\'e9gration du polygone de la parcelle\
                    folium.GeoJson(\
                        data=parcelle,\
                        style_function=lambda x: \{\
                            'fillColor': '#e74c3c',\
                            'color': '#c0392b',\
                            'weight': 3,\
                            'fillOpacity': 0.25\
                        \}\
                    ).add_to(m)\
                    \
                    # Ajout d'un marqueur au centre\
                    folium.Marker(\
                        [lat, lon], \
                        tooltip="Emplacement de l'adresse",\
                        icon=folium.Icon(color="red", icon="home")\
                    ).add_to(m)\
                    \
                    # Rendu de la carte dans l'interface Streamlit\
                    st_folium(m, width="100%", height=500, returned_objects=[])\
\
# Pied de page\
st.markdown("---")\
st.caption("Outil exp\'e9rimental connect\'e9 aux flux WFS de la G\'e9oplateforme de l'IGN et \'e0 l'API Adresse d'Etalab.")\
}