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
	nodeRead = (len(row) == 5)
	nodeDictionary[row[0]] = row[1]
print nodeDictionary

graphFile.close()
