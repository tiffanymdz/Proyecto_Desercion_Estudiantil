# transformar archivo .SAV a .csv

import pyreadstat
import pandas as pd

df, meta = pyreadstat.read_sav(r"C:\Users\tiffa\OneDrive\Desktop\Big Data\Programación II\Desercion_Estudiantil\data\raw\GPES-ELAB-GEBD-ENAHO-2025_BdPublica.sav")
print(df.head())
print(df.columns)

df.to_csv(r"C:\Users\tiffa\OneDrive\Desktop\Big Data\Programación II\Desercion_Estudiantil\data\processed\datos_inec_convertidos.csv", index=False)


# limpiar dataset del INEC

import csv
print("Usando módulo csv desde:", csv.__file__)

import pandas as pd

ruta = r"C:\Users\tiffa\OneDrive\Desktop\Big Data\Programación II\Desercion_Estudiantil\data\processed\datos_inec_convertidos.csv"

df = pd.read_csv(ruta)

print(df.head())
print("Datos cargados correctamente ")


print(df.isnull().sum())

import pandas as pd

ruta = r"C:\Users\tiffa\OneDrive\Desktop\Big Data\Programación II\Desercion_Estudiantil\data\processed\datos_inec_convertidos.csv"
df = pd.read_csv(ruta)

print("\nDatos cargados correctamente ✓")


# 1. Identificar ID

id_cols = ['ID_HOGAR', 'ID_VIVIENDA', 'id']
print("\nColumnas ID detectadas:", id_cols)


# 2. ID rellenar con 0

df[id_cols] = df[id_cols].fillna(0)


# 3. NUMÉRICAS

cols_numericas = df.select_dtypes(include=['int64','float64']).columns.difference(id_cols)

df[cols_numericas] = df[cols_numericas].fillna(df[cols_numericas].mean())


# 4. CATEGÓRICAS

cols_categoricas = df.select_dtypes(include=['object']).columns
for col in cols_categoricas:
    if df[col].isnull().any():
        df[col] = df[col].fillna(df[col].mode()[0])


# 5. Verificar

print("\nNulos después de la limpieza:")
print(df.isnull().sum())


# 6. Guardar

ruta_salida = r"C:\Users\tiffa\OneDrive\Desktop\Big Data\Programación II\Desercion_Estudiantil\data\processed\datos_inec_convertidos1.csv"
df.to_csv(ruta_salida, index=False)

print("\nArchivo limpio guardado en:")
print(ruta_salida)


print(df.isnull().sum().sum())

# uso de API

import requests

BASE_URL = "https://api.worldbank.org/v2"

def get_poverty_data(country="CR", indicator="SI.POV.DDAY"):
    """
    Consulta datos de pobreza desde el API del Banco Mundial.
    country = código ISO del país (CR = Costa Rica, MX = México, etc)
    indicator = indicador de pobreza (SI.POV.DDAY = pobreza extrema $2.15)
    """

    url = f"{BASE_URL}/country/{country}/indicator/{indicator}?format=json"

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Error en el API: {response.status_code}")

    data = response.json()

    # El resultado viene en dos partes, en data[1] están los valores
    if data[1] is None:
        return []

    poverty_list = []

    for entry in data[1]:
        poverty_list.append({
            "year": entry["date"],
            "value": entry["value"]
        })

    return poverty_list
