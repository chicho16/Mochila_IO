class Item:
    def __init__(self, nombre, peso, beneficio):
        self.nombre = nombre
        self.beneficio = beneficio
        self.peso = peso
    
    def __str__(self):
        return 'Item: ' + self.nombre