from tkinter import *
from ingreso_datos import ingreso_datos
# from principal import principal

class nuevo_problema:

    def __init__(self):
        # Creacion de la ventana nuevo problema
        self.ventana = Tk()
        self.ventana.geometry("500x200+0+0")
        self.ventana.title("Nuevo problema")

        #Etiqueta capacidad
        self.etiqueta_capacidad=Label(self.ventana, text="Capacidad de la mochila")
        self.etiqueta_capacidad.grid(column=0,row=1,padx=4,pady=4)
        
        #Caja de texto capacidad
        self.caja_capacidad=IntVar()
        self.texto_capacidad=Entry(self.ventana, textvariable = self.caja_capacidad)
        self.texto_capacidad.grid(column=1,row=1,padx=4,pady=4)

        #Etiqueta cantidad
        self.etiqueta_cantidad=Label(self.ventana, text="Cantidad de articulos a asignar")
        self.etiqueta_cantidad.grid(column=0,row=3,padx=4,pady=4)
        
        #Caja de texto cantidad
        self.caja_cantidad=IntVar()
        self.texto_cantidad=Entry(self.ventana, textvariable= self.caja_cantidad)
        self.texto_cantidad.grid(column=1,row=3,padx=4,pady=4)

        #Boton ok
        self.ok=Button(self.ventana, text="OK",command=self.generar_ingreso_datos)
        self.ok.grid(column=0,row=5,padx=1,pady=4)

        #Boton cancelar
        self.cancelar=Button(self.ventana, text="Cancelar",command = self.cancelar)
        self.cancelar.grid(column=1,row=5,padx=4,pady=4)

        self.ventana.mainloop()

    #Creacion de otras Ventanas
    def cancelar(self):
        # print('muestra ventana principal')
        # principal()
        self.ventana.destroy()
            

    def generar_ingreso_datos(self):
        # self.ventana.destroy()
        cantidad = self.caja_cantidad.get()
        capacidad = self.caja_capacidad.get()
        print('CANTIDAD ', cantidad)
        print('CAPACIDAD ', capacidad)
        ingreso_datos(cantidad, capacidad)