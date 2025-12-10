import streamlit as st
import pandas as pd
<<<<<<< Updated upstream
import io
import sys
import os
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sns
=======
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ruta correcta del dataset
DATA_PATH = os.path.join(os.path.dirname(__file__), "../data/processed/conare_modelo.csv")

# Cargar DataFrame
df = pd.read_csv(DATA_PATH)

from src.modelos.ModeloML import ModeloML
modelo = ModeloML("data/processed/conare_modelo.csv")
modelo.cargar_datos()
modelo.preparar_clasificacion()
modelo.entrenar_clasificacion()
modelo.preparar_regresion()
modelo.entrenar_regresion()

>>>>>>> Stashed changes


st.set_page_config(
    page_title="Proyecto de Deserción Estudiantil",
    page_icon="",
    layout="wide"
)

# Establece la 'página' de inicio como predeterminada

if "pagina" not in st.session_state:
    st.session_state.pagina = "Inicio"


# Menú con las opciones tipo botones

st.sidebar.title("Menú principal")

if st.sidebar.button(" Inicio"):
    st.session_state.pagina = "Inicio"

if st.sidebar.button(" Información importante"):
    st.session_state.pagina = "Información importante"

if st.sidebar.button(" Gráficos"):
    st.session_state.pagina = "Graficos"

<<<<<<< Updated upstream
=======
if st.sidebar.button("Modelos"):
    st.session_state.pagina = "Modelos"

>>>>>>> Stashed changes
# Contenidos
# Página de inicio

if st.session_state.pagina == "Inicio":
    st.title(" Proyecto Final Programación - Análisis Deserción Escolar")
    st.markdown("""
    ### **Curso:** Programación II – Big Data  
    ### **Estudiantes:** Evelyn Calderón Rojas/ María Paubla Delgado Loaiza/ Tiffany Méndez Quirós
    ---
    """)


# Ver el dataset

elif st.session_state.pagina == "Información importante":
    st.header(" Información importante")


# Gráficos

elif st.session_state.pagina == "Graficos":
<<<<<<< Updated upstream
    st.header("Resultados del Análisis")
=======
    st.title("Visualizaciones de resultados")

    st.markdown("### Estas gráficas permiten analizar tendencias importantes relacionadas con la deserción estudiantil.")

    # Ajustes globales
    sns.set(style="whitegrid")

    # -------------------------------
    # 1. Estudiantes por universidad
    # -------------------------------
    st.subheader("Estudiantes por Universidad")

    fig, ax = plt.subplots(figsize=(10, 5))
    df["UNIVERSIDAD"].value_counts().plot(kind="bar", ax=ax, color="skyblue")
    ax.set_title("Cantidad de Estudiantes por Universidad")
    st.pyplot(fig)

    # ------------------------------------------------------
    # 2. Porcentaje de deserción por universidad
    # ------------------------------------------------------
    st.subheader("Porcentaje de Deserción por Universidad")

    fig, ax = plt.subplots(figsize=(10, 5))
    (df.groupby("UNIVERSIDAD")["DESERTA"]
       .mean()
       .sort_values(ascending=False)
       .plot(kind="bar", ax=ax, color="salmon"))

    ax.set_title("Tasa de Deserción por Universidad")
    ax.set_ylabel("Proporción que Deserta")
    st.pyplot(fig)

    # -------------------------------
    # 3. Deserción por año
    # -------------------------------
    st.subheader("Deserción por Año")

    fig, ax = plt.subplots(figsize=(10, 5))
    df.groupby("ANO")["DESERTA"].mean().plot(marker="o", ax=ax, color="purple")
    ax.set_title("Tasa de Deserción por Año")
    st.pyplot(fig)

    # -------------------------------
    # 4. Distribución de edades
    # -------------------------------
    st.subheader("Distribución de Edades")

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(df["EDAD"], bins=20, color="lightgreen")
    ax.set_title("Distribución de Edades")
    st.pyplot(fig)

    # -------------------------------------------
    # 5. Distribución de Años Matriculados
    # -------------------------------------------
    st.subheader("Años Matriculados (Distribución)")

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(df["ANIOS_MATRICULADO"], bins=15, color="lightblue")
    ax.set_title("Distribución de Años Matriculados")
    st.pyplot(fig)

    # -------------------------------------------
    # 6. Deserción por zona urbana/rural
    # -------------------------------------------
    st.subheader("Deserción según Zona")

    fig, ax = plt.subplots(figsize=(7, 5))
    df.groupby("ZONA")["DESERTA"].mean().plot(kind="bar", ax=ax, color="orange")
    ax.set_title("Deserción por Zona (Urbana / Rural)")
    ax.set_ylabel("Proporción que Deserta")
    st.pyplot(fig)

    # -------------------------------------------
    # 7. Correlación entre variables numéricas
    # -------------------------------------------
    st.subheader("Mapa de Correlación (Variables Numéricas)")

    num_df = df.select_dtypes(include=["int64", "float64"])
    corr = num_df.corr()

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.heatmap(corr, annot=False, cmap="coolwarm", ax=ax)
    ax.set_title("Mapa de Calor de Correlaciones")
    st.pyplot(fig)


elif st.session_state.pagina == "Modelos":

    st.title("Modelos Predictivos")
    st.markdown("### Probá los modelos con datos personalizados")

    # ============================================
    # Cargar y entrenar los modelos
    # ============================================
    st.write("Cargando modelos...")

    modelo = ModeloML("data/processed/conare_modelo.csv")
    modelo.cargar_datos()

    modelo.preparar_clasificacion()
    modelo.entrenar_clasificacion()

    modelo.preparar_regresion()
    modelo.entrenar_regresion()

    st.success("Modelos cargados y entrenados correctamente ✔")


    # ============================================
    # FORMULARIO DE PREDICCIÓN
    # ============================================

    st.subheader("Ingresá los datos del estudiante")

    # -------- Inputs --------
    edad = st.number_input("Edad", 15, 80, 20)
    sexo = st.selectbox("Sexo", modelo.df["SEXO"].unique())
    zona = st.selectbox("Zona", modelo.df["ZONA"].unique())
    universidad = st.selectbox("Universidad", modelo.df["UNIVERSIDAD"].unique())
    area = st.selectbox("Área de Conocimiento", modelo.df["AREA_CONOCIMIENTO"].unique())
    tipo = st.selectbox("Tipo de Matrícula", modelo.df["TIPO_MATRICULA"].unique())
    anio = st.selectbox("Año", sorted(modelo.df["ANO"].unique()))

    # ============================================
    # Crear DataFrame con los datos ingresados
    # ============================================
    entrada = pd.DataFrame([{
        "EDAD": edad,
        "SEXO": sexo,
        "ZONA": zona,
        "UNIVERSIDAD": universidad,
        "AREA_CONOCIMIENTO": area,
        "TIPO_MATRICULA": tipo,
        "ANO": anio
    }])

    # Dummificación consistente
    entrada_clas = pd.get_dummies(entrada)
    entrada_clas = entrada_clas.reindex(columns=modelo.Xc.columns, fill_value=0)

    entrada_reg = pd.get_dummies(entrada)
    entrada_reg = entrada_reg.reindex(columns=modelo.Xr.columns, fill_value=0)


    # ============================================
    # BOTÓN DE PREDICCIÓN
    # ============================================
    if st.button("Predecir"):

        # -------- CLASIFICACIÓN --------
        pred_c = modelo.modelo_clasificacion.predict(entrada_clas)[0]

        st.markdown("### Resultado de clasificación (Deserción):")
        if pred_c == 1:
            st.error("El modelo predice que el estudiante podría DESERTAR.")
        else:
            st.success("El modelo predice que el estudiante CONTINUARÁ.")

        # -------- REGRESIÓN --------
        pred_r = modelo.modelo_regresion.predict(entrada_reg)[0]

        st.markdown("###Predicción de años matriculados:")
        st.info(f"El modelo estima que el estudiante permanecerá **{pred_r:.2f} años** matriculado.")






>>>>>>> Stashed changes



