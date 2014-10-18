'''
Created on 18/10/2014

@author: jorge
'''
import unittest
import main
from grafo.grafo import masPopular, masInfluyente

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testMasPopular(self):
        red = main.cargarRedDesdeArchivo("amigosPrueba1.gdf")
        maspopular = masPopular(red)
        self.assertEqual(maspopular.getId(),"5" ,maspopular.getLabel())
    
    def testMasInfluyente1(self):
        red = main.cargarRedDesdeArchivo("amigosPrueba2.gdf")
        nodoMasInfluyente = masInfluyente(red)
        self.assertEqual(nodoMasInfluyente.getLabel(), "JUAN", "no coinciden los mas inlfuyentes")
    
    def testMasInfluyente2(self):
        red = main.cargarRedDesdeArchivo("amigosPrueba3.gdf")
        nodoMasInfluyente = masInfluyente(red)
        self.assertEqual(nodoMasInfluyente.getLabel(), "LUIS", "no coinciden los mas inlfuyentes")
        
    def testMasInfluyente3(self):
        red = main.cargarRedDesdeArchivo("amigosPrueba1.gdf")
        nodoMasInfluyente = masInfluyente(red)
        #TODAVIA TENGO QUE HACER LA CUENTA DE SI ESTA BIEN EL RESULTADO
        print nodoMasInfluyente
                
    
    def testSujerirAmigo(self):
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testMasPopular']
    unittest.main()