#Con for iteramos los items de una lista para poder entender esto veamos el siguiente ejemplo.
animales = ["perro","gato","loro","cocodrilo","jirafa"]
numeros = [134,321,4343,35,232]

#recorriendo la lista animales
for animal in animales:
	print(f'Ahora la variable animal es igual a: {animal}')


for numero in numeros :
	resultado = numero * 10
	print(f'cada numero de la lista se multiplicara por 10 lo cual el resultado será: {resultado}')


#el siguiente formato es para iterar a dos listas al mismo tiempo 
for numero, animal in zip(numeros, animales):
	print(f'Recorriendo la lista de numeros: {numero}')
	print(f'Recorriendo la lista de animales: {animal}')
	#recordando así que las listas deben de tener la misma lomgitud entre si, osea el mismo número de elementos para poder así imprimirlas completas.

#función range() que sirve para iterar el numero de veces que se le asigne dentro de los parentesis, si hay 2 parametros el primero indica desde que punto irá a comenzar la iteración y el segundo hasta que punto irá a parar la iteración, habiendo un parametros indica que hasta ahí se va a iterar, tomando como inicio el numero 0, ejemplo....
for rango in range(10):
	print(f'usando como único parametro el 10 {rango}')

for rango in range(70,100):
	print(f'usando como parametro inicial el numero 70 y como parametro final el 100 {rango}')

#forma no optima de recorrer una lista con su indice (no funciona en conjuntos)
for num in range (len(numeros)):
	print(numeros[num])

#forma correcta de recorrer una lista con su indice 
for num in enumerate(numeros):
	indice = num[0]
	valor = num[1]
	print(f'El indice es: {indice}  y el valor es: {valor}')

#También existe una forma de recorrer la lista usando for/else de la siguiente manera:
for numero in numeros:
	print(f'Ejecutando el ultimo bucle actual: {numero}')
else:
	print(f'El bucle terminó.')


#Los conjuntos se pueden iterar al igual que las listas/tuplas, sin embargo estos no aceptaran la funcion de range(len()) encambio las tuplas si lo ejecutan.