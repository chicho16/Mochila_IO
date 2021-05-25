from Etapa import Etapa

class Mochila:
    def __init__(self, capacidad, items):
        self.capacidad = capacidad
        self.items = items
        self.etapas = []
        
    def suma_pesos(self):
        tot = 0
        for i in self.items:
            tot += i.peso
        return tot

    def crear_etapas(self):
        e = Etapa(self.capacidad, self.capacidad)
        self.etapas.append(e)
        
        self.items.reverse()
        
        for item in self.items[1:]:
                
            if self.suma_pesos() <= self.capacidad:
                min_x = 0
                indice = self.items.index(item)
                for i in self.items[::-1][indice:]:
                    min_x += i.peso
                        
                max_x = self.capacidad
                for i in self.items[::-1][:indice]:
                    max_x -= i.peso
            else:
                min_x = 0
                max_x = self.capacidad
                        
            e = Etapa(min_x, max_x)
            self.etapas.append(e)
            
        self.etapas.reverse()
        for i in range(len(self.etapas)):
            self.etapas[i].set_sig_min(0) if i == 0 else self.etapas[i].set_sig_min(self.etapas[i-1].min_x)
            self.etapas[i].set_item(self.items[i])
        self.items.reverse()
    
    def print_etapas(self):
        for e in self.etapas:
            print(e)
            
    def generar_tablas(self):
        for e in self.etapas:
            e.generar_tabla()
            
    def resolver(self):
        self.generar_tablas()
        for i in range(len(self.etapas)):
            print('destinos: ', self.etapas[i].get_destinos())
            if i != 0:
                self.etapas[i].transicion(self.etapas[i-1].get_fun_max())
            print(self.etapas[i].get_destino_op())
            
    def print_solucion(self):
        self.etapas.reverse()
        aux = self.capacidad
        for i in range(len(self.etapas)):
            if i == 0:
                des = self.etapas[i].get_destino_sol(aux)
            else:
                des = self.etapas[i].get_destino_sol(aux)
            aux -= des
            print('destino: ', des)
        self.etapas.reverse()
            
                
    def print_matrices(self):
        print(e.matriz for e in self.etapas)