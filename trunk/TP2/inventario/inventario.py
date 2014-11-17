#!/usr/bin/env python
#encoding:UTF-8

class Inventario:
	def __init__(self, cantMeses, tamDeposito, costoCamion, costoOrden):
		""" Meses totales """
		self.cantMeses = cantMeses
		""" Tamaño del depósito en donde se almacen stock """
		self.tamDeposito = tamDeposito
		""" Costo de mantener un camion en el deposito """
		self.costoCamion = costoCamion
		""" costo por emitir una orden de compra """
		self.costoOrden = costoOrden
		""" vector con las compras emitidas """
		self.compras = [0]* cantMeses
		""" espacio disponible en deposito """
		self.espacio = tamDeposito
		""" Mes en el que se realizó la última compra """
		self.ultimaCompra = 0
		self.mesActual = 0

	def agregarDemanda(self, demanda):
		""" Si la demanda entra en el depósito"""
		entraDemanda = (self.espacio - demanda) > 0
		""" Si almacenar en deposito es más barato que emitir compra """
		costoAlmacenar = (self.mesActual - self.ultimaCompra) * self.costoCamion * demanda
		esRentable = costoAlmacenar <= self.costoOrden
		if (not entraDemanda or not esRentable):
			""" Realizo una compra """
			self.ultimaCompra = self.mesActual
			""" vacio el deposito """
			self.espacio = self.tamDeposito 
		else:
			self.espacio -= demanda
		self.compras[self.ultimaCompra] += demanda
		self.mesActual += 1

def main():
	"""Asumo camino feliz :D"""
        fd = open("inventario.txt", 'rb')
	cantMeses = int(fd.readline())
	tamDeposito = int(fd.readline())
	costoCamion = int(fd.readline())
	costoOrden = int(fd.readline())
	inventario = Inventario(cantMeses, tamDeposito, costoCamion, costoOrden)

	"""Cargo los meses"""
	fd.readline()
	for i in range(cantMeses):
		demanda = int(fd.readline())
		inventario.agregarDemanda(demanda)
	print inventario.compras

main()
