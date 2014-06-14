#----------------------------------------#
#password.py 							 #
#Intoduce un user y un password          #
#comprueba si estan dentro de una lista  #
#----------------------------------------#

import sys
#listas con usuarios y password
usuarios = ['Edu','Jose','Javi','Martin']
password = ['camino','de','la','miranda']

#peticion de datos al usuario
username = 'Edu' #input('dime tu nombre => ')
pwd = 'camino' #input('dime tu password => ')

#comprobacion de datos
if username in usuarios:
	posicion = usuarios.index(username)
	if pwd == password[posicion]:
		print("Hola %s, tu password es %s" %(username, pwd ))
	else:
		print("acceso denegado %s"%username)
else:
	print('Siento mucho pero no te reconozco')