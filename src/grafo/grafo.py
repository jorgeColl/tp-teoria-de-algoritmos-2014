#!usr/bin/env python
#encoding:windows-1251
import heapq
import os

class Nodo (object):
	def __init__(self, id_nodo, label):
		
		self.id_nodo = id_nodo
		self.label = label
		"""aristas adyacentes al nodo"""
		#TODO ordenar por destino
		self.aristas_ad = []
		
		"""atrubuto que se utiliza para la funcion prim"""
		self.visitado = False
	def __str__(self):
		return "id: " + self.id_nodo +" - Label: "+self.label
	
	def get_id(self):
		return self.id_nodo
	
class Arista (object):
	def __init__(self, origen, destino):
		
		""" origen y destino son dos variables de la clase nodo """
		"""TODO intentar no usar origen"""
		self.origen = origen
		
		self.destino = destino
		
		""" peso ponderado """
		self.peso = 1
		
		self.restringida = False
		
	def __str__(self):
		return "[origen:"+ str(self.origen.id_nodo) +" destino:"+str(self.destino.id_nodo)+" ]"
	
	""" se utilizará el cmp para el heap """
	def __cmp__(self, arista2):
		
		if (self.peso > arista2.peso):
			return 1
			
		if (self.peso < arista2.peso):
			return -1
		else:
			return 0
	
	def	get_peso(self):
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
			string += nodo.__str__()
			string += '\n'
			print nodo
		return string
	""" recive la instancia del nodo y lo agrega a los nodos que 
	contiene el grafo """
	def ingresar_nodo(self, nodo):
		self.dicc_nodos[nodo.get_id()] = nodo
		
	"""crea una arista y la mete en su correspondiente nodo
	pre: los nodos tiene que estar creados"""
	def ingresar_arista(self, id_origen, id_destino):
		
		nodo_destino = self.dicc_nodos[id_destino]
		nodo_origen = self.dicc_nodos[id_origen]
		
		arista = Arista(nodo_origen, nodo_destino)
		nodo_origen.aristas_ad.append(arista)
		if(self.no_dirigido):
			arista2 = Arista(nodo_origen, nodo_destino)
			nodo_destino.aristas_ad.append(arista2)
				
	
	""" carga el peso en una arista previamente creada """
	def cargar_peso_arista(self, id_origen, id_destino, peso):
		#TODO BUSQUEDA BINARIA
		for ar in self.dicc_nodos[id_origen].aristas_ad:
			if ar.destino.id_nodo == id_destino:
				ar.peso = int(peso)
				break
				
	""" dado un id_origen y un id_destino se busca y devuelve la arista
	que tenga origen en id_origen y destino en id_destino
	pre: arista buscada debe existir """
	def arista(self, id_origen, id_destino):
		nodo = self.dicc_nodos[id_origen]
		#TODO busqueda binaria->hay que ordenar aristas por destino
		for arista in nodo.aristas_ad:
			if arista.destino.id_nodo == id_destino:
				return arista
		
		
	""" dado un id_origen y un id_destino se busca y devuelve el peso de
	la arista que tenga origen en id_origen y destino en id_destino
	en caso de no encontrar la arista devuelve -1 """
	def arista_peso(self, id_origen, id_destino):
		arista =  self.arista(id_origen, id_destino)
		return arista.peso
		
	
	"""	inicializa todos los nodos del grafo como no visitados """
	def inicializar_en_0(self):	
		for id_nodo in self.dicc_nodos:
			self.dicc_nodos[id_nodo].visitado = False
	
	
	""" funcion utilizada para "ignorar" a los id recividos en la lista
	negra """ 
	def aplicar_restricciones_nodo(self, lista_negra):
		""" inicializa en False todas las restricciones por si ya hubo
		una ejecucion previa """
		for id_nodo in self.dicc_nodos:
			self.dicc_nodos[id_nodo].restringido = False
			
		"""si hay una lista de nodos restrinjidos , aplica las
		restricciones pertinentes"""
		if lista_negra != None :
			for id_nodo in lista_negra:
				self.dicc_nodos[id_nodo].restringido = True

	
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
			
			if arista.destino.visitado == False and arista.destino.restringido == False :
				
				arista.destino.visitado = True
				solucion.append(arista)
				
				for arista2 in arista.destino.aristas_ad :
					if arista2.peso < peso_max:
						heapq.heappush(heap_aristas, arista2)
	
		return solucion
		
	

def floyd (grafo, peso_max):

	distancia = {}
	camino = {}
	
	for id1 in grafo.dicc_nodos :
		distancia[id1] = {}
		camino[id1] = {}
		vecinos = grafo.vecinos_no_restringidos(id1)
		
		for id2 in grafo.dicc_nodos:
			if id2 in vecinos and grafo.arista_peso(id1, id2) <= peso_max:
				distancia[id1][id2] = grafo.arista_peso(id1, id2)
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
	
def leer_linea(archivo):
	linea = archivo.readline() 
	linea = linea.rstrip ("\n")
	linea = linea.split(" ")
	
	return linea

""" funcion que lee todas las lineas del archivo y las pone en una lista
con cada palabra de la linea formando tuplas """
def procesar_lineas_archivo(archivo):
	
	lineas_procesadas = []
	linea = leer_linea(archivo)
	while linea != [""] :
		
		lineas_procesadas.append(linea)
		linea = leer_linea(archivo)
	
	return lineas_procesadas

def cargar_agentes_en_grafo(lineas_procesadas, grafo):
	for linea in lineas_procesadas:
		grafo.ingresar_nodo(linea[0])

def cargar_aristas_en_grafo(lineas_procesadas, grafo, peso_columna):
	for linea in lineas_procesadas:
		grafo.ingresar_arista(linea[0], linea[1])
		#caso particular que se cargarán todos los pesos en 1
		if peso_columna == None:
			peso = 1
		else:
			#caso que se cargarán los pesos desde archivo
			peso = linea[peso_columna]
			
		grafo.cargar_peso_arista(linea[0], linea[1], peso)
		


""" funcion que se encarga de cargar todos los datos de los archivos al
grafo, los modos soportados son:
"agentes" que entonces se entenderá que se está trabajando con el 
formato del archivo1 y se cargarán los agentes(nodos) al grafo
"tiempo" se entenderá que se está trabajando con el formato del archivo2
y se cargarán al grafo las aristas , con el peso como el tiempo.
"confianza" se entenderá que se está trabajando con el formato del 
archivo2 y se cargarán al grafo las aristas , con el peso como el tiempo
"nodos" se entenderá que se está trabajando con el formato del archivo2
y se cargarán al grafo las aristas pero con TODAS las aristas con peso 1

pre: nombre_archivo tiene que ser valido y grafo fue creado
post: grafo contiene datos del archivo (segun modo, datos variarán)
"""
def cargar_datos(nombre_archivo, grafo, modo):
	archivo = open(nombre_archivo)
	
	lineas_procesadas = procesar_lineas_archivo(archivo)
	
	if modo == "agentes":
		cargar_agentes_en_grafo(lineas_procesadas, grafo)
	elif modo == "tiempo" :
		cargar_aristas_en_grafo(lineas_procesadas, grafo, 3)
	elif modo == "confianza":
		cargar_aristas_en_grafo(lineas_procesadas, grafo, 2)
	elif modo == "nodos":
		cargar_aristas_en_grafo(lineas_procesadas, grafo, None)
	archivo.close()


def tomar_opcion_menu():
	print "Que desea hacer?"
	print "'1' para buscar mas popular"
	print "'2' para buscar el amigo mas influyente"
	print "'3' para que te recomendemos un nuevo amigo "
	
	print "'0' Para salir"
	while True:
		try:
			opcion = raw_input('ingrese el numero de la opcion deseada:')
			opcion = int(opcion)
			if opcion > -1 and opcion < 6:
				break
		except:
			pass
	return opcion

""" informa al usuario si hay camino o no, en el caso de haber camino
usando el dicc_id_nombre pasa de los ids a los nombres de los agentes
y muestra el camino a recorrer """
def imprimir_camino(camino, dicc_id_nombre, id_destino):
	if camino == []:
		print "no se encontro camino posible entre los agentes"
	else:
		print "camino a seguir: "
		camino += [id_destino]
		for id in camino:
			print " -> ",dicc_id_nombre[id],
		print " "


""" pregunta el nombre del archivo y corrobora que exista este, en caso
de no existir se preguntará el nombre nuevamente """
def tomar_nombre_archivo ():
	while True:
		nombre_archivo = raw_input("ingrese nombre de archivo: ")
		if os.path.exists(nombre_archivo):
			return nombre_archivo


""" funcion auxiliar que sirve para las pruebas """
def debug_caminos_menos_nodos(dicc_camino_menos_nodos, dicc_id_nombre):
	
	for id1 in dicc_camino_menos_nodos:
		for id2 in dicc_camino_menos_nodos[id1]:
			
			agente_emisor = dicc_id_nombre[str(id1)]
			agente_receptor = dicc_id_nombre[str(id2)]
			
			print "agente_emisor: ", agente_emisor,",",
			print "agente_receptor: ",agente_receptor
			camino = dicc_camino_menos_nodos[id1][id2]
			print imprimir_camino(camino, dicc_id_nombre)
			
""" funcion que se encarga de llamar a prim que devolverá las aristas
que crean el arbol de tendido minimo y lo mustra en pantalla """
def arbol_tend_min(grafo_nodos, origen, dicc_id_nombre, peso_max):
	print "Arbol de tendido minimo"
	
	lista_aristas = grafo_nodos.prim(origen, peso_max)
	for arista in lista_aristas:
		agente_origen = dicc_id_nombre[arista.origen.id_nodo]
		agente_recept = dicc_id_nombre[arista.destino.id_nodo]
		
		print agente_origen,"->",agente_recept


def main():
	
	grafo = Grafo() #para mejor tiempo
	
	
	
	
	#distancia1, camino_minimo1 = floyd(grafo_confianza, peso_maximo)
	#distancia2, camino_minimo2 = floyd(grafo_tiempo, peso_maximo)
	
	opcion = 1
	while opcion != 0 :
		opcion = tomar_opcion_menu()
		if opcion == 1:
			print "ha elegido buscar el amigo mas popular"	
		
		elif opcion == 2:
			print "ha elegido buscar el amigo mas influyente"
				
		elif opcion == 3:
			print "ha"
			

