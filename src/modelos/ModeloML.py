import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix,
    mean_absolute_error, mean_squared_error
)


class ModeloML:

    def __init__(self, ruta_datos):
        """
        Inicializa el modelo con la ruta al dataset procesado.
        """
        self.ruta_datos = ruta_datos
        self.df = None

        # Clasificación
        self.Xc = None
        self.yc = None
        self.Xc_train = None
        self.Xc_test = None
        self.yc_train = None
        self.yc_test = None
        self.modelo_clasificacion = None

        # Regresión
        self.Xr = None
        self.yr = None
        self.Xr_train = None
        self.Xr_test = None
        self.yr_train = None
        self.yr_test = None
        self.modelo_regresion = None

    # ==============================================================
    # 1. Cargar dataset
    # ==============================================================
    def cargar_datos(self):
        self.df = pd.read_csv(self.ruta_datos)
        print("✔ Datos cargados correctamente.")
        return self.df

    # ==============================================================
    # 2. PREPARAR VARIABLES PARA CLASIFICACIÓN
    # ==============================================================
    def preparar_clasificacion(self):
        print("Preparando datos para CLASIFICACIÓN...")

        self.yc = self.df["DESERTA"]

        X = self.df.drop(columns=[
            "DESERTA", "ID_ESTUDIANTE", "ANIOS_MATRICULADO"
        ])

        self.Xc = pd.get_dummies(X, drop_first=True)

        self.Xc_train, self.Xc_test, self.yc_train, self.yc_test = train_test_split(
            self.Xc, self.yc, test_size=0.2, random_state=42, stratify=self.yc
        )

        print("✔ Clasificación lista.")
        return self.Xc_train, self.Xc_test, self.yc_train, self.yc_test

    # ==============================================================
    # 3. ENTRENAR CLASIFICACIÓN
    # ==============================================================
    def entrenar_clasificacion(self):
        print("Entrenando modelo de CLASIFICACIÓN...")

        self.modelo_clasificacion = RandomForestClassifier(
            n_estimators=300,
            class_weight="balanced",
            random_state=42
        )

        self.modelo_clasificacion.fit(self.Xc_train, self.yc_train)
        print("✔ Modelo de clasificación entrenado.")
        return self.modelo_clasificacion

    # ==============================================================
    # 4. EVALUAR CLASIFICACIÓN
    # ==============================================================
    def evaluar_clasificacion(self, guardar_imagen=False):
        y_pred = self.modelo_clasificacion.predict(self.Xc_test)

        accuracy = accuracy_score(self.yc_test, y_pred)
        print(f"\n📊 Accuracy: {accuracy:.4f}")

        print("\n📄 Reporte:")
        print(classification_report(self.yc_test, y_pred))

        cm = confusion_matrix(self.yc_test, y_pred)

        plt.figure(figsize=(6, 4))
        sns.heatmap(cm, annot=True, fmt='d', cmap="Blues")
        plt.title("Matriz de Confusión - Clasificación")
        plt.xlabel("Predicción")
        plt.ylabel("Real")

        if guardar_imagen:
            plt.savefig(".../data/processed/matriz_confusion_clasificacion.png")
            print("✔ Imagen guardada.")

        plt.show()

        return accuracy, cm

    # ==============================================================
    # 5. PREPARAR VARIABLES PARA REGRESIÓN
    # ==============================================================
    def preparar_regresion(self):
        print("Preparando datos para REGRESIÓN...")

        self.yr = self.df["ANIOS_MATRICULADO"]

        X = self.df.drop(columns=[
            "DESERTA", "ID_ESTUDIANTE", "ANIOS_MATRICULADO"
        ])

        self.Xr = pd.get_dummies(X, drop_first=True)

        self.Xr_train, self.Xr_test, self.yr_train, self.yr_test = train_test_split(
            self.Xr, self.yr, test_size=0.2, random_state=42
        )

        print("✔ Regresión lista.")
        return self.Xr_train, self.Xr_test, self.yr_train, self.yr_test

    # ==============================================================
    # 6. ENTRENAR REGRESIÓN
    # ==============================================================
    def entrenar_regresion(self):
        print("Entrenando modelo de REGRESIÓN...")

        self.modelo_regresion = RandomForestRegressor(
            n_estimators=300,
            random_state=42
        )

        self.modelo_regresion.fit(self.Xr_train, self.yr_train)
        print("✔ Modelo de regresión entrenado.")
        return self.modelo_regresion

    # ==============================================================
    # 7. EVALUAR REGRESIÓN
    # ==============================================================
    def evaluar_regresion(self):
        y_pred = self.modelo_regresion.predict(self.Xr_test)

        mae = mean_absolute_error(self.yr_test, y_pred)
        rmse = np.sqrt(mean_squared_error(self.yr_test, y_pred))

        print(f"\n📏 MAE: {mae:.4f}")
        print(f"📐 RMSE: {rmse:.4f}")

        return mae, rmse
