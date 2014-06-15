import datetime
ultimaId = 0
class Nota(object):
	"""Representa una nota en el cuaderno. 
		se compara con un string en busquedas 
		y tags"""

	def __init__(descripcion,tag=''):
		global ultimaId
		ultimaId =ultimaId + 1
		self.descripcion = descripcion
		self.tag = tag
		self.creacionFecha = datetime.date.today()
		self.id = ultimaId
	def match(self,comparador):
		return comparador in self.descripcion or comparador in self.tag

class Cuaderno(object):
	def __innit__(self):
		self.notas = []
	def nuevaNota(self,descripcion,tag=''):
		self.notas.append(Nota(descripcion,tag))
	def _encontrarNota(self,notaId):
		for nota in self.notas:
			if str(nota.id) == str(notaId):
				return nota
		return None
	def modificar_descripcion(self,notaId,descripcion):
		nota = self._encontrarNota(notaId)
		if nota:
			nota.descripcion = descripcion
	def modificar_tag(self,notaId,tag):
		nota = _encontrarNota(notaId)
		if nota:
			nota.tag = tag
	def buscar(self,filtro):
		for nota in range(len(self.notas)):
			if nota == nota.match(filtro):
				return nota
		#return[nota for nota in self.notas if nota.match(filtro)]