import tkinter 
from model.conexion_db import *
from tkinter import ttk,messagebox
import tkinter as tk
from model.pelicula_dao import *

from tkinter import *



def barra_menu(root):
    barra_menu = tkinter.Menu(root)
    root.config(menu=barra_menu,width=300,height=300)

    menu_inicio = tkinter.Menu(barra_menu,tearoff=0)
    menu_consulta= tkinter.Menu(barra_menu,tearoff=0)
    menu_ayuda= tkinter.Menu(barra_menu,tearoff=0)

    barra_menu.add_cascade(label='Inicio',menu = menu_inicio)
    barra_menu.add_cascade(label='Consultas',menu = menu_consulta)
    barra_menu.add_cascade(label='Configuración')
    barra_menu.add_cascade(label='Ayuda',menu=menu_ayuda)
    #Add the menu inicio
    menu_inicio.add_command(label='Salir',command=root.destroy)
    #Add the menu ayuda
    menu_ayuda.add_command(label='Acerca de')
    #Add the menu consulta
    menu_consulta.add_command(label='Ir al formulario de búsqueda',command = abrir_ventana_secundaria)


def abrir_ventana_secundaria():

    # Crear una ventana secundaria.
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title("Ventana secundaria")
    ventana_secundaria.title("Consultas")
    ventana_secundaria.geometry("400x400")


class Frame(tkinter.Frame):

    def __init__(self,root=None):
        super(). __init__(root)
        self.root = root
        self.pack()
        self.config(width = 480, height = 320)
        self.id_pelicula = None
        

        #Inicilaizar en el constructor
        self.campos_pelicula()

        
        #inicializar en el constructor
        self.deshabilitar_campos()

        #inicializar en el constructor
        self.tabla_peliculas()

        
        
    def campos_pelicula(self):
        # Label de cada campo
        self.label_nombre = tkinter.Label(self,text='Nombre : ')
        self.label_nombre.config(font = ('Arial',10))
        self.label_nombre.grid(row=0, column=0, padx=10,pady=10,columnspan=2)

        self.label_duracion = tkinter.Label(self,text='Duración : ')
        self.label_duracion.config(font = ('Arial',10))
        self.label_duracion.grid(row=1, column=0, padx=10,pady=10,columnspan=2)

        self.label_genero = tkinter.Label(self,text='Género : ')
        self.label_genero.config(font = ('Arial',10))
        self.label_genero.grid(row=2, column=0, padx=10,pady=10,columnspan=2)

        #Entrys de cada campo
        self.mi_nombre = tkinter.StringVar()
        self.entry_nombre = tkinter.Entry(self,textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50,font=('Arial',10))
        self.entry_nombre.grid(row=0,column=1,padx=10,pady=10,columnspan=3)

        self.mi_duracion = tkinter.StringVar()
        self.entry_duracion = tkinter.Entry(self,textvariable=self.mi_duracion)
        self.entry_duracion.config(width=50,font=('Arial',10))
        self.entry_duracion.grid(row=1,column=1,padx=10,pady=10,columnspan=3)


        #Combobox de campo géneros para
        self.mi_genero= tkinter.StringVar()
        self.combo_genero= ttk.Combobox(self,textvariable=self.mi_genero)
        self.combo_genero['values']=['Acción','Animación','Aventuras','Ciencia Ficción','Comedia','No-Ficción','Drama','Fantasía','Musical','Suspenso','Terror']
        self.combo_genero.config(width=47,font=('Arial',10))
        self.combo_genero.grid(row=2,column=1,padx=10,pady=10,columnspan=3)


        #Buttons

        self.button_nuevo = tkinter.Button(self,text= 'Nuevo',command=self.habilitar_campos)
        self.button_nuevo.config(width=20,font=('Arial',10,'bold'),fg='white',bg='#58B68E',cursor='hand2',activebackground='#0ACF8F')
        self.button_nuevo.grid(row=3,column=0,padx=10,pady=10)

        self.button_guardar = tkinter.Button(self,text= 'Guardar',command=self.guardar_datos)
        self.button_guardar.config(width=20,font=('Arial',10,'bold'),fg='white',bg='#1B74D1',cursor='hand2',activebackground='#2C96D1')
        self.button_guardar.grid(row=3,column=1,padx=10,pady=10)

        self.button_cancelar = tkinter.Button(self,text= 'Cancelar',command=self.deshabilitar_campos)
        self.button_cancelar.config(width=20,font=('Arial',10,'bold'),fg='white',bg='#C73C10',cursor='hand2',activebackground='#C75210')
        self.button_cancelar.grid(row=3,column=2,padx=10,pady=10)

    def habilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')

        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.combo_genero.config(state='normal')

        self.button_guardar.config(state='normal')
        self.button_cancelar.config(state='normal')

    def deshabilitar_campos(self):
        self.id_pelicula=None
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')

        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.combo_genero.config(state='disabled')

        self.button_guardar.config(state='disabled')
        self.button_cancelar.config(state='disabled')

    def guardar_datos(self):

        pelicula = Pelicula(
            self.mi_nombre.get(),
            self.mi_duracion.get(),
            self.mi_genero.get(),
        )

        if self.id_pelicula == None : 
            guardar(pelicula)
        else:
            editar(pelicula,self.id_pelicula)
        self.tabla_peliculas()

        self.deshabilitar_campos()

    
    def tabla_peliculas(self):
        # Recuperar la lista de peliculas
        self.lista_peliculas = listar()
        self.lista_peliculas.reverse()
        
        
        self.tabla = ttk.Treeview(self,column=('nombre','duracion','genero'))
        self.tabla.grid(row=6, column=0, columnspan=4, sticky='nse')
    
        #Scrollbar para la tabla
        self.scroll= ttk.Scrollbar(self,orient ='vertical',command= self.tabla.yview)
        self.scroll.grid(row=6, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand= self.scroll.set)

        self.tabla.heading('#0',text='ID')
        self.tabla.heading('#1',text='NOMBRE')
        self.tabla.heading('#2',text='DURACIÓN')
        self.tabla.heading('#3',text='GÉNERO')

        for lista in self.lista_peliculas:
            #self.tabla.insert('',tkinter.END,values=lista)
            self.tabla.insert('',0, text=lista[0],values=(lista[1],lista[2],lista[3]))

        
        #Button editar
        self.button_editar = tkinter.Button(self,text= 'Editar',command=self.editar_datos)
        self.button_editar.config(width=20,font=('Arial',10,'bold'),fg='white',bg='#58B68E',cursor='hand2',activebackground='#0ACF8F')
        self.button_editar.grid(row=7,column=0,padx=10,pady=10)

        #Button eliminar
        self.button_eliminar = tkinter.Button(self,text= 'Eliminar',command=self.eliminar_datos)
        self.button_eliminar.config(width=20,font=('Arial',10,'bold'),fg='white',bg='#C73C10',cursor='hand2',activebackground='#C75210')
        self.button_eliminar.grid(row=7,column=1,padx=10,pady=10)

    
        #Button salir
        self.button_salir = tkinter.Button(self,text= 'Salir',command=self.salir)
        self.button_salir.config(width=20,font=('Arial',10,'bold'),fg='white',bg='#2576F5',cursor='hand2',activebackground='#195FF5')
        self.button_salir.grid(row=3,column=3,padx=10,pady=10)
        
        # Self Busqueda
        self.label_busqueda = tkinter.Label(self,text='Buscar Película : ')
        self.label_busqueda.config(font = ('Arial',10))
        self.label_busqueda.grid(row=7, column=2, padx=10,pady=10)

        # Self Busqueda
        self.label_titulo = tkinter.Label(self,text='Todos los derechos reservados ®.')
        self.label_titulo.config(font = ('Arial',10))
        self.label_titulo.grid(row=8, column=0, padx=10,pady=10 ,columnspan=2)

        #Entry busqueda
        self.mi_busqueda = tkinter.StringVar()
        self.entry_busqueda = tkinter.Entry(self,textvariable=self.mi_busqueda)
        self.entry_busqueda.config(width=24,font=('Arial',10))
        self.entry_busqueda.grid(row=7,column=3,padx=10,pady=10,columnspan=1)

        #Button busqueda
        self.button_busqueda = tkinter.Button(self,text= 'Buscar',command=self.busqueda_datos)
        self.button_busqueda.config(width=20,font=('Arial',10,'bold'),fg='white',bg='#58B68E',cursor='hand2',activebackground='#0ACF8F')
        self.button_busqueda.grid(row=8,column=2,padx=10,pady=10)
        
        #Button Limpiar

        self.button_limpiar = tkinter.Button(self,text= 'Limpiar',command=self.limpiar)
        self.button_limpiar.config(width=20,font=('Arial',10,'bold'),fg='white',bg='#58B68E',cursor='hand2',activebackground='#0ACF8F')
        self.button_limpiar.grid(row=8,column=3,padx=10,pady=10)


    def busqueda_datos(self):
        
        nombres=self.mi_busqueda.get()
        nombres= str("'"+ nombres + "'")
        nombre_buscado = busqueda(nombres)
        self.tabla.delete(*self.tabla.get_children())
        for dato in nombre_buscado:  
            self.tabla.insert('',0, text=dato[0],values=(dato[1],dato[2],dato[3]))
        

    def editar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
            self.nombre_pelicula = self.tabla.item(self.tabla.selection())['values'][0]
            self.duracion_pelicula = self.tabla.item(self.tabla.selection())['values'][1]
            self.genero_pelicula = self.tabla.item(self.tabla.selection())['values'][2]
            
            self.habilitar_campos()

            self.entry_nombre.insert(0,self.nombre_pelicula)
            self.entry_duracion.insert(0,self.duracion_pelicula)
            self.combo_genero.insert(0,self.genero_pelicula)
            
        except:
            titulo= 'Editar el registro'
            mensaje = 'No ha seleccionado ningún registro'
            messagebox.showerror(titulo,mensaje)

    

    def eliminar_datos(self):
        try:
            resultado = messagebox.askquestion("Eliminar registro", "¿Está seguro que desea eliminar el registro?")
            if resultado == "yes":
                self.id_pelicula= self.tabla.item(self.tabla.selection())['text']
                eliminar(self.id_pelicula)

                self.tabla_peliculas()
                self.id_pelicula=None
        except:
            self.tabla_peliculas()
    

    def salir(self):
        resultado = messagebox.askquestion("Salir del sistema", "¿Está seguro que desea salir de la aplicación?")
        if resultado == "yes":
            self.root.destroy()
        else:
            self.tabla_peliculas()

    def limpiar(self):
        self.entry_busqueda.delete(0,END)   
        self.tabla_peliculas()
