import random
class Persona(object):
	"""Comprueba el imc de una persona que ha de ser mayor de edad
	teniendo en cuenta el sexo que tiene. """
	infrapeso = -1
	sobrepeso = 1
	ideal = 0
	def __init__(self,nombre = '',edad = 0,sexo = 'H' ,peso = 0,altura = 0):
		"""inicializacion de la clase"""
		self.__nombre = nombre
		self.__edad = edad
		self.__sexo = sexo 
		self.__peso = peso 
		self.__altura = altura
		self.__dni=''
		self.__generarDni()
		self.__comprobarSexo()

		

	def imc(self,peso,altura):
		"""calcula el imc de una persona devolviendo si esta en infrapeso (-1), sobrepeso(1) o ideal(0)
			imc(number,number) -> number

			return -1 if infrapeso
			return  0 if sobrepeso
			return  1 if ideal
		"""
		imc = self.__peso/(self.__altura**2)
		if imc<20:
			return infrapeso
		elif imc>25:
			return sobrepso
		else:
			return ideal

	def mayorEdad(self,edad):
		"""Comprobacion de mayoria de edad

			mayorEdad(number) -> bool
			return True if edad equal or over 18
			return False if edad under 18"""
			
		if edad>=18:
			return True
		else:
			return False

	def __comprobarSexo(self):
		"""Comprobacion del sexo H o M, devuelve H por defecto si no se introduce correctamente
		__comprobarSexo() -> Bool
		"""
		if self.__sexo != 'H' and self.sexo != 'M':
			self.__sexo = 'H'
		return self.__sexo 
	def toString(self):
		sexo = ''
		if self.__sexo == 'H':
			sexo = 'hombre'
		else:
			sexo = 'mujer'

		return 'Informacion de la persona:\n' +	'Nombre: ' + self.nombre + '\n' + 'Sexo: ' + self.sexo + '\n' +	'Edad: ' + str(self.edad) + '\n' + 'DNI: ' + self.dni + '\n'+ 'Peso: ' + str(self.peso) + '\n' + 'Altura: ' + str(self.altura) + '\n'


	def __generarDni(self):
		"""Genera un DNI aleatorio
		"""
		dni = random.randint(0,99999999)
		#dni = '%08d'%dni
		#print(dni)
		#dni = int(dni)
		#print(dni)
		resultado = dni%23
		self.__dni = str(dni) + self.__letraDni(resultado)
	def __letraDni(self,letraDni):
		"""Devuelve letra de DNI alojado en una lista al pasarle un indice 
			__letraDni(String) -> String
		"""
		listaLetras=['T', 'R', 'W', 'A', 'G', 'M', 'Y',
					 'F', 'P', 'D', 'X', 'B', 'N', 'J',
					 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
		return listaLetras[letraDni]

	def __setNombre(self,nombre):
		"""Modifica nombre del objeto"""
		self.__nombre = nombre
	def __getNombre(self):
		"""devuelve nombre del objecto
		__getNombre()->String
		"""
		return self.__nombre

	nombreProperty = property(fget = __getNombre,fset=__setNombre,doc='Nombre')


persona1 = Persona(nombre = 'ews',edad = 40,sexo = 'H' ,peso = 20,altura = 230)
#print(persona1.__nombre) esto no lo imprime porque cariable __nombre es privado

#print(persona1.nombreProperty)
persona1.nombreProperty='jose luis gonzales'
print(persona1.nombreProperty)
#persona2=Persona()
#persona2.nombre='joder'
#print(persona2.nombre)
#persona2.nombre='pepito perez'
#print('el nombre de la persona 2 es' + persona2.nombre)
#print(persona1.comprobarSexo())
#print(persona1.toString())
