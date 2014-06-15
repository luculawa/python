import sys
from cuaderno import Cuaderno, Nota

class Menu(object):
	def __init__(self):
		self.cuaderno = Cuaderno()
		self.eleccionMenu = {'1': self.mostrarNotas,
							 '2': self.buscarNotas,
							 '3': self.anadirNotas,
							 '4': self.modificarNotas,
							 '5': self.salir
							 }
	def mostrarMenu(self):
		print("""Menu Cuaderno
			1 Mostrar todas las notas
			2 Buscar notas
			3 Añadir notas
			4 Modificar notas
			5 Salir""")

	def run(self):
		while True:
			self.mostrarMenu()
			eleccion = 3 #input('Escribe una opcion: ')
			accion = self.eleccionMenu.get(eleccion)
			if accion:
				accion()
			else:
				print('Eleccion %s no valida' %eleccion)
	def mostrarNotas(self):
		if not notas:
			notas = self.cuaderno.notas
		for nota in notas:
			print('%s  %s  %s' %(nota.id,nota.descripcion,nota.tag))
	def buscarNotas(self):
		filtro=input('que vas a buscar: ')
		self.cuaderno.buscar(filtro)
		self.mostrarNotas()
	def anadirNotas(self):
		descripcion = input('escribe una descripcion: ')
		self.cuaderno.nuevaNota(descripcion)
		print('Nueva nota añadida')
	def modificarNotas(self):
		id = input('que nota (ID) quieres modificar: ')
		descripcion = input('modifica la descripcion: ')
		tag = input('modifica el tag ')

		if descripcion:
			self.cuaderno.modificarDescripcion(id,descripcion)
		if tag:
			self.cuaderno.modificarTag(id,tag)

	def salir(self):
		print('Asias por usar el cuaderno')
		sys.exit(0)
if __name__=='__main__':
	Menu().run()