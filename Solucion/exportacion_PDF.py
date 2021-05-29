from Mochila import Mochila
from Item import Item
## Introduccion de datos al problema
## Atributos de item: nombre, peso, utilidad
items = [Item('Producto 1', 4, 5),
        Item('Producto 2', 4, 5),
        Item('Producto 3', 4, 5)]

##  Creacion de la mochila, parametros: capacidad, lista de items
mochila = Mochila(19, items)

## Resolucion del problema
mochila.crear_etapas()
mochila.resolver()
## Nota, todas las lineas anteriores no seran necesarias a la hora de
## la exportacion en PDF, ya se ejecutaran por medio de la interfaz,
## solo estan presentes por motivos de prueba

## Funcion que retorna la formulacion del problema, datos de este
## El primer dato sera la capacidad de la mochila, los demas datos son los items
datos_problema = mochila.get_formulacion_problema()

#Impresion de los datos
print('Capacidad: ', datos_problema[0])
for item in datos_problema[1:]:
    print(item)
    
## Funcion que retorna todas las soluciones del problema
## Nota, se debe resolver el problema antes de llamar a esta funcion
## estructura soluciones = (solucion1, solucion2...)
## solucion = (nombre, cantidad, peso, utilidad)
soluciones = mochila.get_soluciones()

# Impresion de las soluciones
print('\nSolucion del problema:')
for i in range(len(soluciones)):
    print('\nSolucion: ', i+1)
    for fila in soluciones[i]:
        print(fila)
        
## Funcion que retorna lista con pesos usados de cada solucion
## Cada peso pertenece a una solucion, en orden 1, 2, 3...
pesos_sol = mochila.get_pesos_sol()

## Funcion que retorna utilidad de la solucion (todas las soluciones tienen
## la misma utilidad)
utilidad_neta = mochila.get_utilidad_neta()

