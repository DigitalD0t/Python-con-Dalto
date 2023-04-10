diccionario = {
	"nombre": "brandon",
	"apellido":"moreno",
	"notas": 8.5
}

#Recorriendo diccionario para obtener las claves.
for key in diccionario:
	print(f'Clave del diccionario {key}')

#Recorriendo el diccionario con la ayuda de la función items()
for key in diccionario.items():
	print(f'Recorriendo diccionario con función items() {key}')

#Recorriendo el diccionario con la ayuda de la función items() para obtener los valores con su indice 
for dato in diccionario.items():
	key = dato[0]
	value = dato[1]
	print(f'la llave es: {key}. el valor es: {value}')