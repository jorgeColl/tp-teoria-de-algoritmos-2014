#!usr/bin/env python
#encoding:windows-1251
import heapq
from dns.rdatatype import NULL

class Nodo (object):
	def __init__(self, id_nodo, label):
		
		self.id_nodo = id_nodo
		self.label = label
		#TODO ordenar por destino
		self.aristas_ad = []
		self.distanciaAcumulada = float("inf")
		##self.distanciaAcumulada = 999.0
		self.visitado = False

	def __str__(self):
		result = "id: " + self.id_nodo +" - Label: "+self.label+"- Visitado: "+str(self.visitado)+"\n"
		result += "Aristas: "
		for arista in self.aristas_ad:
			result += str(arista) + " - "
		return result
	
	def get_id(self):
		return self.id_nodo
	
	def getLabel(self):
		return self.label
	
	def getVecinos(self):
		return self.aristas_ad
	
class Arista (object):
	def __init__(self, origen, destino):
		
		""" origen y destino son dos variables de la clase nodo """
		"""TODO intentar no usar origen"""
		self.origen = origen
		self.destino = destino
		self.peso = 1.0
		
	def __str__(self):
		return "[origen:"+ str(self.origen.getLabel()) +" destino:"+str(self.destino.getLabel())+" ]"
	
	""" se utilizará el cmp para el heap """
	def __cmp__(self, arista2):
		
		if (self.peso > arista2.peso):
			return 1
			
		if (self.peso < arista2.peso):
			return -1
		else:
			return 0
	
	def	getPeso(self):
		return self.peso
	

class Grafo (object):
	
	def __init__(self):
		self.no_dirigido = True
		""" diccionario que guardará a todos los nodos que contenga el
		grafo """
		self.dicc_nodos = {}	
		
		self.dicc_cam_min = {}
	def __str__(self):
		string =""
		for nodo in self.dicc_nodos.itervalues():
			string += str(nodo)
			string += '\n'
		return string
	""" recive la instancia del nodo y lo agrega a los nodos que 
	contiene el grafo """
	def ingresar_nodo(self, nodo):
		self.dicc_nodos[nodo.get_id()] = nodo
		
	def getNodo(self,nodo_id):
		return self.dicc_nodos[nodo_id]
	
	"""crea una buscarArista y la mete en su correspondiente nodo
	pre: los nodos tiene que estar creados"""
	def ingresar_arista(self, id_origen, id_destino):
		
		nodo_destino = self.dicc_nodos[id_destino]
		nodo_origen = self.dicc_nodos[id_origen]
		
		arista = Arista(nodo_origen, nodo_destino)
		nodo_origen.aristas_ad.append(arista)
		if(self.no_dirigido):
			arista2 = Arista(nodo_destino, nodo_origen)
			nodo_destino.aristas_ad.append(arista2)
				
	
	""" carga el peso en una buscarArista previamente creada """
	def cargar_peso_arista(self, id_origen, id_destino, peso):
		#TODO BUSQUEDA BINARIA
		for ar in self.dicc_nodos[id_origen].aristas_ad:
			if ar.destino.id_nodo == id_destino:
				ar.peso = int(peso)
				break
				
	""" dado un id_origen y un id_destino se busca y devuelve la buscarArista
	que tenga origen en id_origen y destino en id_destino
	En caso de que la arista NO exista, se devolvera una con peso infinito """
	def buscarArista(self, id_origen, id_destino):
		nodo = self.dicc_nodos[id_origen]
		#TODO busqueda binaria->hay que ordenar aristas por destino
		for arista in nodo.aristas_ad:
			if arista.destino.id_nodo == id_destino:
				return arista
		return Arista(NULL,NULL)
	
	"""	inicializa todos los nodos del grafo como no visitados """
	def inicializar_en_0(self):	
		for id_nodo in self.dicc_nodos:
			self.dicc_nodos[id_nodo].visitado = False
			self.dicc_nodos[id_nodo].distanciaAcumulada = float("inf")
	
	def prim(self, id_origen, peso_max):
		""" devuelve una lista de aristas """	
		heap_aristas = []
		solucion = []
		self.inicializar_en_0()
		
		nodo_inicial = self.dicc_nodos[id_origen]
		nodo_inicial.visitado = True
		
		for arista in nodo_inicial.aristas_ad:
			if arista.peso < peso_max:
				heapq.heappush(heap_aristas, arista)
		
		while len(heap_aristas) > 0 :
			arista = heapq.heappop(heap_aristas)
			
			if arista.destino.visitado == False:
				
				arista.destino.visitado = True
				solucion.append(arista)
				
				for arista2 in arista.destino.aristas_ad :
					if arista2.peso < peso_max:
						heapq.heappush(heap_aristas, arista2)
	
		return solucion
	""" determina el camino mas corto dado un vertice origen 
	al resto de vertices en un grafo con pesos en cada arista."""
	def dijkstra(self,nodo):
		"""pone todos como no visitados"""
		self.inicializar_en_0()
		camino = {}
		camino[nodo]=list()
		camino[nodo].append(nodo)
		nodo.distanciaAcumulada = 0
		lista = list()
		lista.append(nodo)
		while len(lista)>0 :
			vertice = lista.pop(0)
			#print vertice
			vertice.visitado = True
			for arista in vertice.getVecinos():
				#print arista.destino
				if ( arista.destino.visitado == False ):
					distanciaVecinoOrigenDesdeVertice = vertice.distanciaAcumulada + arista.getPeso()
					distanciaVecinoOrigenDesdeVecino = arista.destino.distanciaAcumulada
					if distanciaVecinoOrigenDesdeVertice < distanciaVecinoOrigenDesdeVecino:
						arista.destino.distanciaAcumulada = distanciaVecinoOrigenDesdeVertice
						camino[arista.destino] = camino[vertice]
						camino[arista.destino].append (vertice)
					#print "se agrega a: "+str(arista.destino.getLabel())
					lista.append(arista.destino)
		return camino
			

def floyd (grafo):
	distancia = {}
	camino = {}
	
	for id1 in grafo.dicc_nodos :
		distancia[id1] = {}
		camino[id1] = {}
		
		for id2 in grafo.dicc_nodos:
			arista = grafo.buscarArista(id1,id2)
			if arista.getPeso() <= float("inf"):
				distancia[id1][id2] = arista.getPeso()
				camino[id1][id2] = [id1]
			else:
				distancia[id1][id2] = float("inf")
				camino[id1][id2] = []
				
		distancia[id1][id1] = 0
		

	for A in grafo.dicc_nodos:
		for B in grafo.dicc_nodos:
			for C in grafo.dicc_nodos:
				if distancia[B][C] > distancia[B][A] + distancia[A][C]:
					distancia[B][C] = distancia[B][A] + distancia[A][C]
					camino[B][C] = camino[B][A] + camino[A][C] 
					
	return distancia, camino


""" devuelve el nodo que tiene mas conecciones con los otros nodos dentro del grafo"""
def masPopular(grafo):
	nodo_max = Nodo("nadie","nadie")
	for nodo in grafo.dicc_nodos.itervalues():
		if(len(nodo_max.getVecinos())<len(nodo.getVecinos())):
			nodo_max = nodo
	return nodo_max

""" devuelve el nodo que tiene mas caminos minimos que pasan por el que el resto"""
def masInfluyente(grafo):
	pass
		
		
	
