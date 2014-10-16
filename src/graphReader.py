#!/usr/bin/env python
import csv

graphFile = open('matias-graph.gdf', 'rb')
graphReader = csv.reader(graphFile)

"""
* Armo diccionario de amigos
"""

nodeRead = True
nodeDictionary = {}

#Saco header
graphReader.next()

while nodeRead:
	row = graphReader.next()
	nodeDictionary[row[0]] = row[1]
	nodeRead = (len(row) == 5)
print nodeDictionary

graphFile.close()
