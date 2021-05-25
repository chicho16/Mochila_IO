from Item import Item
from Mochila import Mochila

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

mochila = Mochila(15, items2)
mochila.crear_etapas()
# mochila.print_etapas()
# mochila.generar_tablas()
mochila.resolver()
mochila.print_solucion()