#falto el profe y los chicos van a hacer la clase

#función para obtener al asistente y al profesor segun la edad
def obtener_compañeros(cantidad_de_compañeros):
	#creamos la lista con los compañeros
	compañeros = []
	#ejecutando un for para pedir la información de cada compañero
	for i in range(cantidad_de_compañeros):
		nombre = input("ingresa el nombre del compañero")
		edad = int(input("ingrese la edad del compañero"))
		compañero = (nombre,edad)

		#agregando la información a la lista
		compañeros.append(compañero)

	#ordenandolos de menor a mayor segun su edad
	compañeros.sort(key=lambda x:x[1])

	#compaeros[x] devuelve una tupla con (nombre,edad) y después accedemos al nombre
	#para definir al asistente y al profesor.
	asistente = compañeros[0][0]
	profesor = compañeros[-1][0]

	#retornamos una tupla
	return asistente, profesor

#desempaquetamos lo que nos retorna la funcion
asistente,profesor = obtener_compañeros(5)

#mostramos el resultado
print(f'el profesor es: {profesor} y su asistente es: {asistente}') 