import pandas as pd
import unicodedata

class InformacionModelo:

    def __init__(self, path_excel, sheet_name="Archivo 2021-2024"):
        self.path_excel = path_excel
        self.sheet_name = sheet_name

        self.excel_raw = None
        self.df = None


    # -------------------------------------------------------------
    # Normalizar textos
    # -------------------------------------------------------------
    def normalizar(self, serie):
        return (serie.astype(str)
                .apply(lambda x: unicodedata.normalize("NFKD", x)
                       .encode("ascii", errors="ignore")
                       .decode("utf-8"))
                .str.upper()
                .str.strip()
               )

    # -------------------------------------------------------------
    # 1. Cargar datos
    # -------------------------------------------------------------
    def cargar_datos(self):
        print("Cargando Excel del CONARE...")
        self.excel_raw = pd.read_excel(self.path_excel, sheet_name=self.sheet_name)
        print("Carga completada ✔️")

    # -------------------------------------------------------------
    # 2. Seleccionar columnas relevantes
    # -------------------------------------------------------------
    def seleccionar_columnas(self):
        print("Filtrando columnas útiles...")

        columnas = [
            "AÑO",
            "TIPO_MATRICULA",
            "UNIVERSIDAD",
            "CARRERA",
            "SEXO",
            "EDAD",
            "PROVINCIA_ESTUDIANTE",
            "CANTON_ESTUDIANTE",
            "ZONA_URBANO_RURAL_ESTUDIANTE",
            "GAM_ESTUDIANTE",
            "AREA_CONOCIMIENTO"
        ]

        self.df = self.excel_raw[columnas].copy()

        # Normalización
        self.df["PROVINCIA_ESTUDIANTE"] = self.normalizar(self.df["PROVINCIA_ESTUDIANTE"])
        self.df["CANTON_ESTUDIANTE"] = self.normalizar(self.df["CANTON_ESTUDIANTE"])
        self.df["ZONA_URBANO_RURAL_ESTUDIANTE"] = self.normalizar(
            self.df["ZONA_URBANO_RURAL_ESTUDIANTE"]
        )

        print("Columnas preparadas ✔️")

    # -------------------------------------------------------------
    # 3. Crear llave única para identificar estudiantes
    # -------------------------------------------------------------
    def crear_llave_estudiante(self):
        print("Generando llave única de estudiante...")

        self.df["ID_ESTUDIANTE"] = (
            self.df["UNIVERSIDAD"].astype(str) + "_" +
            self.df["CARRERA"].astype(str) + "_" +
            self.df["SEXO"].astype(str) + "_" +
            self.df["EDAD"].astype(str) + "_" +
            self.df["CANTON_ESTUDIANTE"].astype(str)
        )

        print("Llaves generadas ✔️")

    # -------------------------------------------------------------
    # 4. Crear variable de deserción
    # -------------------------------------------------------------
    def crear_desercion(self):
        print("Creando variable DESERTA...")

        # Años por estudiante
        años = self.df.groupby("ID_ESTUDIANTE")["AÑO"].agg(list)

        deserta = {}

        for estudiante, lista_años in años.items():
            lista_ordenada = sorted(lista_años)

            desertor = 0

            for i in range(len(lista_ordenada) - 1):
                if lista_ordenada[i+1] != lista_ordenada[i] + 1:
                    desertor = 1
                    break

            deserta[estudiante] = desertor

        self.df["DESERTA"] = self.df["ID_ESTUDIANTE"].map(deserta)

        print("Variable DESERTA creada ✔️")

    # -------------------------------------------------------------
    # 5. Crear variable años matriculado
    # -------------------------------------------------------------
    def crear_anios_matriculado(self):
        print("Creando variable ANIOS_MATRICULADO...")

        anios = self.df.groupby("ID_ESTUDIANTE")["AÑO"].transform("nunique")

        self.df["ANIOS_MATRICULADO"] = anios

        print("Variable ANIOS_MATRICULADO creada ✔️")

    # -------------------------------------------------------------
    # 6. Guardar dataset final
    # -------------------------------------------------------------
    def guardar(self, path_salida="../../data/processed/conare_modelo.csv"):
        print(f"Guardando dataset final en {path_salida}...")
        self.df.to_csv(path_salida, index=False, encoding="utf-8")
        print("Dataset final listo ✔️🎉")

    # -------------------------------------------------------------
    # FUNCIÓN PRINCIPAL
    # -------------------------------------------------------------
    def ejecutar_todo(self, path_salida="../../data/processed/conare_modelo.csv"):
        self.cargar_datos()
        self.seleccionar_columnas()
        self.crear_llave_estudiante()
        self.crear_desercion()
        self.crear_anios_matriculado()
        self.guardar(path_salida)
