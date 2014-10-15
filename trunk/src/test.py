#!/usr/bin/env python
from gdflib import GdfEntries, Node
entities = GdfEntries()
entities.add_node(Node(name='node1', label='This is the first node'))
entities.add_node(Node(name='node2', label='This is the second node'))
entities.link('node1', 'node2')
print entities.dumps()
