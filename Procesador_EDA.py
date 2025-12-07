
import numpy as np
import pandas as pd

#EDA
class ProcesadorEDA:
    @property
    def df(self):
        return self._df

    @df.setter
    def df(self, archivo_csv):
        try:
            self._df = pd.read_csv(archivo_csv)
            print("Archivo cargado correctamente:", archivo_csv)
        except Exception as e:
            print("Error cargando el archivo:", archivo_csv)
            print(e)


    def __init__(self, archivo_csv=None):
        self._df = pd.DataFrame()
        if archivo_csv:
            self.df = archivo_csv


    def correlacion_educacion_pobreza(self):
        educ = [c for c in self.df.columns if "EDU" in c.upper() or "NIVEL" in c.upper()]
        pobreza = [c for c in self.df.columns if "IPM" in c.upper() or "POBRE" in c.upper()]

        cols = educ + pobreza
        df_temp = self.df[cols].select_dtypes(include=[np.number])
        print("\n--- Correlación Educación vs Pobreza ---")
        print(df_temp.corr())
        return df_temp.corr()


    def correlacion_ingreso_pobreza(self):
        ingreso = [c for c in self.df.columns if "ING" in c.upper() or "SAL" in c.upper()]
        pobreza = [c for c in self.df.columns if "IPM" in c.upper() or "POBRE" in c.upper()]

        cols = ingreso + pobreza
        df_temp = self.df[cols].select_dtypes(include=[np.number])
        print("\n--- Correlación Ingresos vs Pobreza ---")
        print(df_temp.corr())
        return df_temp.corr()

    def correlacion_servicios_pobreza(self):
        servicios = [c for c in self.df.columns if any(x in c.upper() for x in ["AGUA", "LUZ", "INTERNET", "SANEAM"]) ]
        pobreza = [c for c in self.df.columns if "IPM" in c.upper() or "POBRE" in c.upper()]

        cols = servicios + pobreza
        df_temp = self.df[cols].select_dtypes(include=[np.number])
        print("\n--- Correlación Servicios Básicos vs Pobreza ---")
        print(df_temp.corr())
        return df_temp.corr()


    def correlacion_vivienda_pobreza(self):
        vivienda = [c for c in self.df.columns if any(x in c.upper() for x in ["PISO", "TECHO", "PARED", "VIVI"]) ]
        pobreza = [c for c in self.df.columns if "IPM" in c.upper() or "POBRE" in c.upper()]

        cols = vivienda + pobreza
        df_temp = self.df[cols].select_dtypes(include=[np.number])
        print("\n--- Correlación Vivienda vs Pobreza ---")
        print(df_temp.corr())
        return df_temp.corr()


#Pruebas
ruta = "datos_inec_convertidos_limpios.csv"

p = ProcesadorEDA(ruta)

p.correlacion_educacion_pobreza()
p.correlacion_ingreso_pobreza()
p.correlacion_servicios_pobreza()
p.correlacion_vivienda_pobreza()

