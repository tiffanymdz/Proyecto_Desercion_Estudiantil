import folium
import pandas as pd
import json
from streamlit_folium import st_folium
import os

class VisualizadorMapas:

    def __init__(self, df):
        self.df = df

        # Ruta local del geojson en tu proyecto
        self.geojson_path = os.path.join("data", "geo", "provincias.geojson")

        # Normalizar nombres de provincia para asegurar coincidencias con el GeoJSON
        if "PROVINCIA_ESTUDIANTE" in self.df.columns:
            self.df["PROVINCIA_ESTUDIANTE"] = (
                self.df["PROVINCIA_ESTUDIANTE"]
                .str.upper()
                .replace({
                    "SAN JOSE": "San José",
                    "LIMON": "Limón",
                    "HEREDIA": "Heredia",
                    "CARTAGO": "Cartago",
                    "GUANACASTE": "Guanacaste",
                    "PUNTARENAS": "Puntarenas",
                    "ALAJUELA": "Alajuela",
                })
            )

    # ----------------------------------------------------------------------
    # 📍 MAPA DE DESECION POR PROVINCIA
    # ----------------------------------------------------------------------
    def mapa_desercion_provincia(self, ancho=700, alto=500):

        if not os.path.exists(self.geojson_path):
            return "❌ No se encontró el archivo provincias.geojson en data/geo/"

        # Calcular la tasa de deserción por provincia
        mapa_df = (
            self.df.groupby("PROVINCIA_ESTUDIANTE")["DESERTA"]
            .mean()
            .reset_index()
        )
        mapa_df.columns = ["provincia", "tasa_desercion"]

        # Cargar GeoJSON
        with open(self.geojson_path, "r", encoding="utf-8") as f:
            geojson_data = json.load(f)

        # Crear mapa centrado en Costa Rica
        m = folium.Map(location=[9.63, -84.25], zoom_start=7)

        # ----------------------------
        # Choropleth (colormap)
        # ----------------------------
        folium.Choropleth(
            geo_data=geojson_data,
            name="choropleth",
            data=mapa_df,
            columns=["provincia", "tasa_desercion"],
            key_on="feature.properties.name",
            fill_color="YlOrRd",
            fill_opacity=0.85,
            line_opacity=0.5,
            highlight=True,
            legend_name="Tasa de Deserción por Provincia",
        ).add_to(m)

        # ----------------------------
        # Tooltips (cuando pasás el mouse)
        # ----------------------------
        for _, row in mapa_df.iterrows():
            folium.Tooltip(
                f"<b>Provincia:</b> {row['provincia']}<br>"
                f"<b>Tasa deserción:</b> {row['tasa_desercion']:.2f}"
            )

        return st_folium(m, width=ancho, height=alto)
