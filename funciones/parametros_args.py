def suma(a,b):
	return a+b

resultado = suma(5,6)
print(resultado)

#Forma no optima de sumar valores
def sumavalores(lista):
	numeros_sumados = 0
	for numero in lista:
		numeros_sumados = numeros_sumados + numero
	return numeros_sumados
resultado = sumavalores([4,78,3,473,21])
print(resultado)

#Usando el parametro args *
def sumatotal(nombre, *numeros): #algo que hay que resaltar de este parametro es que es obligatorio usarlo al final de los parametros ya que python hace caso omiso a los parametros después de este 
	return f'la suma de tus numeros es {sum(numeros)}'
	resultado = sumatotal("brandon",15,35,87)
	print(resultado)