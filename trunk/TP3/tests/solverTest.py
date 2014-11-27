'''
Created on 25/11/2014
@author: jorge y matias y andres
'''
import unittest
from dinamic.solver import Solver


class Test(unittest.TestCase):
    
    """ funcion auxiliar de prueba comprueba que la matriz de valores y la solucion final sean iguales """
    def aux(self, tareasOriginales, matrixValoresOptimosEsperada, solucionEsperada):
        if(matrixValoresOptimosEsperada != None):
            """ compruebo la correcta creacion de la matrix de valores """
            solv1 = Solver(tareasOriginales)
            solv1.getMatrixValues()
            matrixValoresOptimosObtenida = solv1.Matrix
            self.assertEqual(matrixValoresOptimosEsperada, matrixValoresOptimosObtenida)
        
        """ compruebo si la solucion de tareas a ejecutar son correctas """
        solv2 = Solver(tareasOriginales)
        solucionObtenida = solv2.solve()
        self.assertEqual(solucionEsperada, solucionObtenida)
        
    def testBasicoConSuperposicionConstructiva(self):
        """ Nota: aunque las tareas se superpongan igualmente las dos son parte de la solucione """
        """ recordar que formato es t, b, v """
        tareasOriginales = [[2, 3, 4], [5, 6, 7]]
        matrixValoresOptimosEsperada = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 3, 3, 3, 3, 3, 3], [0, 0, 3, 3, 3, 6, 6, 9]]
        solucionEsperada = [1, 2]
        
        self.aux(tareasOriginales, matrixValoresOptimosEsperada, solucionEsperada)
    
    def testBasicoConSuperposicionDestructiva(self):
        """ Nota: las tareas se superponen y SOLO UNA forma parte de la solucione """
        """ recordar que formato es t, b, v """
        tareasOriginales = [[2, 3, 4], [6, 6, 7]]
        matrixValoresOptimosEsperada = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 3, 3, 3, 3, 3, 3], [0, 0, 3, 3, 3, 3, 6, 6]]
        solucionEsperada = [2]
        
        self.aux(tareasOriginales, matrixValoresOptimosEsperada, solucionEsperada)
    
    def test3TareasTarea2EsEliminadaDeLaSolucion(self):
        """ recordar que formato es t, b, v """
        tareasOriginales = [[2, 2, 3], [3, 1, 6], [6, 2, 10]]
        matrixValoresOptimosEsperada = None
        solucionEsperada = [1, 3]
        self.aux(tareasOriginales, matrixValoresOptimosEsperada, solucionEsperada)
    
    def test3TareasTarea3EmpiezaPrimero(self):
        """ recordar que formato es t, b, v """
        tareasOriginales = [[2, 88, 3], [3, 1, 6], [1, 2, 2]]
        matrixValoresOptimosEsperada = None
        solucionEsperada = [3, 1, 2]
        self.aux(tareasOriginales, matrixValoresOptimosEsperada, solucionEsperada)
    
    def test3TareasTarea3EsEliminadaDeLaSolucion(self):
        """ recordar que formato es t, b, v """
        tareasOriginales = [[2, 88, 3], [3, 3, 6], [2, 2, 2]]
        matrixValoresOptimosEsperada = None
        solucionEsperada = [1, 2]
        self.aux(tareasOriginales, matrixValoresOptimosEsperada, solucionEsperada)
    
    def test4Tareas(self):
        """ recordar que formato es t, b, v """
        tareasOriginales = [[1, 88, 2], [1, 77, 2], [4, 99, 11], [1, 44, 2]]
        matrixValoresOptimosEsperada = None
        solucionEsperada = [1, 2, 3]
        self.aux(tareasOriginales, matrixValoresOptimosEsperada, solucionEsperada)
    
    def test6Tareas(self):
        """ recordar que formato es t, b, v """
        tareasOriginales = [[1, 88, 2], [1, 77, 2], [4, 99, 11], [1, 44, 2], [7, 200, 24], [77, 999, 78]]
        matrixValoresOptimosEsperada = None
        solucionEsperada = [1, 6]
        self.aux(tareasOriginales, matrixValoresOptimosEsperada, solucionEsperada)
    
    def testNTareas(self):
        """ recordar que formato es t, b, v """
        """ notese que al aumentar el v y t del ultimo item a un numero grande el test empieza a demorar """
        tareasOriginales = [[1, 77, 2], [5, 200, 5], [1, 100, 1], [1, 100, 2] , [9999,1,9999]]
        matrixValoresOptimosEsperada = None
        solucionEsperada = [3, 4]
        self.aux(tareasOriginales, matrixValoresOptimosEsperada, solucionEsperada)
    
    def testNNTareas(self):
        """ recordar que formato es t, b, v """
        tareasOriginales = [[1, 77, 2], [5, 200, 5], [1, 100, 1], [1, 100, 2], [1, 100, 15], [1, 100, 16], [1, 100, 17], [1, 100, 18], [1, 100, 19]]
        matrixValoresOptimosEsperada = None
        solucionEsperada = [3, 4, 5, 6, 7, 8, 9]
        self.aux(tareasOriginales, matrixValoresOptimosEsperada, solucionEsperada)
    
if __name__ == "__main__":
    unittest.main()
