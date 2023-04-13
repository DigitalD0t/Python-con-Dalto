numeros = [32,12,321,456, 1029]

#encontrando el número mayor de una lista 
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#encontrando el número menor de una lista
numeros_mas_chico = min(numeros)
print(numeros_mas_chico)

#redondeando a 6 decimales
numero = round(13.141618191214562545, 6)
print(f'Redondeando con round() {numero}')

#retorna false -> 0, vacio, false, ninguno (null)
resultado_bool = bool(9)
print(resultado_bool)

def saludar(nombre,sexo):
	sexo = sexo.lower()
	if (sexo == "hombre"):
		adjetivo = "titan"
	elif (sexo == "mujer"):
		adjetivo = "reina"
	else:
		adjetivo = "amor"

	print(f'hola {nombre} mi {adjetivo} como estas?')

saludar("rene", "no binario")
saludar("Brandon","hombre")
saludar("camila","Mujer")

#Crear una funcion que nos retorne valores
def crear_contraseña_random(num):
	chars= "sdjkhcgunlcixh"
	num_entero = str(num)
	num = int(num_entero[0])
	c1 = num - 4
	c2 = num
	c3 = num - 7
	contraseña = f'{chars[c1]}{chars[c2]}{chars[c3]}{num*2}'
	return contraseña,num #aquí ene ste punto los valores no serán mostrados por ningun lado unicamente estamos obteniendo los valores

#Para obtener los valores de la función la asignamos a una variables, con su respectiva propiedad de la siguietne manera
#desempaquetando la función...
password, primer_numero = crear_contraseña_random(5)


#mostrando los resultados obtenidos y los datos utilizados para obtenerlos
print(f'Tu nueva contraseña es: {password}')
print(f'Y los datos para crearla fueron: {primer_numero}')