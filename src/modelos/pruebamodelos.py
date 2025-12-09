import matplotlib.pyplot as plt
import seaborn as sns
from ModeloML import ModeloML

# =========================================================
# EJECUCIÓN COMPLETA DE AMBOS MODELOS
# =========================================================

print("Cargando modelo...\n")

modelo = ModeloML("../../data/processed/conare_modelo.csv")

# 1. Cargar datos
df = modelo.cargar_datos()

print("\n===== CLASIFICACIÓN =====\n")

# 2. Clasificación
modelo.preparar_clasificacion()
modelo.entrenar_clasificacion()
accuracy, cm = modelo.evaluar_clasificacion()

# Guardar matriz de confusión
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap="Blues")
plt.title("Matriz de Confusión - Clasificación")
plt.xlabel("Predicho")
plt.ylabel("Real")
plt.tight_layout()
plt.savefig("../../data/processed/matriz_confusion_clasificacion.png")
plt.close()

# 3. Importancia de variables
importancias = modelo.importancia_variables(guardar_csv=True)


print("\n===== REGRESIÓN =====\n")

# 4. Regresión
modelo.preparar_regresion()
modelo.entrenar_regresion()
mae, rmse = modelo.evaluar_regresion()

# Gráfico real vs predicho
plt.figure(figsize=(6, 6))
y_test = modelo.yr_test
y_pred = modelo.modelo_regresion.predict(modelo.Xr_test)

sns.scatterplot(x=y_test, y=y_pred, alpha=0.6)
plt.xlabel("Valores reales (años matriculado)")
plt.ylabel("Predicción")
plt.title("Regresión - Real vs Predicho")
plt.grid(True)
plt.tight_layout()
plt.savefig("../../data/processed/regresion_real_vs_predicho.png")
plt.close()

print("\n🔹 Ejecución finalizada correctamente.")
print("🔹 Resultados guardados en data/processed/")
