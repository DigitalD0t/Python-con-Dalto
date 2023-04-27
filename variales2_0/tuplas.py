#Creando tuplas con la función tuple()
tupla = tuple(["dato1","dato2"])#el unico dato que debe de contener en su interior es la lista que se convertira en tupla
print(f'Creando listas con el metodo tuple() {tupla}')

#redefinimos la tupla, para crear una tupla sin parentesis
tupla = "dato1", "dato2"
print(f'Creando listas sin parentesis {tupla}')

#de la siguiente manera se crea una tupla con solo un dato, es importante colocar la coma como se muestra ya que sin esta python la reconocería como una variable común de string.
tupla= "dato1",

print(f'Creando listas sin parentesis y con un solo dato {tupla}')