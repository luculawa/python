titulo_valores = [['cocacola',1,50],['whisky',4,55],['acuarios',2,25]]

def bordeArribaAbajo(caracter,longitud):
	return '%s%s%s' %('+',(caracter*(longitud-2)),'+')

def fmt(titulo,left,valor,right):
	part2 = '%.2f' %valor
	return '%s%s%s%s' %('| ',titulo.ljust(left-2,' '),part2.rjust(right-2,' '),' |')


def imprimeTablaProductos():
	total = 0
	print(bordeArribaAbajo('*',40))
	for productos in range(len(titulo_valores)):
		total += titulo_valores[productos][1]
		print(fmt(titulo_valores[productos][0],30,titulo_valores[productos][1],10))
	print(bordeArribaAbajo('-',40))
	print(fmt('total', 30, total, 10))
	print(bordeArribaAbajo('*',40))

imprimeTablaProductos()