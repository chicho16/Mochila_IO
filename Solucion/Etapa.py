import numpy as np

class Etapa:
    def __init__(self, min_x, max_x):
        self.min_x = min_x
        self.max_x = max_x
        self.item = None
        self.sig_min = None
        self.matriz = None

    def __str__(self):
        return f"\n{self.item}\nmin x: {self.min_x}\nmax x: {self.max_x}\nsig min: {self.sig_min}"
    
    def set_item(self, item):
        self.item = item
    
    def set_sig_min(self, sig_min):
        self.sig_min = sig_min
    
    def cantidad_columnas(self):
        col = 1
        while self.item.peso*col <= self.max_x-self.sig_min:
            col += 1
        return col
    
    def generar_destinos(self):
        if self.min_x == self.max_x and self.sig_min == 0:
            return np.arange(0, self.cantidad_columnas()) * self.item.peso
        return np.arange(0 if self.min_x == 0 else 1, self.cantidad_columnas()) * self.item.peso
    
    def generar_origenes(self):
        aux = [[-1]]
        for i in list(range(self.min_x, self.max_x+1)):
            aux.append([i])
        return np.array(aux)
    
    def generar_utilidades(self):
        if self.min_x == self.max_x and self.sig_min == 0:
            return np.arange(0, self.cantidad_columnas()) * self.item.beneficio
        return np.arange(0 if self.min_x == 0 else 1, self.cantidad_columnas()) * self.item.beneficio
        
    def generar_tabla(self):
        origenes = self.generar_origenes()
        destinos = self.generar_destinos()
        
        dif = self.max_x-self.min_x
        if self.min_x == 0 or (self.min_x == self.max_x and self.sig_min == 0):
            self.matriz = np.zeros((dif+1, self.cantidad_columnas()))
        else:
            self.matriz = np.zeros((dif+1, self.cantidad_columnas()-1))
        
        self.utilidades = self.generar_utilidades()
        
        self.matriz = np.vstack((destinos, self.matriz))
        self.matriz = np.hstack((origenes, self.matriz))
        
        self.inicializar_celdas()
        
    def get_origenes(self):
        return self.matriz[1:, 0].T
        
    def inicializar_celdas(self):
        for i in range(1, len(self.matriz[:, 0])):
            for j in range(1, len(self.matriz[0, :])):
                self.matriz[i, j] = self.utilidades[j-1] if self.matriz[i, 0] - self.matriz[0, j] >= self.sig_min else -1
                    
    def transicion(self, prev_fun_max):
        indice = 0
        if self.min_x == self.max_x:
                prev_fun_max = prev_fun_max[::-1]
        for j in range(1, len(self.matriz[0, :])):
            if self.min_x != self.max_x:
                indice = 0
            for i in range(1, len(self.matriz[:, 0])):
                if self.matriz[i, j] != -1:
                    self.matriz[i, j] += prev_fun_max[indice]
                    indice += self.item.peso if self.max_x == self.min_x else 1
    
    def get_fun_max(self):
        fun_max = [max(fila) for fila in self.matriz[1:, 1:]]
        fun_max = np.array(fun_max)
        return fun_max
    
    def genera_destinos_optimos(self):
        fun_max = self.get_fun_max()
        maximos = []
        destinos_op = []
        i = 0
        for fila in self.matriz[1:, 1:]:
            maximo = np.where(fila == fun_max[i])[0]
            maximos.append(maximo)
            destino = []
            for m in maximo:
                destino.append(self.matriz[0, m+1])
            destinos_op.append(destino)
            i+=1
        self.destinos_op = destinos_op
        
    def get_destino_op(self):
        return self.destinos_op
    
    def get_destino_sol(self, prev_residuo):
        indice = np.where(self.get_origenes() == prev_residuo)[0]
        return self.destinos_op[indice[0]]