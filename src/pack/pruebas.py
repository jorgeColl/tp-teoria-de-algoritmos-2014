#!/usr/bin/env python
'''
Created on 14/10/2014


'''

import csv
import unittest
import grafo

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
        print red
            
        # print nodeDictionary
        
        graphFile.close()



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testHola']
    unittest.main()