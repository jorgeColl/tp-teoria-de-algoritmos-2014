'''
Created on 25/11/2014

@author: jorge
'''
import unittest
from dinamic.solver import Solver


class Test(unittest.TestCase):
    
    """funcion auxiliar de prueba comprueba que la matriz de valores y la solucion final sean iguales"""
    def aux(self, tareasOriginales, matrixValoresOptimosEsperada, solucionEsperada):
        """compruebo la correcta creacion de la matrix de valores"""
        solv1 = Solver(tareasOriginales)
        solv1.getMatrixValues()
        matrixValoresOptimosObtenida = solv1.Matrix
        self.assertEqual(matrixValoresOptimosEsperada, matrixValoresOptimosObtenida)
        
        """compruebo si la solucion de tareas a ejecutar son correctas """
        solv2 = Solver(tareasOriginales)
        solucionObtenida = solv2.solve()
        self.assertEqual(solucionEsperada, solucionObtenida)
        
    def testBasicoConSuperposicionConstructiva(self):
        """Nota: aunque las tareas se superpongan igualmente las dos son parte de la solucione"""
        """recordar que formato es t, b, v """
        tareasOriginales = [[2, 3, 4], [5, 6, 7]]
        matrixValoresOptimosEsperada = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 3, 3, 3, 3, 3, 3], [0, 0, 3, 3, 3, 6, 6, 9]]
        solucionEsperada = [1, 2]
        
        self.aux(tareasOriginales, matrixValoresOptimosEsperada, solucionEsperada)
    
    def testBasicoConSuperposicionDestructiva(self):
        """Nota: las tareas se superponen y SOLO UNA forma parte de la solucione"""
        """recordar que formato es t, b, v """
        tareasOriginales = [[2, 3, 4], [6, 6, 7]]
        matrixValoresOptimosEsperada = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 3, 3, 3, 3, 3, 3], [0, 0, 3, 3, 3, 3, 6, 6]]
        solucionEsperada = [2]
        
        self.aux(tareasOriginales, matrixValoresOptimosEsperada, solucionEsperada)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testBasicoSinSuperposicion']
    unittest.main()
