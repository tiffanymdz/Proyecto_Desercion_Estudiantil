import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, mean_absolute_error, mean_squared_error

# -----------------------------------------------------------
#  DETECCIÓN AUTOMÁTICA DE LA RUTA BASE DEL PROYECTO
# -----------------------------------------------------------
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

class ModeloML:

    def __init__(self, ruta_datos):
        """
        ruta_datos: ruta relativa al proyecto, ej:
        data/processed/conare_modelo.csv
        """
        self.ruta_datos = ruta_datos
        self.df = None

        # Espacios para los modelos
        self.modelo_clasificacion = None
        self.modelo_regresion = None

        # Datos clasificación
        self.Xc_train = None
        self.Xc_test = None
        self.yc_train = None
        self.yc_test = None

        # Datos regresión
        self.Xr_train = None
        self.Xr_test = None
        self.yr_train = None
        self.yr_test = None


    # -----------------------------------------------------------
    #  CARGAR DATOS
    # -----------------------------------------------------------
    def cargar_datos(self):
        ruta_completa = os.path.join(BASE_DIR, self.ruta_datos)
        print(f"Cargando datos desde: {ruta_completa}")

        self.df = pd.read_csv(ruta_completa)
        print(" Datos cargados correctamente.")
        return self.df


    # -----------------------------------------------------------
    #  PREPARAR CLASIFICACIÓN
    # -----------------------------------------------------------
    def preparar_clasificacion(self):
        print("\n Preparando datos para CLASIFICACIÓN...")

        # Variable objetivo: DESERTA
        self.yc = self.df["DESERTA"]

        # Variables predictoras
        X = self.df.drop(columns=["DESERTA", "ANIOS_MATRICULADO", "ID_ESTUDIANTE"])

        # Dummificar columnas (pero evitando explosión dimensional)
        X = self._limpiar_columnas_grandes(X)
        self.Xc = pd.get_dummies(X, drop_first=True)

        # División train/test
        self.Xc_train, self.Xc_test, self.yc_train, self.yc_test = train_test_split(
            self.Xc, self.yc, test_size=0.2, random_state=42
        )

        print(f" Clasificación lista. Shape final: {self.Xc.shape}")
        return self.Xc_train, self.Xc_test, self.yc_train, self.yc_test


    # -----------------------------------------------------------
    #  ENTRENAR CLASIFICACIÓN
    # -----------------------------------------------------------
    def entrenar_clasificacion(self):
        print("\n Entrenando modelo de CLASIFICACIÓN (Random Forest)...")

        self.modelo_clasificacion = RandomForestClassifier(
            n_estimators=200,
            max_depth=12,
            min_samples_split=4,
            min_samples_leaf=2,
            n_jobs=-1,
            random_state=42
        )

        self.modelo_clasificacion.fit(self.Xc_train, self.yc_train)
        print(" Modelo entrenado.")
        return self.modelo_clasificacion


    # -----------------------------------------------------------
    #  EVALUAR CLASIFICACIÓN
    # -----------------------------------------------------------
    def evaluar_clasificacion(self):
        print("\n Evaluando CLASIFICACIÓN...")
        y_pred = self.modelo_clasificacion.predict(self.Xc_test)

        acc = accuracy_score(self.yc_test, y_pred)
        print(f" Accuracy: {acc:.4f}")

        return acc


    # -----------------------------------------------------------
    #  PREPARAR REGRESIÓN
    # -----------------------------------------------------------
    def preparar_regresion(self):
        print("\n Preparando datos para REGRESIÓN...")

        self.yr = self.df["ANIOS_MATRICULADO"]

        X = self.df.drop(columns=["DESERTA", "ANIOS_MATRICULADO", "ID_ESTUDIANTE"])

        # Eliminar columnas gigantes (las que tienen demasiadas categorías)
        X = self._limpiar_columnas_grandes(X)

        # Dummificar
        self.Xr = pd.get_dummies(X, drop_first=True)

        # División
        self.Xr_train, self.Xr_test, self.yr_train, self.yr_test = train_test_split(
            self.Xr, self.yr, test_size=0.2, random_state=42
        )

        print(f" Regresión lista. Shape final: {self.Xr.shape}")
        return self.Xr_train, self.Xr_test, self.yr_train, self.yr_test


    # -----------------------------------------------------------
    #  ENTRENAR REGRESIÓN (Lineal)
    # -----------------------------------------------------------
    def entrenar_regresion(self):
        print("\n Entrenando modelo de REGRESIÓN (Linear Regression)...")

        self.modelo_regresion = LinearRegression()
        self.modelo_regresion.fit(self.Xr_train, self.yr_train)

        print("✔ Modelo de regresión entrenado.")
        return self.modelo_regresion


    # -----------------------------------------------------------
    #  EVALUAR REGRESIÓN
    # -----------------------------------------------------------
    def evaluar_regresion(self):
        print("\n Evaluando REGRESIÓN...")

        y_pred = self.modelo_regresion.predict(self.Xr_test)

        mae = mean_absolute_error(self.yr_test, y_pred)
        rmse = np.sqrt(mean_squared_error(self.yr_test, y_pred))

        print(f" MAE: {mae:.4f}")
        print(f" RMSE: {rmse:.4f}")

        return mae, rmse


    # -----------------------------------------------------------
    #  FUNCIÓN PARA REDUCIR COLUMNAS GIGANTES
    # -----------------------------------------------------------
    def _limpiar_columnas_grandes(self, X):
        """
        Elimina columnas categóricas con más de 30 categorías.
        Evita explosión de dummies y alta carga computacional.
        """
        columnas_a_eliminar = []

        for col in X.columns:
            if X[col].dtype == "object" and X[col].nunique() > 30:
                print(f" Eliminando columna enorme: {col} ({X[col].nunique()} categorías)")
                columnas_a_eliminar.append(col)

        X = X.drop(columns=columnas_a_eliminar)
        return X
