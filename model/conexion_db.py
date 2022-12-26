import psycopg2

class ConexionDB:
    def __init__(self):
        self.base_datos = psycopg2.connect(dbname="peliculas",user="postgres",password="root",host="localhost")
        self.conexion = self.base_datos
        
        self.cursor = self.conexion.cursor()

    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()