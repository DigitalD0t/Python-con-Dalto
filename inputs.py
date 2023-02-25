#solicitando información al usuario
usuario = input("Cual es tu nombre?: ")
print(f'Hola {usuario} te damos la bienvenida desde python!')
print("El elemento ingresado es de tipo :",  type(usuario))

#para poder solicitar un número y que el interprete reconozca que no es una cadena de caracteres usaremos el metodo int, lo solicitamos y posteriormente lo convertimos a entero
solicita_numero = input("ingresa un numero: ")
resultado = int(solicita_numero) * 3
print(f'El número ingresado es y es entero: {solicita_numero}')
print("el resultado de la multiplicación es", resultado)
print("Y así podemos verificar que el dato ingresado es de tipo entero :", type(solicita_numero))

#Solicitemos un valor flotante (condecimal), lo soclicitamos y posteriormente lo convertimos a flotante
numero_decimal = input("ingresa numeros con decimal: ")
resultado = float(numero_decimal)/3 
print("Y Float: ", resultado)
print("el número ingresado es de tipo: ", type(numero_decimal))
print("si por casualidad ingresaramos un numero no solicitado la aplicación nos daría error... en este caso no porque habéis podido llegar a ver este mensaje")
