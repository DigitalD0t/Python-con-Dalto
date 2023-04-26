def frase(nombre,apellido,adjetivo):#función con parametros posicionales, quiere decir, el orden tal cual son escritos deberan 
	return f'Hola {nombre} {apellido}, soy muy {adjetivo}'
frase_resultante = frase("brandon","monreno","hermoso")
print(frase_resultante)