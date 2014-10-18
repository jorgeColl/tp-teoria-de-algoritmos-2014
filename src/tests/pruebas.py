'''
Created on 18/10/2014

@author: jorge
'''
import unittest
import main
from grafo.grafo import masPopular


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testMasPopular(self):
        red = main.cargarRedDesdeArchivo("amigosPrueba1.gdf")
        maspopular = masPopular(red)
        self.assertEqual(maspopular.get_id(),"1" ,maspopular.getLabel())
    
    def testMasInfluyente(self):
        pass
    
    def testSujerirAmigo(self):
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testMasPopular']
    unittest.main()