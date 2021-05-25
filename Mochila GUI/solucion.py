from tkinter import*
import tkinter
from nuevo_problema import *
from menu_problema import *

a=("a","b","c","d","e","1","2","3","f","4","5","6","g","7","8","9")
class solucion:
    def __init__(self):
        # Creacion de la ventana solucion
        
        solucion = Tk()
        solucion.geometry("600x400+0+0")
        solucion.title("Asignacion caso mochila")

        #Llamada al menu problema
        menu_problema(solucion)
        
        # Creacion de la funcion que genera la matriz 
        def genera_matriz(a):
            s=0
            for r in range(0,4):
                for c in range(0,4):
                    b=a[s]
                    s+=1
                    celda = Label(matriz,text=b, width=8)
                    celda.grid(padx=5, pady=5, row=r, column=c)
                    celda.config(fg="white",    # letra
                        bg="skyblue",   # caja
                        font=("Verdana",12))

        # Creacion del marco matriz
        matriz = Frame(solucion)
        genera_matriz(a)
        matriz.pack()

        #Creacion del marco botones
        botones= Frame(solucion)
        botones.pack(side= tkinter.BOTTOM)

        #Boton cancelar
        cancelar=Button(botones, text="Cancelar")#,command=ejercicio)
        cancelar.grid(column=0,row=2,padx=4,pady=4)

        #Boton correr
        ok=Button(botones, text="Correr")#,command=ejercicio)
        ok.grid(column=5,row=2,padx=4,pady=4)


        solucion.mainloop()

# solucion=solucion()