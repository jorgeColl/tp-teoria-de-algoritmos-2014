'''
Created on 23/11/2014
@author: jorge y matias y andres
'''
from dinamic.solver import Solver
def parse (nombreArchivo):
    listaTareas = []
    with open(nombreArchivo, 'rb') as fd:
            for fila in fd:
                numeros = fila.split(",")
                for x in range(0,len(numeros)):
                    numeros[x] = int(numeros[x])
                listaTareas.append(numeros)
    return listaTareas

def main():
    listaTareas = parse("tareas.txt")
    print "Tareas originales: " + str(listaTareas)
    solv = Solver(listaTareas)
    solucion = solv.solve()
    print "La solucion es: "+str(solucion)

if __name__ == '__main__':
    main()