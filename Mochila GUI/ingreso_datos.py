from tkinter import *
# from principal import principal
from menu_problema import menu_problema
from solucion import solucion


class ingreso_datos:
    def __init__(self,cant,cap):
        self.cant = cant
        # a=nuevo_problema.
        # Creacion de la ventana problema
        
        self.ventana = Tk()
        self.ventana.geometry("600x400+0+0")
        self.ventana.title("Asignacion caso mochila")

        #Llamada al menu problema
        menu_problema(self.ventana) # Veremos        

        # Creacion del marco matriz
        self.matriz_problema = Frame(self.ventana)
        self.genera_matriz()
        self.matriz_problema.pack()

        #Creacion del marco botones
        self.botones= Frame(self.ventana)
        self.botones.pack(side= BOTTOM)

        #Boton cancelar
        self.cancelar=Button(self.botones, text="Cancelar",command=self.cancelar)
        self.cancelar.grid(column=0,row=2,padx=4,pady=4)

        #Boton correr
        # self.ok=Button(self.botones, text="Correr",command=self.generar_ventana_solucion)
        self.ok=Button(self.botones, text="Correr",command=self.get_datos_tabla)
        self.ok.grid(column=5,row=2,padx=4,pady=4)


        self.ventana.mainloop()

# Creacion de la funcion que genera la matriz 
    def genera_matriz(self):
        self.matriz = []
        for r in range(0,self.cant):
            fila = []
            for c in range(0, 3):
                celda = Entry(self.matriz_problema, width=8)
                celda.grid(padx=5, pady=5, row=r, column=c)
                celda.insert(0, '({}, {})'.format(r, c))
                celda.config(fg="white",    # Foreground
                            bg="skyblue3",   # Background
                            font=("Verdana",12))
                fila.append(celda)
            self.matriz.append(fila)

    def get_datos_tabla(self):
        nombres = []
        pesos = []
        utilidades = []
        for fila in self.matriz:
            nombres.append(fila[0].get())
            pesos.append(fila[1].get())
            utilidades.append(fila[2].get())

        print('Nombres: ', nombres)
        print('Pesos: ', pesos)
        print('Utilidades: ', utilidades)
        print('SOLUCION DEL PROBLEMA')
        self.generar_ventana_solucion()

#Creacion de otras Ventanas
    def cancelar(self):
        self.ventana.destroy()

    def generar_ventana_solucion(self):
        # self.ventana.destroy()
        solucion()