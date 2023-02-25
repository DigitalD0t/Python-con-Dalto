#En el siguiente ejercicio obtendremos el valor del tiempo en segundo que una persona puede decir cualquier frase, si pasa de los 120 segundos se le dira, "tampoco te pedimos un testamento"
frase = input("Dime lo que quieras y te calculo cuanto tiempo tardarías en decirmela: ")

#Creamos una lista con todas las palabras de la frase (se separan cada vez que haya un espacio en blanco)
palabra_separadas = frase.split(" ")

#usamos len() para ver la cantidad d elementos que hay en la lista
cantidad_de_palabras = len(palabra_separadas)

#En caso de que tarde más de un minuto en decirlo, le decimos que pase un poco
if cantidad_de_palabras > 120:
	print("para tampoco te pedí un testamento")

#Calculamos cuanto tardaría e decir las palabras y se lo decimos
print(f'Dijiste {cantidad_de_palabras} palabras, y tardarías {cantidad_de_palabras/2} segundo en decirlo')
print(f'Dalto lo diría en {cantidad_de_palabras * 100 // 2 * 1.3 / 100} segundos')