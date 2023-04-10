frutas = ["banana", "manzana", "ciruela", "pera", "naranja", "granada", "durazno"]
cadena = "Hola Brandon"
numeros = [23, 34, 21, 54]

for fruta in frutas:
	if fruta =='granada':
		continue #con continue podemos hacer que el bucle continue recorriendo la lista, sin interrumpir el programa
	print(f'Con continue..: {fruta}')
else:
	print('Se terminó el bucle')

#evitamos que se termine de ejecutar el programa...
for fruta in frutas:
	print(f'Con break... {fruta}')
	if fruta == 'pera':
		break #evitamos que el bucle continue.
else:
	print('Terminado')

#recorriendo una cadena de texto
for texto in cadena:
	print(texto)

#recorriendo y multiplicando numeros en una sola linea con el for
numeros_multiplicados = [x*2 for x in numeros]
print(f'Veamos el resultado de un numero x multiplicado por 2 {numeros_multiplicados}')