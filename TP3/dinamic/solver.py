'''
Created on 23/11/2014

@author: jorge
'''

class Solver(object):


    def __init__(self, tareas):
        self.listaTareas = tareas
        self.listaTareas.sort(self.comp)
        self.Matrix = [] 
        
        self.maxD = self.listaTareas[len(self.listaTareas) - 1][2]
        self.tareaN = len(self.listaTareas)
        for x in range (0, self.tareaN + 1):
            aux = [0] * (self.maxD + 1)
            self.Matrix.append(aux)
    
    """funcion auxiliar usada para ordenar las tuplas por orden de v"""
    def comp(self, e1, e2):
        if (e1[2] == e2[2]):
            return 0
        if(e1 > e2):
            return 1
        return -1
    
    def getMatrixValues(self):
        """Orden: O(a*v)"""
        for a in range(1, self.tareaN + 1):
            for v in range(0, self.maxD + 1):
                t = self.listaTareas[a - 1][0]
                b = self.listaTareas[a - 1][1]
                
                if (self.Matrix[a - 1][v] > self.Matrix[a - 1][v - t] + b or t > v):
                    """no es tarea optima"""
                    self.Matrix[a][v] = self.Matrix[a - 1][v]
                else:
                    """es tarea optima"""
                    self.Matrix[a][v] = self.Matrix[a - 1][v - t] + b
        #print "marix"
        #print self.Matrix
    
    def __getPathSolution(self):
        """ como se puede observar se iterara en el while la cantidad de tareas que existan O(a)"""
        solucion = []
        a = len(self.listaTareas)
        v = self.maxD
        
        while (self.Matrix[a][v] !=0 and a != 0 and v != 0 ):
            t = self.listaTareas[a - 1][0]
            b = self.listaTareas[a - 1][1]
            
            sinTarea = self.Matrix[a - 1][v]
            conTarea = self.Matrix[a - 1][v - t] + b
            
            if (sinTarea > conTarea):
                """no es tarea optima"""
                a -= 1
            else:
                """es tarea optima"""
                solucion.append(a)
                a -= 1
                v = v - t
        solucion.reverse()
        return solucion
    
    """ orden O(a*v + a)"""
    def solve(self):
        self.getMatrixValues()
        return self.__getPathSolution()
       
        
        
        
        
