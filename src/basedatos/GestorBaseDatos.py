import pandas as pd
from sqlalchemy import create_engine

class GestorBaseDatos:
    def __init__(self, server, database, driver="ODBC Driver 17 for SQL Server", trusted_connection="yes"):
        """
        Inicializa la conexión a SQL Server usando SQLAlchemy.
        """
        self.server = server
        self.database = database
        self.driver = driver
        self.trusted_connection = trusted_connection

        self.connection_string = (
            f"mssql+pyodbc://@{self.server}/{self.database}"
            f"?driver={self.driver}&trusted_connection={self.trusted_connection}"
        )

        # Crear el engine (conexión)
        self.engine = create_engine(self.connection_string)
        print(f"Conexión creada con la base '{self.database}' en el servidor '{self.server}'")

    # -----------------------------------------------------------------

    def cargar_csv(self, ruta_archivo, nombre_tabla, modo="replace", chunksize=5000, encoding="utf-8"):
        """
        Carga un CSV a SQL Server.
        modo = 'replace' | 'append'
        """
        print(f"Cargando CSV '{ruta_archivo}' a la tabla '{nombre_tabla}'...")

        df = pd.read_csv(ruta_archivo, encoding=encoding)

        df.to_sql(
            nombre_tabla,
            con=self.engine,
            if_exists=modo,
            index=False,
            chunksize=chunksize
        )

        print("Carga CSV completa")

    # -----------------------------------------------------------------

    def cargar_excel(self, ruta_archivo, hoja, nombre_tabla, modo="replace", chunksize=5000):
        """
        Carga una hoja de un Excel a SQL Server.
        """
        print(f"Cargando Excel '{ruta_archivo}', hoja '{hoja}' a '{nombre_tabla}'...")

        df = pd.read_excel(ruta_archivo, sheet_name=hoja)

        df.to_sql(
            nombre_tabla,
            con=self.engine,
            if_exists=modo,
            index=False,
            chunksize=chunksize
        )

        print("Carga Excel completa")

