from .conexion_db import ConexionDB
from tkinter import messagebox,Listbox,Frame,W,E,END,ttk


class Pelicula:
    def __init__(self,nombre,duracion,genero):
        self.id_pelicula= None
        self.nombre= nombre
        self.duracion= duracion
        self.genero=genero

    def __str__(self):
        return f'Pelicula[{self.nombre}, {self.duracion}, {self.genero}]'

    
def guardar(pelicula):
    conexion = ConexionDB()
    
    sql = f""" INSERT INTO peliculas (nombre, duracion,genero) 
    VALUES ('{pelicula.nombre}', '{pelicula.duracion}', '{pelicula.genero}') """

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Conexión al registro'
        mensaje = 'La tabla películas no está creada en la base de datos'
        messagebox.showerror(titulo,mensaje)


def editar(pelicula,id_pelicula):
    conexion = ConexionDB()

    sql= f"""UPDATE peliculas SET nombre='{pelicula.nombre}', duracion='{pelicula.duracion}',
    genero ='{pelicula.genero}'
    WHERE id_pelicula= {id_pelicula}"""
    

    conexion.cursor.execute(sql)
    conexion.cerrar()


def eliminar(id_pelicula):
    conexion = ConexionDB()

    sql= f"""DELETE FROM peliculas WHERE id_pelicula={id_pelicula}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Eliminar el registro'
        mensaje = 'No ha seleccionado ningún registro'
        messagebox.showerror(titulo,mensaje)



def listar():
    conexion=ConexionDB()
    lista_peliculas = []
    sql = 'SELECT * FROM peliculas'

    try:
        conexion.cursor.execute(sql)
        lista_peliculas = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexión al registro'
        mensaje = 'Crea la tabla en la base de datos'
        messagebox.showwarning(titulo,mensaje)
    
    return lista_peliculas
    

def busqueda(nombre):
        conexion = ConexionDB()
        sql= "SELECT * FROM peliculas WHERE nombre = {}".format(nombre)
        
        conexion.cursor.execute(sql)
        lista_peliculas = conexion.cursor.fetchall()
        conexion.cerrar()
        
        return lista_peliculas