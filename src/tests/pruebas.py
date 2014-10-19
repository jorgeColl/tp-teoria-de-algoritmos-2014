'''
Created on 18/10/2014

@author: jorge
'''
import unittest
import main
from grafo.grafo import masPopular, masInfluyente

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testMasPopular(self):
        red = main.cargarRedDesdeArchivo("amigosPrueba1.gdf")
        maspopular = masPopular(red)
        self.assertEqual(maspopular.getId(),"5" ,maspopular.getLabel())
    
    def testMasPopular2(self):
        red = main.cargarRedDesdeArchivo("amigosPruebaEnunciadoTp.gdf")
        nodoMasPopular = masPopular(red)
        self.assertEqual(nodoMasPopular.getLabel(), "Juana", "no coinciden los mas inlfuyentes, lo obtenido fue "+nodoMasPopular.getLabel())
        
    def testMasInfluyente1(self):
        print "amigosPrueba2.gdf"
        red = main.cargarRedDesdeArchivo("amigosPrueba2.gdf")
        nodoMasInfluyente = masInfluyente(red)
        self.assertEqual(nodoMasInfluyente.getLabel(), "JUAN", "no coinciden los mas inlfuyentes")
    
    def testMasInfluyente2(self):
        print "amigosPrueba3.gdf"
        red = main.cargarRedDesdeArchivo("amigosPrueba3.gdf")
        nodoMasInfluyente = masInfluyente(red)
        self.assertEqual(nodoMasInfluyente.getLabel(), "LUIS", "no coinciden los mas inlfuyentes")
        
    def testMasInfluyente3(self):
        #este test corrobora lo que mandaron por mail del resultado del ejercicio de ejemplo en
        # el enunciado del tp
        print "amigosPruebaEnunciadoTp.gdf"
        red = main.cargarRedDesdeArchivo("amigosPruebaEnunciadoTp.gdf")
        nodoMasInfluyente = masInfluyente(red)
        self.assertEqual(nodoMasInfluyente.getLabel(), "Juana", "no coinciden los mas inlfuyentes se obtuvo: "+nodoMasInfluyente.getLabel())
        """segun el mail, los caminos minimos son:
        En total hay 132 caminos mínimos
        Por cada persona pasan la siguiente cantidad de caminos mínimos:
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
    def testMasInfluyente4(self):
        red = main.cargarRedDesdeArchivo("amigosPrueba1.gdf")
        nodoMasInfluyente = masInfluyente(red)
        #TODAVIA TENGO QUE HACER LA CUENTA DE SI ESTA BIEN EL RESULTADO
        print nodoMasInfluyente
                
    
    def testSujerirAmigo(self):
        red = main.cargarRedDesdeArchivo("amigosPruebaEnunciadoTp.gdf")
        pass
        """ LO QUE DIJIERON QUE EL EJEMPLO DEBERIA DEVOLVER(SEGUN EL MAIL QUE MANDARON)
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