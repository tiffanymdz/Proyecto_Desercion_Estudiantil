# transformar archivo .SAV a .csv

import pyreadstat
import pandas as pd

df, meta = pyreadstat.read_sav("../../data/raw/GPES-ELAB-GEBD-ENAHO-2025_BdPublica.sav")
print(df.head())
print(df.columns)

df.to_csv("../../data/processed/datos_inec_convertidos1.csv", index=False)


# limpiar dataset del INEC

import csv
print("Usando módulo csv desde:", csv.__file__)


ruta = "../../data/processed/datos_inec_convertidos1.csv"

df = pd.read_csv(ruta)

print(df.head())
print("Datos cargados correctamente ")


print(df.isnull().sum())

ruta = "../../data/processed/datos_inec_convertidos1.csv"
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

ruta_salida = "../../data/processed/datos_inec_convertidos1.csv"
df.to_csv(ruta_salida, index=False)

print("\nArchivo limpio guardado en:")
print(ruta_salida)


print(df.isnull().sum().sum())

