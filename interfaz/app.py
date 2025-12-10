import streamlit as st
import pandas as pd
import io
import sys
import os
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================
# 1. AÑADIR RUTA A SRC PARA IMPORTAR CLASES
# ============================================
# Ruta raíz del proyecto (importante para Streamlit)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Agregar raíz al sys.path (esto permite importar "src" correctamente)
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from src.visualizacion.VisualizadorMapas import VisualizadorMapas
from src.modelos.ModeloML import ModeloML

# ============================================
# 3. CARGAR DATASET
# ============================================
DATA_PATH = os.path.join(ROOT_DIR, "data/processed/conare_modelo.csv")
df = pd.read_csv(DATA_PATH)

# ============================================
# 4. CONFIG STREAMLIT
# ============================================
st.set_page_config(
    page_title="Proyecto de Deserción Estudiantil",
    page_icon="🏫",
    layout="wide"
)

if "pagina" not in st.session_state:
    st.session_state.pagina = "Inicio"

# Sidebar
st.sidebar.title("Menú principal")

if st.sidebar.button("🏠 Inicio"):
    st.session_state.pagina = "Inicio"

if st.sidebar.button("🔎 Información importante"):
    st.session_state.pagina = "Información importante"

if st.sidebar.button("📊 Gráficos"):
    st.session_state.pagina = "Graficos"

if st.sidebar.button("🤖 Modelos"):
    st.session_state.pagina = "Modelos"

if st.sidebar.button("🗺️ Mapas"):
    st.session_state.pagina = "Mapas"


# ============================================================
#                     PÁGINA DE INICIO
# ============================================================
if st.session_state.pagina == "Inicio":
    st.title("🎒 Proyecto Final Programación - Análisis Deserción Escolar")
    st.markdown("""
    ### **Curso:** Programación II – Big Data  
    ### **Estudiantes:** Evelyn Calderón Rojas, María Paubla Delgado Loaiza, Tiffany Méndez Quirós  
    ---
    """)

# ============================================================
#                INFORMACIÓN IMPORTANTE
# ============================================================
elif st.session_state.pagina == "Información importante":
    st.header("🔎 Información importante del proyecto")
    st.write("A continuación se muestra la estructura del dataset final:")
    st.dataframe(df.head())

# ============================================================
#                         GRÁFICOS
# ============================================================
elif st.session_state.pagina == "Graficos":

    st.title("📊 Visualizaciones del Análisis")

    sns.set(style="whitegrid")

    # 1. Estudiantes por universidad
    st.subheader("🏫 Estudiantes por Universidad")
    fig, ax = plt.subplots(figsize=(10, 5))
    df["UNIVERSIDAD"].value_counts().plot(kind="bar", ax=ax, color="skyblue")
    ax.set_title("Cantidad de Estudiantes por Universidad")
    st.pyplot(fig)

    # 2. Deserción por universidad
    st.subheader("⚠️ Porcentaje de Deserción por Universidad")
    fig, ax = plt.subplots(figsize=(10, 5))
    df.groupby("UNIVERSIDAD")["DESERTA"].mean().sort_values(ascending=False).plot(
        kind="bar", ax=ax, color="salmon"
    )
    ax.set_ylabel("Proporción")
    st.pyplot(fig)

    # 3. Deserción por año (CORREGIDO)
    st.subheader("📅 Deserción por Año")
    fig, ax = plt.subplots(figsize=(10, 5))
    df.groupby("AÑO")["DESERTA"].mean().plot(marker="o", ax=ax, color="purple")
    ax.set_title("Tasa de Deserción por Año")
    st.pyplot(fig)

    # 4. Distribución de edades
    st.subheader("👥 Matrícula por Edades")

    # Asegurar que EDAD sea numérica
    df["EDAD"] = pd.to_numeric(df["EDAD"], errors="coerce")

    # Filtrar edades razonables (17 a 80)
    df_edad = df[(df["EDAD"] >= 17) & (df["EDAD"] <= 80)]

    # Contar estudiantes por edad
    conteo_edad = df_edad["EDAD"].value_counts().sort_index()

    fig, ax = plt.subplots(figsize=(9, 6))
    ax.bar(conteo_edad.index, conteo_edad.values, color="lightblue", edgecolor="black")

    ax.set_title("Distribución de Estudiantes por Edad", fontsize=14)
    ax.set_xlabel("Edad", fontsize=12)
    ax.set_ylabel("Cantidad de Estudiantes", fontsize=12)

    st.pyplot(fig)


    # 5. Años matriculados
    st.subheader("🎓 Años Matriculados")
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(df["ANIOS_MATRICULADO"], bins=15, color="lightblue")
    st.pyplot(fig)

    # 6. Deserción por zona (CORREGIDO)
    st.subheader("🌎 Deserción por Zona")
    fig, ax = plt.subplots(figsize=(7, 5))
    df.groupby("ZONA_URBANO_RURAL_ESTUDIANTE")["DESERTA"].mean().plot(
        kind="bar", ax=ax, color="orange"
    )
    ax.set_title("Deserción por Zona")
    st.pyplot(fig)

    # 7. Heatmap
    st.subheader("📈 Mapa de Correlaciones")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.heatmap(df.select_dtypes(include=["int64", "float64"]).corr(), cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    # -------------------------------------------
    # 8. Tasa de deserción por rangos de edad
    # -------------------------------------------
    st.subheader("📉 Deserción por Rangos de Edad")

    # Crear rangos de edad
    bins = [15, 20, 25, 30, 35, 40, 50, 60, 80]
    labels = ["15-19", "20-24", "25-29", "30-34", "35-39", "40-49", "50-59", "60-80"]

    df["rango_edad"] = pd.cut(df["EDAD"], bins=bins, labels=labels, right=False)

    # Calcular tasa de deserción por rango
    desercion_rangos = df.groupby("rango_edad")["DESERTA"].mean()

    fig, ax = plt.subplots(figsize=(9, 5))
    desercion_rangos.plot(kind="bar", color="coral", ax=ax)

    ax.set_title("Tasa de Deserción por Rangos de Edad")
    ax.set_ylabel("Proporción que Deserta")
    ax.set_xlabel("Rango de Edad")

    st.pyplot(fig)


# ============================================================
#                       MODELADO ML
# ============================================================
elif st.session_state.pagina == "Modelos":

    st.title("🤖 Modelos Predictivos")

    # 1. Cargar modelo
    st.write("Cargando modelos...")

    modelo = ModeloML("data/processed/conare_modelo.csv")
    modelo.cargar_datos()
    modelo.preparar_clasificacion()
    modelo.entrenar_clasificacion()
    modelo.preparar_regresion()
    modelo.entrenar_regresion()

    st.success("Modelos entrenados correctamente ✔")

    # 2. Formulario de predicción
    st.subheader("📥 Ingresá los datos del estudiante")

    edad = st.number_input("Edad", 15, 80, 20)
    sexo = st.selectbox("Sexo", modelo.df["SEXO"].unique())
    universidad = st.selectbox("Universidad", modelo.df["UNIVERSIDAD"].unique())
    area = st.selectbox("Área de Conocimiento", modelo.df["AREA_CONOCIMIENTO"].unique())
    tipo = st.selectbox("Tipo de Matrícula", modelo.df["TIPO_MATRICULA"].unique())
    anio = st.selectbox("Año", sorted(modelo.df["AÑO"].unique()))

    entrada = pd.DataFrame([{
        "EDAD": edad,
        "SEXO": sexo,
        "UNIVERSIDAD": universidad,
        "AREA_CONOCIMIENTO": area,
        "TIPO_MATRICULA": tipo,
        "AÑO": anio
    }])

    entrada_clas = pd.get_dummies(entrada).reindex(columns=modelo.Xc.columns, fill_value=0)
    entrada_reg = pd.get_dummies(entrada).reindex(columns=modelo.Xr.columns, fill_value=0)

    if st.button("🔮 Predecir"):

        # Clasificación
        pred_c = modelo.modelo_clasificacion.predict(entrada_clas)[0]

        st.markdown("### 📘 Predicción de deserción:")
        if pred_c == 1:
            st.error("⚠️ El estudiante podría DESERTAR.")
        else:
            st.success("✅ El estudiante probablemente CONTINUARÁ.")

        # Regresión
        pred_r = modelo.modelo_regresion.predict(entrada_reg)[0]

        st.markdown("### 🎓 Predicción de permanencia:")
        st.info(f"El modelo estima que permanecerá **{pred_r:.2f} años** matriculado.")


elif st.session_state.pagina == "Mapas":
    st.header("📍🗺️ Visualización por zonas")

    mapas = VisualizadorMapas(df)
    st.subheader("🗺 Mapa de deserción por provincia")
    mapas.mapa_desercion_provincia()
