from Etapa import Etapa
from copy import deepcopy

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
    
    def generar_tablas(self):
        for e in self.etapas:
            e.generar_tabla()
        
    def resolver(self):
        self.generar_tablas()
        for i in range(len(self.etapas)):
            if i != 0:
                self.etapas[i].transicion(self.etapas[i-1].get_fun_max())
            self.etapas[i].genera_destinos_optimos()
            
        soluciones = self.get_conjunto_solucion()
        self.soluciones = self.normalizar_sol(soluciones)
                
    def get_conjunto_solucion(self):
        self.etapas.reverse()
        sol = self.etapas[0].get_destino_sol(self.capacidad)
        conjunto = self.trasponer(sol)
        for e in self.etapas[1:]:
            conj = []
            for camino in conjunto:
                des = e.get_destino_sol(self.capacidad - sum(camino))
                # decision = []
                for d in des:
                    cam = deepcopy(camino)
                    cam.append(d)
                    conj.append(cam)
                # conj.append(decision[0])
            conjunto = conj
        self.etapas.reverse()
        return conjunto
    
    def trasponer(self, sol):
        aux = []
        for s in sol:
            aux.append([s])
        return aux
    
    def get_utilidad_neta(self):
        return self.etapas[-1].get_fun_max()[0]
    
    def normalizar_sol(self, soluciones):
        for i in range(len(soluciones)):
            for j in range(len(soluciones[i])):
                soluciones[i][j] = int(soluciones[i][j] / self.items[j].peso)
        return soluciones
                
            
    def print_solucion(self):
        tablas = []
        for sol in self.soluciones:
            tabla = [(f'\nSolucion: {self.soluciones.index(sol)+1}'),('Item', 'Cantidad', 'Peso', 'Utilidad')]
            for indice in range(len(sol)):
                i = self.items[indice]
                tabla.append((i.nombre, sol[indice], i.peso*sol[indice], i.beneficio*sol[indice]))
            tabla.append(('Utilidad total = ', self.get_utilidad_neta()))
            tablas.append(tabla)
        self.tabla_sol = tablas
        print(self.tabla_sol)
        
    def print_etapas(self):
        for e in self.etapas:
            print(e)
            
    def print_matrices(self):
        print(e.matriz for e in self.etapas)
        
    def get_formulacion_problema(self):
        problema = [self.capacidad]
        for item in self.items:
            problema.append((item.nombre, item.peso, item.beneficio))
        return tuple(problema)
    
    def get_soluciones(self):
        soluciones = []
        for sol in self.soluciones:
            solucion = []
            for i in range(len(sol)):
                solucion.append((self.items[i].nombre, sol[i], self.items[i].peso * sol[i], self.items[i].beneficio * sol [i]))
            soluciones.append(tuple(solucion))
        return tuple(soluciones)
    
    def get_pesos_sol(self):
        pesos = []
        for solucion in self.get_soluciones():
            peso = 0
            for fila in solucion:
                peso += fila[2]
            pesos.append(peso)
        return tuple(pesos)