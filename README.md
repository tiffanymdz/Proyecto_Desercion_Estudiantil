# Proyecto_Desercion_Estudiantil
Proyecto final de Programación II

🎓 Análisis de Deserción Estudiantil Universitaria en Costa Rica

Proyecto universitario de ciencia de datos que analiza la deserción estudiantil universitaria en Costa Rica mediante el uso de APIs, conexiones a bases de datos y modelos de Machine Learning para predicción.

📋 Tabla de Contenidos

🔍 Descripción

📊 Fuentes de Datos

🎯 Objetivos del Proyecto

🏗️ Arquitectura del Proyecto

🛠️ Tecnologías Utilizadas

📒 Uso

👥 Autores

🔍 Descripción

Este proyecto implementa un análisis exhaustivo de la deserción estudiantil universitaria en Costa Rica, integrando múltiples fuentes de datos para identificar patrones y factores que influyen en el abandono de los estudios superiores. El análisis combina datos de matrícula universitaria, índices de pobreza y variables socioeconómicas mediante técnicas de ciencia de datos y aprendizaje automático.

📊 Fuentes de Datos

Datasets Utilizados

Matrícula Sector Estatal (CONARE)


📁 Dataset de estudiantes universitarios 2021-2024

🔗 https://www.conare.ac.cr/sdm_downloads/datos-abiertos-matricula-sector-estatal-2021-2024/


Pobreza en Hogares Costarricenses (INEC)


📁 ENAHO - Encuesta Nacional de Hogares

🔗 https://sistemas.inec.cr/nada5.4/index.php/catalog/373/get-microdata


API Externa

World Bank API

🌐 Índices de pobreza en Costa Rica

🔗 https://publicapis.io/world-bank-api


🎯 Objetivos del Proyecto

El proyecto busca diseñar y desarrollar un sistema completo de ciencia de datos que integre:

✅ Diversas fuentes de datos: bases de datos relacionales (SQLite, SQL Server, PostgreSQL, MySQL), APIs públicas nacionales e internacionales, y archivos CSV reales

✅ Análisis Exploratorio de Datos (EDA): exploración profunda de patrones y tendencias en la deserción estudiantil

✅ Visualización de datos: representaciones gráficas claras y significativas

✅ Machine Learning supervisado: aplicación de algoritmos de clasificación y regresión para predicción

✅ Programación Orientada a Objetos: estructura modular que fomenta buenas prácticas de desarrollo

🏗️ Arquitectura del Proyecto

📂 Data

Almacena todos los conjuntos de datos del proyecto:

Raw: datos originales sin modificar

Processed: datos limpios y preparados para análisis

📂 SRC

Contiene todo el código fuente del proyecto:

datos: procesamiento y limpieza de datasets

basedatos: gestión de conexiones a bases de datos relacionales

eda: herramientas para análisis exploratorio

modelos: implementaciones de algoritmos de ML (clasificación y regresión)

visualizador: módulos para generación de gráficos estadísticos

📂 Interfaz

Aplicación web interactiva desarrollada con Streamlit para visualización y uso de los modelos.

📂 Notebooks

Cuadernos Jupyter con análisis detallados y experimentación.

🛠️ Tecnologías Utilizadas

- Lenguaje Principal

Python 3.8+

Librerías de Ciencia de Datos

Librería: pandas

Propósito: Manipulación y análisis de datos

Librería: numpy

Propósito: Computación numérica

Librería: pyreadstat

Propósito: Lectura de archivos estadísticos (SPSS, SAS, Stata)

- Visualización

Librería: matplotlib

Propósito: Gráficos estáticos y visualizaciones

Librería: seaborn

Propósito: Visualizaciones estadísticas avanzadas

- Bases de Datos

Librería: sqlalchemy

Propósito: ORM y gestión de bases de datos

Librería: pyodbc

Propósito: Conexión a bases de datos SQL Server

- Machine Learning

Librería: scikit-learn

Propósito: Modelos de clasificación y regresión

- Utilidades

Librería: openpyxl

Propósito: Manejo de archivos Excel

Librería: io

Propósito: Operaciones de entrada y salida

Librería: sys

Propósito: Funciones del sistema

Librería: os

Propósito: Interacción del sistema operativa

- Interfaz de Usuario 

Librería: streamlit

Propósito: Aplicación web interactiva

📒 Estructura de Uso Típica

1. Cargar y procesar datos: utiliza los módulos en SRC/datos/

2. Realizar EDA: ejecuta Procesador_EDA.py para análisis exploratorio

3. Entrenar modelos: usa los scripts en SRC/modelos/

4. Visualizar resultados: genera gráficos con los módulos en SRC/visualizador/

5. Interactuar con la aplicación: lanza la interfaz Streamlit para exploración interactiva

👥 Autores

Equipo de Desarrollo

👩‍💻 María Paubla Delgado Loaiza

👩‍💻 Evelin Calderón Rojas

👩‍💻 Tiffany Méndez Quirós

Información Académica

📚 Colegio Universitario de Cartago

📘 Curso: BD-143 Programación II

📅 Período: III Cuatrimestre 2025

👨‍🏫 Profesor: Osvaldo González Chaves

📝 Licencia

Este proyecto fue desarrollado con fines académicos para el curso de Programación II.
