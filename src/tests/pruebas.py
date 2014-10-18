'''
Created on 18/10/2014

@author: jorge
'''
import unittest
import main
from grafo.grafo import masPopular

def printCamino (red,nodoOrigen,camino):
    for nodoId in camino:
        print "De:"+nodoOrigen.getLabel()+" hacia: "+red.getNodo(nodoId).getLabel()
        for vert in camino[nodoId]:
            print vert.getLabel()+" -> ",
        print red.getNodo(nodoId).getLabel()
        print ""

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testMasPopular(self):
        red = main.cargarRedDesdeArchivo("amigosPrueba1.gdf")
        maspopular = masPopular(red)
        self.assertEqual(maspopular.getId(),"1" ,maspopular.getLabel())
    
    def testMasInfluyente(self):
        red = main.cargarRedDesdeArchivo("amigosPrueba1.gdf")
        nodo = red.getNodo("1")
        camino = red.dijkstra(nodo)
        printCamino(red, nodo, camino)
    
    def testSujerirAmigo(self):
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testMasPopular']
    unittest.main()