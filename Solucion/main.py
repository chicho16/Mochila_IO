from Item import Item
from Mochila import Mochila
from random import randint

# Item(nombre, peso, beneficio)
items1 = [Item('Aceite', 1, 8),
        Item('Azucar', 3, 7),
        Item('Maiz', 2, 7),
        Item('Frijol', 2, 9)]

items2 = [Item('Verde', 12, 4),
        Item('Violeta', 1, 2),
        Item('Celeste', 2, 2),
        Item('Rojo', 1, 1),
        Item('Naranja', 4, 10)]

items3 = [Item('Verde', 4, 4),
        Item('Violeta', 1, 2),
        Item('Celeste', 2, 2),
        Item('Rojo', 2, 1),
        Item('Naranja', 3, 5)]

# SOLUCIONES MULTIPLES
items4 = [Item('Producto 1', 12, 4),
        Item('Producto 2', 5, 2),
        Item('Producto 3', 7, 1)]

items5 = [Item('Producto 1', 4, 5),
        Item('Producto 2', 4, 5),
        Item('Producto 3', 4, 5)]

mochila = Mochila(18, items5)
mochila.crear_etapas()
mochila.resolver()
mochila.print_solucion()

def encontrar_problema_sol_multiple():
    flag = True
    while flag:
        print('Iteracion')
        pesos = (randint(1, 9), randint(1, 9), randint(1, 9))
        utilidades = (randint(1, 10), randint(1, 10), randint(1, 10))
        capacidad = randint(10, 40)
        items = [Item('Producto 1', pesos[0], utilidades[0]),
                 Item('Producto 2', pesos[1], utilidades[1]),
                 Item('Producto 3', pesos[2], utilidades[2])]
        m = Mochila(capacidad, items)
        m.crear_etapas()
        m.resolver()
        conj_sol = m.get_conjunto_solucion()
        print('pesos: ', pesos)
        print('utilidades: ', utilidades)
        print('capacidad: ', capacidad)
        print('SOL ', conj_sol)
        # for i in range(len(conj_sol)):
        #     if i > 0:
        #         if conj_sol[i][0] == conj_sol[i-1][0]:
        #             flag = False
        #         else:
        #             flag = True
        var = input()
        if var != '1':
            flag = False
        m.print_solucion()
    
# encontrar_problema_sol_multiple()
