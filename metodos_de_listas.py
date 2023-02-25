#lis palabra clave de python encargada de asignar listas
#lista....
lista =list(["camila","te","amo",12,45])
lista_numerica = list([23,45,123,21])

#en seguida veremos varios metodos utiles para modificar listas ya creadas, o crear nuevas listas.

#metodo antes visto devuelve el el nuemro total de caracteres dentro de una cadena, pero usandolo aqui funciona para decir cuantos items hay en una lista, por ejemplo
cantidad_items =len(lista)
print("total: ",cantidad_items)

#Agrega un elemento a la lista con el metodo append, teniendo en cuenta que este agrega el elemento (item) al final de la lista
lista.append("soy el nuevo elemento")

#El siguiente metodo agrega un elemento a la lista con ayuda de dos parametros, el primero sera el numero de la posición en donde queremos el nuevo elemento de la lista y el segundo el elemento a añadir.
lista.insert(3,"elemento agregado en donde quise")

print("insert & append: ", lista)

#el siguiente metodo nos sirve para pasar elementos al final de la lista, sin necesidad de limite, es importante añadir los corchetes seguidos del parentesis ya que asi indicaremos que lo que queremos agregar, es una lista
lista.extend(["ya","me quiero","ir",56,48,5])
print("extend:  ",lista)

#pop que al lado contrario de lo que estamos haciendo, vamos a eliminar
#Eliminando así al elemento por su indice
lista.pop(3)
print("pop: ",lista)

#remove nos permite remover una cadena de carcateres especificos por ejemplo
lista.remove("me quiero")
print("remove: ",lista)

#sort que nos sirve para acomodar la lista de forma ascendente si la lista esta desordenada con sort la podemos acomodar de forma ascendente, hay una manera de solo voltear la lista y eso es con la ayuda del parametro propio del metodo el cual se llama "reverse=true", sin este la forma de trabajar del metodo es de forma ascendente
lista_numerica.sort()
print(lista_numerica)

#El siguiente metodo nos sirve para hacer precisamente eso que hacem,os con el parametro de sort pero como metodo funciona excatamente igual
#una ves acomodada la lista con sort, podemos revertirla con este metodo
lista_numerica.reverse()
print(lista_numerica)
#clear nos permite eliminar a todos los elementos de la lista
lista.clear()
print("clear: ", lista)
