'''
Created on 18/10/2014

@author: jorge
'''
import unittest
import main
from grafo.grafo import masPopular, masInfluyente,recomendaciones

class Test(unittest.TestCase):


    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMasPopular(self):
        red = main.cargarRedDesdeArchivo("amigosPrueba1.gdf")
        maspopulares = masPopular(red)
        nodoMasPopular = maspopulares[0]
        listaVieja = []
        for v in maspopulares:
            for w in listaVieja:
                booll = len(w.aristas_ad) < len(v.aristas_ad)
                self.assertFalse(booll, "ERROR lista no odenada")
            listaVieja.append(v)
        self.assertEqual(nodoMasPopular.getId(),"5" ,nodoMasPopular.getLabel())
        
    def testMasPopular2(self):
        red = main.cargarRedDesdeArchivo("amigosPruebaEnunciadoTp.gdf")
        maspopulares = masPopular(red)
        nodoMasPopular = maspopulares[0]
        self.assertEqual(nodoMasPopular.getLabel(), "Juana")
        listaVieja = []
        for v in maspopulares:
            for w in listaVieja:
                booll = len(w.aristas_ad) < len(v.aristas_ad)
                self.assertFalse(booll, "ERROR lista no odenada")
            listaVieja.append(v)
    
    def testBFS_1(self):
        red = main.cargarRedDesdeArchivo("amigosPrueba2.gdf")
        s = red.getNodo("5")
        sup = red.BFS(s)
        tomas = sup.pop()
        juan = sup.pop()
       
        self.assertEqual(juan.getLabel() , "JUAN")
        self.assertEqual(juan.layer , 1)
        self.assertEqual(tomas.getLabel() , "TOMAS",)
        self.assertEqual(tomas.layer , 2)
    
    def testBFS_2(self):
        red = main.cargarRedDesdeArchivo("amigosPrueba3.gdf")
        s = red.getNodo("3")
        sup = red.BFS(s)
        
        juan = sup.pop()
        tomas = sup.pop()
        luis = sup.pop()
        pepe = sup.pop()
        
        self.assertEqual(juan.getLabel(), "JUAN")
        self.assertEqual(juan.layer, 2)
        self.assertEqual(tomas.getLabel(), "TOMAS")
        self.assertEqual(tomas.layer, 2)
        self.assertEqual(luis.getLabel(), "LUIS")
        self.assertEqual(luis.layer, 1)
        self.assertEqual(pepe.getLabel(), "PEPE")
        self.assertEqual(pepe.layer, 1)
        
    def testPadres1(self):
        red = main.cargarRedDesdeArchivo("amigosPrueba2.gdf")
        s = red.getNodo("5")
        sup = red.BFS(s)
        red.padres()
        
        tomas = sup.pop()
        self.assertEqual(red.cantCaminos[tomas], 1)
        
        padreDeTomas = tomas.padres[0]
        self.assertEqual(padreDeTomas.getLabel(), "JUAN")
        self.assertEqual(red.cantCaminos[padreDeTomas] ,1)
        
        juan = sup.pop()
        self.assertEqual(red.cantCaminos[juan], 1)
        
        padreDeJuan = juan.padres[0]
        self.assertEqual(padreDeJuan.getLabel(), "PEPE")
    
    def testPadres2(self):
        red = main.cargarRedDesdeArchivo("amigosPrueba3.gdf")
        s = red.getNodo("3")
        sup = red.BFS(s)
        red.padres()
        
        juan = sup.pop()
        tomas = sup.pop()
        luis = sup.pop()
        pepe = sup.pop()
        
        self.assertEqual(red.cantCaminos[pepe] ,1)
        self.assertEqual(red.cantCaminos[luis] ,1)
        self.assertEqual(red.cantCaminos[juan] , 1)
        self.assertEqual(red.cantCaminos[tomas] , 2)
        
        padreDeJuan = juan.padres[0]
        padre1DeTomas = tomas.padres[0]
        padre2DeTomas = tomas.padres[1]
        padreDeLuis = luis.padres[0]
        padreDePepe = pepe.padres[0]
        
        self.assertEqual(padreDeJuan.getLabel(), "LUIS")
        self.assertEqual(padre1DeTomas.getLabel(), "PEPE")
        self.assertEqual(padre2DeTomas.getLabel(), "LUIS")
        self.assertEqual(padreDeLuis.getLabel(), "FER")
        self.assertEqual(padreDePepe.getLabel(), "FER")
       
    def test1SumPadres(self):
        red = main.cargarRedDesdeArchivo("amigosPrueba2.gdf")
        s = red.getNodo("5")
        colaOrdenada = red.BFS(s)
        red.padres()
        red.sumPadre(colaOrdenada)
        
        tomas = colaOrdenada[0]
        juan = colaOrdenada[1]
        
        self.assertEqual(juan.cantVecesUsado[tomas], 1)
        self.assertEqual(tomas.cantVecesUsado[tomas], 0)
    
    def test2SumPadres(self):
        red = main.cargarRedDesdeArchivo("amigosPrueba3.gdf")
        s = red.getNodo("3")
        colaOrdenada = red.BFS(s)
        red.padres()
        red.sumPadre(colaOrdenada)
        
        juan = colaOrdenada[0]
        tomas = colaOrdenada[1]
        luis = colaOrdenada[2]
        pepe = colaOrdenada[3]
        
        self.assertEqual(juan.cantVecesUsado[tomas], 0)
        self.assertEqual(tomas.cantVecesUsado[pepe], 0)
        self.assertEqual(pepe.cantVecesUsado[tomas], 1)
        self.assertEqual(luis.cantVecesUsado[tomas], 1)
        self.assertEqual(luis.cantVecesUsado[juan], 1)
    
    def testCalcularTodosLosIndices1(self):
        red = main.cargarRedDesdeArchivo("amigosPrueba2.gdf")
        lista = red.calcularTodosLosIndices()
        for v in lista:
            print v.getLabel()+" I: "+str(v.indice)
        print""
        
    def testCalcularTodosLosIndices2(self):
        red = main.cargarRedDesdeArchivo("amigosPrueba3.gdf")
        lista = red.calcularTodosLosIndices()
        for v in lista:
            print v.getLabel()+" I: "+str(v.indice)
        print""
    
    def testMasInfluyente1(self):
        red = main.cargarRedDesdeArchivo("amigosPrueba2.gdf")
        nodoMasInfluyente = masInfluyente(red)
        self.assertEqual(nodoMasInfluyente.getLabel(), "JUAN" )
    
    def testMasInfluyente2(self):
        red = main.cargarRedDesdeArchivo("amigosPrueba3.gdf")
        nodoMasInfluyente = masInfluyente(red)
        self.assertEqual(nodoMasInfluyente.getLabel(), "LUIS")
    
    def testMasInfluyente3(self):
        #este test corrobora lo que mandaron por mail del resultado del ejercicio de ejemplo en
        # el enunciado del tp
        red = main.cargarRedDesdeArchivo("amigosPruebaEnunciadoTp.gdf")
        nodoMasInfluyente = masInfluyente(red)
        self.assertEqual(nodoMasInfluyente.getLabel(), "Juana")
        """
        segun el mail, los caminos minimos son:
        En total hay 132 caminos minimos
        Por cada persona pasan la siguiente cantidad de caminos minimos:
        Juana: 38
        Roberto: 38
        Carlos: 22
        Esteban: 16
        Milena: 10
        Monica: 10
        Pablo: 4
        Nora: 0
        Lorena: 0
        Brenda: 0
        Tomas: 0
        """

    """def testSujerirAmigo(self):
        red = main.cargarRedDesdeArchivo("amigosPruebaEnunciadoTp.gdf")
        listaRecomendaciones = recomendaciones(red)
        for item in listaRecomendaciones:
            print "{0}: {1} ({2} amigos en comun)".format(item[0], item[1], item[2])
        pass
        
        LO QUE DIJIERON QUE EL EJEMPLO DEBERIA DEVOLVER(SEGUN EL MAIL QUE MANDARON)
        -----------------recomendaciones-----------------
        Roberto: Esteban (2 amigo(s) en comun)
        Milena: Monica (2 amigo(s) en comun)
        Milena: Carlos (2 amigo(s) en comun)
        Monica: Milena (2 amigo(s) en comun)
        Carlos: Milena (2 amigo(s) en comun)
        Esteban: Roberto (2 amigo(s) en comun)
        Juana: Milena (1 amigo(s) en comun)
        Juana: Monica (1 amigo(s) en comun)
        Juana: Esteban (1 amigo(s) en comun)
        Juana: Pablo (1 amigo(s) en comun)
        Juana: Brenda (1 amigo(s) en comun)
        Pablo: Roberto (1 amigo(s) en comun)
        Pablo: Monica (1 amigo(s) en comun)
        Pablo: Juana (1 amigo(s) en comun)
        Pablo: Tomas (1 amigo(s) en comun)
        Lorena: Milena (1 amigo(s) en comun)
        Lorena: Monica (1 amigo(s) en comun)
        Lorena: Carlos (1 amigo(s) en comun)
        Lorena: Tomas (1 amigo(s) en comun)
        Lorena: Brenda (1 amigo(s) en comun)
        Lorena: Nora (1 amigo(s) en comun)
        Tomas: Roberto (1 amigo(s) en comun)
        Tomas: Esteban (1 amigo(s) en comun)
        Tomas: Pablo (1 amigo(s) en comun)
        Tomas: Lorena (1 amigo(s) en comun)
        Tomas: Nora (1 amigo(s) en comun)
        Brenda: Milena (1 amigo(s) en comun)
        Brenda: Juana (1 amigo(s) en comun)
        Brenda: Esteban (1 amigo(s) en comun)
        Brenda: Lorena (1 amigo(s) en comun)
        Nora: Roberto (1 amigo(s) en comun)
        Nora: Carlos (1 amigo(s) en comun)
        Nora: Lorena (1 amigo(s) en comun)
        Nora: Tomas (1 amigo(s) en comun)
        """

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testMasPopular']
    unittest.main()
