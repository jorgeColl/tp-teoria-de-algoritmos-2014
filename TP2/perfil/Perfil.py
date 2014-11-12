'''
Created on 11/11/2014

@author: jorge
'''

class Perfil(object):
    @classmethod
    def fromFile(self,nombreArchivo):
        perfil = Perfil()
        perfil.perfilOriginal = []
        with open(nombreArchivo, 'rb') as fd:
            for fila in fd:
                fila = fila.strip("()\n")
                numeros = fila.split(",")
                for x in range(0,len(numeros)):
                    numeros[x] = int(numeros[x])
                perfil.perfilOriginal.extend(numeros)
                perfil.perfilOriginal.append(0)
        return perfil
    
    def calcularPerfil(self, listaPerfiles, nivelIteracion):
        resultado = self._calcularPerfil(listaPerfiles, nivelIteracion)
        #se elimina el ultimo numero que simpre es 0
        resultado.pop()
        return resultado
    
    def _calcularPerfil(self, listaPerfiles, nivelIteracion):
        #sleep (1)
        # condicion de corte de la division
        if len(listaPerfiles) == 4:
            return listaPerfiles
        
        mitad = len(listaPerfiles) / 2
        while(mitad%4.0 !=0):
            mitad +=2
        #stri =""
        #for n in range(0,nivelIteracion):
        #    stri+="|  "
        #print stri+"lista entera" + str(listaPerfiles)
        perfilesProcesados1 = self._calcularPerfil(listaPerfiles[0:mitad],nivelIteracion+1)
        #print stri+"mitad izq" + str(listaPerfiles[:mitad])
        perfilesProcesados2 = self._calcularPerfil(listaPerfiles[mitad:],nivelIteracion+1)
        #print stri+"mited der" +str(listaPerfiles[mitad:])
        unionPerfilesProcesados = self.unirPerfilesProcesados(perfilesProcesados1, perfilesProcesados2)
        #print stri+"union " + str(unionPerfilesProcesados)
        #print ""
        return unionPerfilesProcesados
    
    """ en cada "evento" se compara las alturas y se queda la mas alta """
    def unirPerfilesProcesados(self, perfil1, perfil2):
        unionPerfiles = []
        posP1 = 0
        posP2 = 0
        AlturaActual = 0
        H1 = 0
        H2 = 0
        X1 = perfil1[posP1]
        X2 = perfil2[posP2]
        
        
        while (X1>=0 and X2>=0):
            if(X1 < X2):
                H1 = perfil1[posP1+1]
                maxVersus = max(H1,H2)
                if(maxVersus != AlturaActual):
                    AlturaActual = maxVersus
                    unionPerfiles.append(X1)
                    unionPerfiles.append(maxVersus)
                
                if(posP1+2 == len(perfil1)):
                    X1=-1
                else:
                    posP1+=2
                    X1=perfil1[posP1]
                               
            else:
                H2 = perfil2[posP2+1]
                maxVersus = max(H1,H2)
                if(maxVersus != AlturaActual):
                    AlturaActual = maxVersus
                    unionPerfiles.append(X2)
                    unionPerfiles.append(maxVersus)
                
                if(posP2+2 == len(perfil2)):
                    X2=-1
                else:
                    posP2+=2
                    X2=perfil2[posP2]
                
        
        
        if(X1<0):
            #print "unir faltante de perfil 2: "+str(perfil2[posP2:])
            """while(X2>0):
                print "agregando X2: "+str(X2)+" H2: "+str(H2)
                unionPerfiles.append(X2)
                unionPerfiles.append(H2)
                if(posP2+2 == len(perfil2)):
                        X2=-1
                else:
                    posP2+=2
                    X2=perfil2[posP2]
                    H2=perfil2[posP2+1]
            """
            unionPerfiles.extend(perfil2[posP2:])
                 
        elif(X2<0):
            #print "unir faltante de perfil 1: "+str(perfil1[posP1:]) 
            """while(X1>0):
                print "uniendo X1: "+str(X1)+" H1: "+str(H1)
                unionPerfiles.append(X1)
                unionPerfiles.append(H1)
                if(posP1+2 == len(perfil1)):
                        X1=-1
                else:
                    posP1+=2
                    X1=perfil1[posP1]
                    H1=perfil1[posP1+1]
            """
            unionPerfiles.extend(perfil1[posP1:])
        
        return unionPerfiles
        
        
