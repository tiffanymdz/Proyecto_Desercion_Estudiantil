import folium
import pandas as pd
import json
from streamlit_folium import st_folium
import os


class VisualizadorMapas:

    def __init__(self, df):
        self.df = df

        # Ruta local del geojson
        self.geojson_path = os.path.join("data", "geo", "provincias.geojson")

        # Normalizar nombres de provincia para que coincidan con el GeoJSON
        if "PROVINCIA_ESTUDIANTE" in self.df.columns:
            self.df["PROVINCIA_ESTUDIANTE"] = (
                self.df["PROVINCIA_ESTUDIANTE"]
                .str.title()
                .replace({
                    "Limon": "Limón",
                    "San jose": "San José",
                    "Heredia": "Heredia",
                    "Alajuela": "Alajuela",
                    "Cartago": "Cartago",
                    "Puntarenas": "Puntarenas",
                    "Guanacaste": "Guanacaste",
                })
            )

    def mapa_desercion_provincia(self, ancho=700, alto=500):

        # Verificar existencia del archivo
        if not os.path.exists(self.geojson_path):
            return "❌ No se encontró el archivo provincias.geojson en data/geo/"

        # ===========================
        #  Cálculo de deserción
        # ===========================
        mapa_df = (
            self.df.groupby("PROVINCIA_ESTUDIANTE")["DESERTA"]
            .mean()
            .reset_index()
        )
        mapa_df.columns = ["provincia", "tasa_desercion"]

        # ===========================
        #  Cargar GeoJSON
        # ===========================
        with open(self.geojson_path, "r", encoding="utf-8") as f:
            geojson_data = json.load(f)

        # ===========================
        # Crear mapa centrado en CR
        # ===========================
        m = folium.Map(location=[9.63, -84.25], zoom_start=8)

        # ===========================
        # Mapa coroplético
        # ===========================
        folium.Choropleth(
            geo_data=geojson_data,
            name="choropleth",
            data=mapa_df,
            columns=["provincia", "tasa_desercion"],
            key_on="feature.properties.name",
            fill_color="YlOrRd",
            fill_opacity=0.8,
            line_opacity=0.4,
            nan_fill_color="white",
            legend_name="Tasa de Deserción por Provincia",
        ).add_to(m)

        # ===========================
        # Mostrar en Streamlit
        # ===========================
        return st_folium(m, width=ancho, height=alto)
