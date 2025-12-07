import streamlit as st
import pandas as pd
import io
import sys
import os
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(
    page_title="Proyecto de Deserción Estudiantil",
    page_icon="🏫",
    layout="wide"
)

# Establece la 'página' de inicio como predeterminada

if "pagina" not in st.session_state:
    st.session_state.pagina = "Inicio"


# Menú con las opciones tipo botones

st.sidebar.title("Menú principal")

if st.sidebar.button("🏠 Inicio"):
    st.session_state.pagina = "Inicio"

if st.sidebar.button("🔎 Información importante"):
    st.session_state.pagina = "Información importante"

if st.sidebar.button("📊 Gráficos"):
    st.session_state.pagina = "Graficos"

# Contenidos
# Página de inicio

if st.session_state.pagina == "Inicio":
    st.title("🎒 Proyecto Final Programación - Análisis Deserción Escolar")
    st.markdown("""
    ### **Curso:** Programación II – Big Data  
    ### **Estudiantes:** Evelyn Calderón Rojas/ María Paubla Delgado Loaiza/ Tiffany Méndez Quirós
    ---
    """)


# Ver el dataset

elif st.session_state.pagina == "Información importante":
    st.header("🔎 Información importante")


# Gráficos

elif st.session_state.pagina == "Graficos":
    st.header("📊 Resultados del Análisis")



