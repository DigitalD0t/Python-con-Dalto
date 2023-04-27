#definimos una función con 3 parametros 
def frase(nombre,apellido,adjetivo):#función con parametros posicionales, quiere decir, el orden tal cual son escritos deberan ser asignados 
	return f'Hola {nombre} {apellido}, soy muy {adjetivo}'
frase_resultante = frase("brandon","monreno","hermoso")
print(frase_resultante)

#de esta forma podemos asignar valor a los parametros in importar el orden y aún así se respetara el orden de los parametos
frase_resultante = frase(adjetivo="precioso",nombre="Brandon",apellido="Moreno")
print(frase_resultante)

#en esta función estamos forzando un parametro que es adjetivo, esto quiere decir que el arametro es opcional o como se les conoce kewords 
def frase_2(nombre,apellido,adjetivo="buenardo"):
	return f'Hola {nombre} {apellido}, eres un {adjetivo}'
frase_resultante = frase_2("Brandon", "Moreno")
print(frase_resultante)

#de la siguiente manera podremos cambiar el parametro forzado u opcional
frase_resultante = frase_2("juan","benitez",adjetivo="estipido por no decirte otra cosa")
print(frase_resultante)