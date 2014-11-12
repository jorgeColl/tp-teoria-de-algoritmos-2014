'''
Created on 11/11/2014

@author: jorge
'''
import unittest
from perfil import Perfil
from _random import Random
from numpy.oldnumeric.random_array import random_integers

class Test(unittest.TestCase):
    TESTALL = True
    
    def testPerfilCasoBase(self):
        """ cuando dos perfiles no se interdectan """
        if self.TESTALL:
            perfilOriginal = [1,7,3,0,4,2,6,0]
            resultadoEsperado = perfilOriginal[0:-1]
            perfil = Perfil.Perfil()
            resultado = perfil.calcularPerfil(perfilOriginal,0)
            self.assertEqual(resultadoEsperado, resultado)        
    
    def testPerfilCasoBaseInvertido(self):
        if self.TESTALL:
            perfilOriginal = [4,2,6,0,1,7,3,0]
            resultadoEsperado = [1,7,3,0,4,2,6]
            perfil = Perfil.Perfil()
            resultado = perfil.calcularPerfil(perfilOriginal,0)
            self.assertEqual(resultadoEsperado, resultado)
        
    def testPerfilCasoInterseccionIgnorada(self):
        """
        ....................... h=7
        |      .....h=3       |
        |     |    |          |
        |     |    |          |
        0     1    2          5
        """
        if self.TESTALL:
            perfilOriginal = [0,7,5,0,1,3,2,0]
            resultadoEsperado = [0,7,5]
            perfil = Perfil.Perfil()
            resultado = perfil.calcularPerfil(perfilOriginal,0)
            self.assertEqual(resultadoEsperado, resultado)
        
    def testPerfilCasoInterseccionAscendente(self):
        """    .............................. h=9
              |                             |
        ......|................ h=7         |
        |     |               |             |    
        |     |               |             |       
        |     |               |             |         
        0     1               5             12             
        """
        if self.TESTALL:
            perfilOriginal = [0,7,5,0,1,9,12,0]
            resultadoEsperado = [0,7,1,9,12]
            perfil = Perfil.Perfil()
            resultado = perfil.calcularPerfil(perfilOriginal,0)
            self.assertEqual(resultadoEsperado, resultado)
    
    def testPerfilCasoInterseccionDescendente(self):
        """    .............................. h=9
              |                             |
              |                .............|.................. h=7
              |               |             |                 |
              |               |             |                 |
              |               |             |                 |
              1               3             5                 12
        """
        if self.TESTALL:
            perfilOriginal = [1,9,5,0,3,7,12,0]
            resultadoEsperado = [1,9,5,7,12]
            perfil = Perfil.Perfil()
            resultado = perfil.calcularPerfil(perfilOriginal,0)
            self.assertEqual(resultadoEsperado, resultado)
        
    def testPerfilCasoInterseccionNaveEspacial(self):
        """       ....................... h=9
                 |                      |
           ......|......................|.............. h=7
           |     |                      |             |
           |     |                      |             |
           |     |                      |             |
           1     3                      5             12
        """
        if self.TESTALL:
            perfilOriginal = [1,7,12,0,3,9,5,0]
            resultadoEsperado = [1,7,3,9,5,7,12]
            perfil = Perfil.Perfil()
            resultado = perfil.calcularPerfil(perfilOriginal,0)
            self.assertEqual(resultadoEsperado, resultado)
        
    def testPerfilCasoInterseccionesVarias(self):
        #se prueba el mismo conjunto introducido en distinto orden
        """       ....................... h=9    ................... h=10
                 |                      |       |                  |
           ......|......................|.......|....... h=7       |
           |     |                      |       |      |           |
           |     |                      |       |      |           |
           |     |                      |       |      |           |
           1     3                      5       8      12          17
        """
        if self.TESTALL:
            pe1 = [1, 7, 12, 0]
            pe2 = [3, 9, 5, 0]
            pe3 = [8, 10, 17, 0]
            combo1 = pe1 + pe2 + pe3
            combo2 = pe1 + pe3 + pe2
            combo3 = pe2 + pe1 + pe3
            combo4 = pe3 + pe2 + pe1
            combo5 = pe2 + pe3 + pe1
            combo6 = pe3 + pe2 + pe1
            listaCombos = []
            listaCombos.append(combo1)
            listaCombos.append(combo2)
            listaCombos.append(combo3)
            listaCombos.append(combo4)
            listaCombos.append(combo5)
            listaCombos.append(combo6)
            
            resultadoEsperado = [1, 7, 3, 9, 5, 7, 8, 10, 17]
            perfil = Perfil.Perfil()
            for perfilOriginal in listaCombos:
                resultado = perfil.calcularPerfil(perfilOriginal, 0)
                self.assertEqual(resultadoEsperado, resultado)
                
    
    def testEjemploTp(self):
        """ lo primero es para probar todas las combinaciones posibles en que me puede entrar
        la informacion, es decir cualquier orden"""
        azul = [0, 4, 5, 0]
        rojo = [1, 7, 4, 0]
        amarillo = [3, 6, 8, 0]
        negro = [6, 10, 10, 0]
        magenta = [7, 8, 12, 0]
        verde = [9, 11, 11, 0]
        perfiles = []
        perfiles.append(azul)
        perfiles.append(rojo)
        perfiles.append(amarillo)
        perfiles.append(negro)
        perfiles.append(magenta)
        perfiles.append(verde)
        perfil = Perfil.Perfil()
        resultadoEsperado = [0, 4, 1, 7, 4, 6, 6, 10, 9, 11, 11, 8, 12]
        for x in range(10000):
            inicial = random_integers(6, 0)
            inicial = inicial*4
            perfilOriginal = []
            for i in range (inicial, len(perfiles)+inicial, 1):
                perfilOriginal += perfiles[i%len(perfiles)]
                
            resultado = perfil.calcularPerfil(perfilOriginal, 0)
            self.assertEqual(resultadoEsperado, resultado)
    
    def testCargadoYejecucionDeEjercicioDePruebaTp(self):
        perfil = Perfil.Perfil.fromFile(self,"ejercicioTp.txt")
        resultadoEsperado = [0, 4, 1, 7, 4, 6, 6, 10, 9, 11, 11, 8, 12]
        resultado = perfil.calcularPerfil(perfil.perfilOriginal, 0)
        self.assertEqual(resultadoEsperado, resultado)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testperfil1']
    unittest.main()
