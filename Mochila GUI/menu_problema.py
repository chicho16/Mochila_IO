from tkinter import*
from nuevo_problema import *

class menu_problema:
    def __init__(self,v):
        #Creacion de otras Ventanas
        def nuevo():
            v.destroy()
            nuevo=nuevo_problema()

        # Creacion de la barra de menus
        barra_menu = Menu(v)

        # Creacion de menus
        archivo = Menu(barra_menu)
        exportar = Menu(barra_menu)
        ayuda = Menu(barra_menu)

        # Creacion de los comandos para menu archivo
        archivo.add_command(label="Nuevo Problema", command=nuevo)
        archivo.add_command(label="Cargar problema")
        archivo.add_command(label="Guardar")
        archivo.add_separator()
        archivo.add_command(label="Salir")

        # Creacion de los comandos para menu exportar
        exportar.add_command(label="Como DOC")
        exportar.add_command(label="Como PDF")
        exportar.add_command(label="Como JPG")

        # Creacion de los comandos para menu ayuda
        ayuda.add_command(label="Manual de uso")
        ayuda.add_command(label="Acerca de")

        # Agregar los menus a la barra de menus
        barra_menu.add_cascade(label="Archivo", menu=archivo)
        barra_menu.add_cascade(label="Exportar", menu=exportar)
        barra_menu.add_cascade(label="Ayuda", menu=ayuda)
        
        # Agregar la barra a principal
        v.config(menu=barra_menu)
