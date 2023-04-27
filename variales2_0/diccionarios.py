#Creando Diccionario con la función dict()
diccionario = dict(nombre="Brandon",apellido="Moreno")
print(f'Los valores del diccionario son: {diccionario}')

#Las listas no pueden ser claves y usamos frozenset para meter conjuntos.
diccionario = {frozenset(["brandon","hermoso"]): "vetegd<flh"}
print(f'las listas no pueden ser llaves, pero usamos la función frozenset() para agregarlos: \n {diccionario}')

#Creando diccionarios con fromkeys(), con esta función creamos diccionarios con valores vacios por defecto.
diccionario = dict.fromkeys(["nombre","apellido"])
#el primer parametro es por lo que se va a iterar veamos...
print(f'Creamos el diccionario con los valores vacios como none: {diccionario}')
diccionario = dict.fromkeys(["nombre","apellido"],"no sé")
print(f'Aquí modificamos el valor por defecto de none por no sé {diccionario}')
