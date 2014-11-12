'''
Created on 11/11/2014

@author: jorge
'''
from perfil import Perfil

def main():
    perfil = Perfil.Perfil.fromFile("ejercicioTp.txt")
    resultado = perfil.calcularPerfil(perfil.perfilOriginal, 0)
    print "resultado: " + str(resultado)
    
if __name__ == '__main__':
    main()

    