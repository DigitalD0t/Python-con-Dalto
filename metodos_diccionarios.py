#Creamos el diccionario con su sintaxis corresponidente, la cual esta compuesta por una llave y su valor
diccionario = {
	"nombre": "Brandon",
	"apellido":"Moreno",
	"edad":20
}

#imprimimos el diccionario para ir viendo como le afectan los metodos llamados por ython
print(diccionario)
claves = diccionario.keys()
#imprimimos las llave del diccionario
print("imprimimos las llaves del dicionaroio: ", diccionario.keys())

obtener_elemento = diccionario.get("apellido")
#con el siguiente metodo obtendremos el valor especificado de la llave mensionada dentro de los párentesis, algo a saber es que el parametro dado tiene que ser la llave del elemento
print("obtenemos el valor de la llave llamandola con get: ", obtener_elemento)


#Con el siguiente metodo nos devuelve del diccionario los elementos que son iterables
diciconario_iterable = diccionario.items()
print("Obteniendo los elementos iterables del diccionario: ", diciconario_iterable)

#Eliminia un elemento del dicionario antes de eliminarlo por completo con clear
borrando_elemento = diccionario.pop("edad")
print("veamos el resultado con pop: ", diccionario)

#limpiamos el diccionario con el siguiente metodo
diccionario_vacio = diccionario.clear()
print("el diccionario viene vacio",diccionario_vacio)
