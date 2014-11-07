#!/usr/bin/env python
'''
Created on 14/10/2014


'''
import grafo
import csv
from grafo.grafo import masPopular, masInfluyente, recomendaciones

def cargarRedDesdeArchivo(nombreArchivo):
    red = grafo.Grafo()
    with open(nombreArchivo, 'rb') as fd:
        graphReader = csv.reader(fd) 
        for row in graphReader:
            if(len(row) == 5):
                nodo = grafo.Nodo(row[0],row[1]) 
                red.ingresar_nodo(nodo)
            elif(len(row)==2):
                red.ingresar_arista(row[0], row[1])
    return red

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

def main():
    red = cargarRedDesdeArchivo("amigos.gdf")
    
    opcion = 1
    while opcion != 0 :
        opcion = tomar_opcion_menu()
        if opcion == 1:
            print "ha elegido buscar el amigo mas popular"
            print "su amigo mas popular es:"
            amigoMasPopularres = masPopular(red) 
            for amigo in amigoMasPopularres:
                print amigo.getLabel()
        
        elif opcion == 2:
            print "ha elegido buscar el amigo mas influyente"
            print "su amigo mas influyente es:"
            amigoMasInfluyente = masInfluyente(red)
            print amigoMasInfluyente
                
        elif opcion == 3:
            print "ha elegido que armemos una lista de sugerencias"
            listaRecomendaciones = recomendaciones(red)
            for item in listaRecomendaciones:
                print "{0}: {1} ({2} amigos en comun)".format(item[0], item[1], item[2])

main()
