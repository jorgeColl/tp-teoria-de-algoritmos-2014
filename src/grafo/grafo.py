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
		# cantidad de veces que pasan por el nodo
		self.cantVecesUsado = {}
		self.cantTotalVecesUsado = 0
		self.padres = []
		self.layer = -1
		self.indice = 0

	def __str__(self):
		result = "id: " + self.id_nodo +" - Label: "+self.label+" - Visitado: "+str(self.visitado)+" - cant amigos: "+str(len(self.aristas_ad))+"\n"
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
		self.cantCaminos = {}
		self.cc={}
		#DEBUG
		self.cantTotalCaminosMinimos=0
		self.cantTotalCaminosPasantesEn = {}
		
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
	
	"""	inicializa todos los nodos del grafo como no visitados """
	def inicializar_en_0(self):	
		for nodo in self.dicc_nodos.itervalues():
			nodo.visitado = False
			nodo.distanciaAcumulada = float("inf")
			nodo.cantTotalVecesUsado = 0
			nodo.padres = []
			self.cantCaminos[nodo] = 1
			for v in self.dicc_nodos.itervalues():
				nodo.cantVecesUsado[v] = 0.0
	
	"""###############################################################"""
	"""se va a llamar a todas estas funciones por cada vertice, las separe para testearlas por separado """
	def BFS(self, s):
		self.inicializar_en_0()
		s.layer = 0;
		s.visitado = True
		cola = []
		cola.append(s)
		supuestaCola = []
		while len(cola) != 0:
			v = cola.pop(0)
			for arista in v.aristas_ad:
				vecino = arista.destino
				if vecino.visitado == False:
					vecino.visitado = True
					vecino.layer = v.layer + 1
					cola.append(vecino)
					supuestaCola.append(vecino)
		return supuestaCola
	
	def padres(self):
		for v in self.dicc_nodos.itervalues():
				self.cantCaminos[v]=0
		
		for v in self.dicc_nodos.itervalues():
			for arista in v.aristas_ad:
				vecino = arista.destino
				if vecino.layer == v.layer + 1:
					vecino.padres.append(v)
					self.cantCaminos[vecino]+=1
		for v in self.dicc_nodos.itervalues():
				self.cantTotalCaminosMinimos+=self.cantCaminos[v]
	
	def sumPadre(self, colaOrdenada):
		colaOrdenada.reverse()
		for nodo in colaOrdenada:
			if(nodo.layer > 1):
				for padre in nodo.padres:
					#cantidad de veces usado para llegar al nodo "nodo"
					padre.cantVecesUsado[nodo] += nodo.cantTotalVecesUsado + 1.0
					padre.cantTotalVecesUsado += nodo.cantTotalVecesUsado + 1.0
	
	def procesarIndice(self):
		for v in self.dicc_nodos.itervalues():
			for w in self.dicc_nodos.itervalues():
				if(self.cantCaminos[w]!=0):
					v.indice += (v.cantVecesUsado[w] / self.cantCaminos[w])
		
		"""for r in self.dicc_nodos.values():
			print r.getLabel()+" :> ",
			for w in self.dicc_nodos.itervalues():
				print w.getLabel()+" :"+str(r.cantVecesUsado[w])+"  ",
			print""
		"""
	""" este metodo lleva a cabo todo el proceso de calculo del indice para cada vertice
	se busco separar el proceso en metodos pequenios cada uno de orden O(E+V), facilitando asi el testing"""
	def calcularTodosLosIndices(self):
		#DEBUG
		for w in self.dicc_nodos.itervalues():
			self.cantTotalCaminosPasantesEn[w]=0
		
		for v in self.dicc_nodos.itervalues():
			cola = self.BFS(v)
			self.padres()
			self.sumPadre(cola)
			self.procesarIndice()
			#DEBUG
			for w in self.dicc_nodos.itervalues():
				self.cantTotalCaminosPasantesEn[w]+=w.cantTotalVecesUsado
		#DEBUG
		for w in self.dicc_nodos.itervalues():
			print w.getLabel()+" caminos : "+str(self.cantTotalCaminosPasantesEn[w])
		return self.dicc_nodos.values()
	
	"""###############################################################"""
	
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

def ordenarPorLayer(nodo1, nodo2):
	if len(nodo1.layer) < len(nodo2.layer):
		return 1
	elif len(nodo1.layer) == len(nodo2.layer):
		return 0
	else:
		return -1

def comp(nodo1, nodo2):
	if len(nodo1.aristas_ad) < len(nodo2.aristas_ad):
		return 1
	elif len(nodo1.aristas_ad) == len(nodo2.aristas_ad):
		return 0
	else:
		return -1

""" devuelve el nodo que tiene mas conecciones con los otros nodos dentro del grafo"""
def masPopular(grafo):
	l = grafo.dicc_nodos.values()
	l.sort(comp)
	return l
	
""" devuelve el nodo que tiene mas caminos minimos que pasan por el que el resto"""
def masInfluyente(grafo):	
	lista = grafo.calcularTodosLosIndices()
	nodoMasInfluyente=Nodo("nadie","nadie")
	for nodo in lista:
		#DEBUG
		print nodo.getLabel()+": "+str(nodo.indice)
		
		if(nodoMasInfluyente.indice < nodo.indice):
			nodoMasInfluyente = nodo
	return nodoMasInfluyente

def recomendaciones(grafo):
	return grafo.vecinosRecomendados()
