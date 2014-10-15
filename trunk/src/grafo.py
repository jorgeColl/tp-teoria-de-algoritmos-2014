#!usr/bin/env python
#encoding:windows-1251
import heapq
import os

class Nodo (object):
	def __init__(self, id_nodo):
		
		self.id_nodo = id_nodo
		
		"""aristas adyacentes al nodo"""
		self.aristas_ad = []
		
		"""atrubuto que se utiliza para la funcion prim"""
		self.visitado = False
		
		"""atributo para no tomar en cuenta al nodo cuando se use la
		funcion prim"""
		self.restringido = False
	
class Arista (object):
	def __init__(self, origen, destino):
		
		""" origen y destino son dos variables de la clase nodo """
		self.origen = origen
		self.destino = destino
		
		""" peso ponderado """
		self.peso = 0
		
		
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

class Grafo (object):
	
	def __init__(self):
		""" diccionario que guardará a todos los nodos que contenga el
		grafo """
		self.dicc_nodos = {}	
		
		self.dicc_cam_min = {}
	""" recive al id_nodo ,crea un Nodo y lo agrega a los nodos que 
	contiene el grafo """
	def ingresar_nodo(self, id_nodo):
		
		nodo = Nodo(id_nodo)
		self.dicc_nodos[id_nodo] = nodo
		
	"""crea una arista y la mete en su correspondiente nodo
	pre: los nodos tiene que estar creados"""
	def ingresar_arista(self, id_origen, id_destino):
		
		nodo_destino = self.dicc_nodos[id_destino]
		nodo_origen = self.dicc_nodos[id_origen]
		
		arista = Arista(nodo_origen, nodo_destino)
		
		nodo_origen.aristas_ad.append(arista)
				
				
	
	""" carga el peso en una arista previamente creada """
	def cargar_peso_arista(self, id_origen, id_destino, peso):
		for ar in self.dicc_nodos[id_origen].aristas_ad:
			if ar.destino.id_nodo == id_destino:
				ar.peso = int(peso)
				break
		
	""" devuelve una lista de los ids de los vecinos que tiene un
	nodo dado y que no estan restringidos """
	def vecinos_no_restringidos(self, nodo_id):
		lista_vecinos = []
		nodo = self.dicc_nodos[nodo_id]
		
		for arista in nodo.aristas_ad:
			if arista.destino.restringido == False:
				lista_vecinos.append(arista.destino.id_nodo)
		
		return lista_vecinos
		
		
	""" dado un id_origen y un id_destino se busca y devuelve la arista
	que tenga origen en id_origen y destino en id_destino
	pre: arista buscada debe existir """
	def arista(self, id_origen, id_destino):
		nodo = self.dicc_nodos[id_origen]
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


def tomar_opcion_camino():
	print '¿Que desea hacer?'
	print "'1' para buscar camino mas rapido"
	print "'2' para buscar camino mas confiable"
	print "'3' para buscar el camino con menos agentes involucrados"
	print "'4' para mostrar arbol tendido minimo de tiempo"
	print "'5' para mostrar arbol tendido minimo de confianza"
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


""" devuelve una tupla de ids (origen,destino) que sera el origen y
destino en el grafo """
def tomar_origen_destino(dicc_nombre_id):
	print"para agente emisor"
	origen = tomar_agente (dicc_nombre_id)
	print "para agente receptor"
	destino = tomar_agente (dicc_nombre_id)
	
	return origen,destino


def tomar_agente (dicc_nombre_id):
	while True:
		try:
			nombre = raw_input('ingrese nombre del agente ')
			id = dicc_nombre_id[nombre]
			break
			
		except:
			print "ingrese agente valido"
			pass
	return id


"""crea dos diccionarios a partir del archivo que contiene a los agentes
un diccionario sera dicc_id_nombre[id] = nombre y el otro lo opuesto """
def crear_dicc_agentes(nombre_archivo):
	
	dicc_id_nombre = {}
	dicc_nombre_id = {}
	
	archivo = open(nombre_archivo)
	lineas = procesar_lineas_archivo(archivo)
	
	for linea in lineas:
		dicc_id_nombre[linea[0]] = linea[1]+" "+linea[2]
		dicc_nombre_id[linea[1]+" "+linea[2]] = linea[0]
	
	archivo.close()
	return dicc_id_nombre,dicc_nombre_id


""" recive por parte del usuario el peso maximo que se permitirá 
de las aristas en el grafo si no se quiere ingresar un peso maximo
se devuelce peso maximo infinito"""
def tomar_peso_maximo():
	
	opcion = raw_input("desea asignar un maximo tiempo/confianza si/no ")
	if opcion == "no":
		return float("inf")
		
	peso = raw_input("ingrese tiempo/confianza maxima entre agentes: ")
	return int(peso)
	
	
""" recibe por parte del usuario los nodos por los cuales no se pasará
en el grafo """
def tomar_nodos_excluir(dicc_nombre_id):
	
	lista_negra = []
	while True:
		opcion = raw_input("desea agregar un agente a la lista negra si/no ")
		
		if opcion == "no":
			break
		
		lista_negra.append(tomar_agente(dicc_nombre_id))
	return lista_negra


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
	
	print "formato esperado 1er archivo:  id nombre apellido "
	#nombre_archivo1 = tomar_nombre_archivo()
	print "formato esperado 2do archivo: id1 id2 confianza tiempo "
	#nombre_archivo2 = tomar_nombre_archivo()
	
	nombre_archivo1 = "agentes"
	nombre_archivo2 = "caminos"
	
	dicc_id_nombre, dicc_nombre_id = crear_dicc_agentes(nombre_archivo1)
	
	grafo_tiempo = Grafo() #para mejor tiempo
	grafo_confianza = Grafo() #para camino mas confiable
	# para recorrido por min cant de nodos implicados
	grafo_nodos = Grafo()
	
	cargar_datos(nombre_archivo1, grafo_nodos, "agentes")
	cargar_datos(nombre_archivo2, grafo_nodos, "nodos")
	
	cargar_datos(nombre_archivo1, grafo_confianza, "agentes")
	cargar_datos(nombre_archivo2, grafo_confianza, "confianza")
	
	cargar_datos(nombre_archivo1, grafo_tiempo, "agentes")
	cargar_datos(nombre_archivo2, grafo_tiempo, "tiempo")
	
	peso_maximo = tomar_peso_maximo()
	lista_negra = tomar_nodos_excluir(dicc_nombre_id)
	
	#aplico restricciones de los nodos que el usuario no quiere pasar por
	grafo_tiempo.aplicar_restricciones_nodo(lista_negra)
	grafo_confianza.aplicar_restricciones_nodo(lista_negra)
	grafo_nodos.aplicar_restricciones_nodo(lista_negra)
	
	
	distancia1, camino_minimo1 = floyd(grafo_confianza, peso_maximo)
	distancia2, camino_minimo2 = floyd(grafo_tiempo, peso_maximo)
	""" no se tomará el peso maximo en este caso """
	distancia3, camino_minimo3 = floyd(grafo_nodos, None)
	
	
	
	opcion = tomar_opcion_camino()
	while opcion != 0 :
		
		if opcion == 4:
			origen = tomar_agente(dicc_nombre_id)
			arbol_tend_min(grafo_tiempo, origen, dicc_id_nombre, peso_maximo)
			
		elif opcion == 5:
			origen = tomar_agente(dicc_nombre_id)
			arbol_tend_min(grafo_confianza, origen, dicc_id_nombre, peso_maximo)
				
		else:
			origen, destino = tomar_origen_destino(dicc_nombre_id)
			
			if opcion == 1:
				
				camino = camino_minimo1[origen][destino]
				imprimir_camino(camino, dicc_id_nombre, destino)
				
			elif opcion == 2:
				
				camino = camino_minimo2[origen][destino]
				imprimir_camino(camino, dicc_id_nombre, destino)
				
			elif opcion == 3:
				camino = camino_minimo3[origen][destino]
				imprimir_camino(camino, dicc_id_nombre, destino)
			
		
		opcion = tomar_opcion_camino()
			
	
main()
