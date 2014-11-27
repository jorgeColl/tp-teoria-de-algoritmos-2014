'''
Created on 23/11/2014
@author: jorge y matias y andres
'''

class Solver(object):


    def __init__(self, tareas):
        self.listaTareas = tareas
        
        # le pongo el nombre a la tarea
        for x in range(1, len(self.listaTareas) + 1):
            self.listaTareas[x - 1].append(x)
        
        # ordeno la lista de tareas por orden de deadline
        self.listaTareas.sort(self.comp)
        self.Matrix = [] 
        
        self.maxD = self.listaTareas[len(self.listaTareas) - 1][2]
        self.tareaN = len(self.listaTareas)
        
        # inicializo la matriz de valores vacia
        for x in range (0, self.tareaN + 1):
            aux = [0] * (self.maxD + 1)
            self.Matrix.append(aux)
    
    """funcion auxiliar usada para ordenar las tuplas por orden de v"""
    def comp(self, e1, e2):
        if (e1[2] == e2[2]):
            return 0
        if(e1[2] > e2[2]):
            return 1
        return -1
    
    """ genera la matriz de valores, esta tiene como informacion que valor optimo existe
    para un sub problema con vencimiento maximo d y tareas a """
    """Orden getMatrixValues: O(a*v)"""
    def getMatrixValues(self):
        for a in range(1, self.tareaN + 1):
            for v in range(0, self.listaTareas[a-1][2] + 1):
                t = self.listaTareas[a - 1][0]
                b = self.listaTareas[a - 1][1]
                
                
                if (self.Matrix[a - 1][v] > self.Matrix[a - 1][v - t] + b or t > v ):
                    """no es tarea optima"""
                    self.Matrix[a][v] = self.Matrix[a - 1][v]
                else:
                    """es tarea optima"""
                    self.Matrix[a][v] = self.Matrix[a - 1][v - t] + b
            
            for v in range(self.listaTareas[a-1][2]+1 ,self.maxD+1 ):
                self.Matrix[a][v] = self.Matrix[a][v-1]
               
    """ a partir de la matriz de valores obtiene las tareas correspondientes de la
    solucion optima """
    """ Orden __getPathSolution: O(a) """
    def __getPathSolution(self):
        solucionTuplas = []
        a = len(self.listaTareas)
        v = self.maxD
        
        while (self.Matrix[a][v] != 0 and a != 0 and v != 0):
            # while(self.Matrix[a][v] == self.Matrix[a][v-1]):
            #    v-=1
            t = self.listaTareas[a - 1][0]
            b = self.listaTareas[a - 1][1]
            
            sinTarea = self.Matrix[a - 1][v]
            conTarea = self.Matrix[a - 1][v - t] + b
            
            if (sinTarea >= conTarea or self.Matrix[a - 1][v] == self.Matrix[a][v]):
                """no es tarea optima"""
                a -= 1
            else:
                """es tarea optima"""
                solucionTuplas.append(self.listaTareas[a - 1])
                a -= 1
                v = v - t
                
        """ consigo los nombres de las tareas en su correspondiente orden """
        solucionTuplas.reverse()
        solucionTareas = []
        for tupla in solucionTuplas:
            solucionTareas.append(tupla[3])
            
        return solucionTareas
    
    """ orden solve:  O(a*v + a) 
        con a: cantidad de tareas
        con v: vencimiento maximo   """
    def solve(self):
        self.getMatrixValues()
        return self.__getPathSolution()
       
        
        
        
        
