#!usr/bin/env python
#encoding:windows-1251
import heapq

class Nodo (object):
	def __init__(self, id_nodo, label):
		
		self.id_nodo = id_nodo
		self.label = label
		#TODO ordenar por destino
		self.aristas_ad = []
		self.distanciaAcumulada = float("inf")
		self.visitado = False
		self.restringido = False
		#cantidad de veces que pasan por el nodo
		self.cantVecesUsado = 0

	def __str__(self):
		result = "id: " + self.id_nodo +" - Label: "+self.label+"- Visitado: "+str(self.visitado)+"\n"
		result += "Aristas: "
		for arista in self.aristas_ad:
			result += str(arista) + " - "
		return result

	def __hash__(self):
		return self.id_nodo.__hash__()
	
	def getId(self):
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
	
	""" se utiliza el cmp para el heap """
	def __cmp__(self, arista2):
		
		if (self.peso > arista2.peso):
			return 1
			
		if (self.peso < arista2.peso):
			return -1
		else:
			return 0
	
	def	getPeso(self):
		return self.peso

	#Este debería ser el cmp?
	def igual(self, other):
		return (self.origen == other.origen and self.destino == other.destino)

class Grafo (object):
	
	def __init__(self):
		self.no_dirigido = True
		""" diccionario que guarda a todos los nodos que contenga el
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
		self.dicc_nodos[nodo.getId()] = nodo
		
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
		return Arista(None, None)
	
	"""	inicializa todos los nodos del grafo como no visitados """
	def inicializar_en_0(self):	
		for nodo in self.dicc_nodos.itervalues():
			nodo.visitado = False
			nodo.distanciaAcumulada = float("inf")
			nodo.cantVecesUsado = 0
	
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
		"""pone todos como no visitados y distancia en infinito"""
		self.inicializar_en_0()
		camino = {}
		camino[nodo.getId()]=list()
		nodo.distanciaAcumulada = 0
		lista = list()
		lista.append(nodo)
		
		while len(lista)>0 :
			vertice = lista.pop(0)
			#print "vertice:"+vertice.getLabel()
			vertice.visitado = True
			for arista in vertice.getVecinos():
				#print "destino:"+arista.destino.getLabel()
				if ( arista.destino.visitado == False ):
					distanciaVecinoOrigenDesdeVertice = vertice.distanciaAcumulada + arista.getPeso()
					distanciaVecinoOrigenDesdeVecino = arista.destino.distanciaAcumulada
					if distanciaVecinoOrigenDesdeVertice < distanciaVecinoOrigenDesdeVecino:
						arista.destino.distanciaAcumulada = distanciaVecinoOrigenDesdeVertice
						"""print "camino de vertice: ",
						for vert in camino[vertice.getId()]:
							print vert.getLabel()+" -> ",
						print ""
						print "camino anterior: ",
						if(camino.has_key(arista.destino.getId())):
							for vert in camino[arista.destino.getId()]:
								print vert.getLabel()+" -> ",
							print ""
						else:
							print "no habia camino"
						"""
						camino[arista.destino.getId()] = list(camino[vertice.getId()])
						camino[arista.destino.getId()].append (vertice)
						"""
						print"camino queda: ",
						for vert in camino[arista.destino.getId()]:
							print vert.getLabel()+" -> ",
						print ""
						"""
					lista.append(arista.destino)
		return camino

	#Esto es O(n) en memoria y O(n . A2) en cpu?
	def vecinosRecomendados(self):
		todos = list(self.dicc_nodos.values())
		#Esta matriz tiene en x la persona a quién se le va a recomendar, y en Y
		#un contador para ver quién conviene recomendar
		vectRecomendaciones = []
		for nodoRecomend in todos:
			recomendacion = self.recomendarVecino(nodoRecomend)
			tuplaAux = (nodoRecomend.label, recomendacion[0].label, recomendacion[1])
			vectRecomendaciones.append(tuplaAux)
		return vectRecomendaciones
			
	def recomendarVecino(self, nodo):
		contadoresRecomend = {}
		amigos = nodo.aristas_ad
		contadoresRecomend[nodo] = 1
		for nodoAmigo in amigos:
			#Acá le sumo un contador para recomendar
			amigosRecomendados = nodoAmigo.destino.aristas_ad
			for amigoRec in amigosRecomendados:
				if amigoRec.destino in contadoresRecomend: #Si el amigo ya apareció
					contadoresRecomend[amigoRec.destino] += 1
				else:
					contadoresRecomend[amigoRec.destino] = 1
		#Una vez que están los contadores, filtro quien NO es amigo
		for nodoAmigo in amigos:
			try:
				del contadoresRecomend[nodoAmigo.destino]
			except KeyError:
				pass
		#Y me quito a mi mismo
		del contadoresRecomend[nodo]
		masRecomendado = (Nodo("Nadie", "Nadie"), 0)
		#Y ahora busco el que más amigos en común tiene
		for recomendacion in contadoresRecomend:
			contAux = contadoresRecomend[recomendacion]
			if contAux > masRecomendado[1]:
				masRecomendado = (recomendacion, contAux)
		return masRecomendado

""" devuelve el nodo que tiene mas conecciones con los otros nodos dentro del grafo"""
def masPopular(grafo):
	nodo_max = Nodo("nadie","nadie")
	for nodo in grafo.dicc_nodos.itervalues():
		if(len(nodo_max.getVecinos())<len(nodo.getVecinos())):
			nodo_max = nodo
	return nodo_max

""" devuelve el nodo que tiene mas caminos minimos que pasan por el que el resto"""
def masInfluyente(grafo):
	for nodo in grafo.dicc_nodos.itervalues():
		caminosMinimosDesdeNodo = grafo.dijkstra(nodo)
		for camino in caminosMinimosDesdeNodo.itervalues():
			#ACA ESTOY CONTANDO DE MAS AL PRIMERO
			for nodo in camino[1:]:
				nodo.cantVecesUsado+=1
	
	nodoMasInfluyente=Nodo("nadie","nadie")
	for nodo in grafo.dicc_nodos.itervalues():
		#print de debugeo para mostrar que la cantidad de caminos minimos difiere de 
		#los del mail
		print nodo.getLabel()+" : "+str(nodo.cantVecesUsado)
		if(nodoMasInfluyente.cantVecesUsado < nodo.cantVecesUsado):
			nodoMasInfluyente = nodo
	return nodoMasInfluyente

def recomendaciones(grafo):
	return grafo.vecinosRecomendados()
