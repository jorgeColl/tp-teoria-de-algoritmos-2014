#!/usr/bin/env python
'''
Created on 14/10/2014


'''

import csv
import unittest
import grafo
from grafo.grafo import masPopular

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testHola(self):
        graphFile = open('amigos.gdf', 'rb')
        graphReader = csv.reader(graphFile)
        
        """
        * Armo diccionario de amigos
        """
        nodeRead = True
        nodeDictionary = {}
        
        #Saco header
        graphReader.next()
        red = grafo.Grafo()
        
        while nodeRead:
            row = graphReader.next()
            nodeDictionary[row[0]] = row[1]
            nodeRead = (len(row) == 5)
            nodo = grafo.Nodo(row[0],row[1]) 
            red.ingresar_nodo(nodo)
        for row in graphReader:
            red.ingresar_arista(row[0], row[1])
        print red
        print "mas amigasooooooooo"
        amigazo = masPopular(red)
        print amigazo
            
        # print nodeDictionary
        
        graphFile.close()



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testHola']
    unittest.main()