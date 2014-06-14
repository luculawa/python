class Dog():
	def __init__(self,nombrePerro,colorPerro,alturaPerro,fisicoPerro,caracterPerro,edadPerro):
		self.nombrePerro = nombrePerro
		self.colorPerro = colorPerro
		self.alturaPerro = alturaPerro
		self.fisicoPerro = fisicoPerro
		self.caracterPerro = caracterPerro
		self.edadPerro = edadPerro
		self.hambriento = False
		self.cansado = False
	def comer(self):
		if self.hambriento:
			print('Guau Guau, tengo hambre')
			self.hambriento = False
		else:
			print('que engordo, dejalo')
	def dormir(self):
		print('ZZzzzzzzzzzzzzzz ZZzzzzzzzzzz')
		self.cansado = False
	def ladrar(self):
		if self.caracterPerro == 'malo':
			print('GRRRRRRRRR')
		elif self.caracterPerro == 'bonachon':
			print('youuu youuu')
		elif self.caracterPerro == 'loco':
			print('hihihihi')
		else:
			print('juau juau')
	def infoPerro(self):
		print ('Mi nombre es %s' % self.nombrePerro)
		print ('Mi color es %s' % self.colorPerro)
		print ('Mi humor es %s' % self.caracterPerro)
		print ('Tengo hambre = %s' % self.hambriento)

perro1 = Dog('Luna', 'marron', 18, 'atletico', 'bonachon', 22)
perro1.infoPerro()
perro1.comer()
perro1.hambriento = True
perro1.comer()
