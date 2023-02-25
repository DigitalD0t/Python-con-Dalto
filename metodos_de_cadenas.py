cadena1 = "me pasas la mantequilla por favor?"
cadena2 = "Si me fuera de tu vida que harías. Nada..."

#Encuentra la cadena de caracterec especificada dentro del parentesis
busqueda_find= cadena1.find("m")
print(busqueda_find)

#Convierte toda la cadena de caracetres a mayusculas
mayusculas_uppercase = cadena2.upper()
print(mayusculas_uppercase)

#convierte toda la cadena de caracteres a minusculas
minusculas_lowercase = cadena2.lower()
print(minusculas_lowercase)

#Muestra la posicion del caracter mensionado dentrod e los parentesis
posicion_index = cadena1.index("f")
print(posicion_index)

#Indica si el valor de la cadena de caracteres es númerico o no, no importa que éste este dentro de la cadena de caracteres, por obvio mostrara falso ya que en la cadena 1 solo hay caracteres de tipo string y no numerico
esnumerico_isnumeric = cadena1.isnumeric()
print(esnumerico_isnumeric)

#Este metodo indicara si el valor es alfanumerico, por lo cual dara false ya que es una cadena de caracteres tampoco importa si el valor alfanumerico esta dentro de una cadena de caracteres, si hubiera mostraria verdadero
esalfa_isalpha = cadena2.isalpha()
print(esalfa_isalpha)

#Mostrará el número de veces que se repite el caracter dentro de la cadena
cuenta_carcater_count = cadena1.count("a")
print(cuenta_carcater_count)

#Esta función nos permitira saber la longitud que tiene una cadena o mejor entendido cuantos caracteres tiene una cadena, contando los espacios
longitud_len = len(cadena2)
print(longitud_len)

#Verificamos si una la cadena comienza con el caracter proporcionado con el metodo
comienza_con = cadena2.startswith("h")
print(comienza_con)

#lo contrario a startswith con el metodo
termina_con = cadena1.endswith("o")
print(termina_con)

#El siguiente metodo nos sirve para reemplazar la cadena de textos por la que queramos, teniendo en cuenta que este metodo contiene 2 parametros, el primero es la cadena a reemplazar y el segundo la cadena por la cual se va a reemplazar, siempre y cuando exista la concidencia dentro de la cadena de caracteres
remplaza = cadena2.replace("Nada", "Llorar")
print(remplaza)

#el siguiente metodo nos separa la cadena convirtiendola en una lista (arreglo), la separasión se crea apartir del caracter proporcionado en los parentesis, es dedcir en el siguiente ejemplo la separación comenzara aparter de la letra "a" que se encuentre en cada palabra de la cadena
cadena_separada = cadena1.split("a")
print(cadena_separada)
