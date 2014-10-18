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

"""
#!/usr/bin/env python
from gdflib import GdfEntries, Node
entities = GdfEntries()
entities.add_node(Node(name='node1', label='This is the first node'))
entities.add_node(Node(name='node2', label='This is the second node'))
entities.link('node1', 'node2')
print entities.dumps()
"""