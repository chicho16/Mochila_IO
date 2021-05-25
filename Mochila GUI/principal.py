from tkinter import *
from nuevo_problema import nuevo_problema

class principal:
    def __init__(self):
        #Creacion de otras Ventanas
            
        # Creacion de la ventana principal
        
        self.principal = Tk()
        self.principal.geometry("600x600+0+0")
        self.principal.title("Ventana principal")

        # Creacion de la barra de menus
        self.barra_menu = Menu(self.principal)

        # Creacion de menus
        self.archivo = Menu(self.barra_menu)
        self.acerca_de = Menu(self.barra_menu)

        # Creacion de los comandos para menu archivo
        self.archivo.add_command(label="Nuevo Problema", command=self.abrir_nuevo)
        self.archivo.add_command(label="Cargar problema")
        self.archivo.add_command(label="Guardar")
        self.archivo.add_command(label="Salir")

        # Agregar los menus a la barra de menus
        self.barra_menu.add_cascade(label="Archivo", menu=self.archivo)
        self.barra_menu.add_cascade(label="Acerca de", menu=self.acerca_de)

        # Agregar la barra a principal
        self.principal.config(menu=self.barra_menu)

        self.principal.mainloop()

    def abrir_nuevo(self):
        self.principal.destroy()
        nuevo_problema()