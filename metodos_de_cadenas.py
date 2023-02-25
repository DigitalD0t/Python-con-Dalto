cadena1 = "este es mi nuevo texto para la siguiente cadena "
cadena2 = "Ahora no veo nada malo por aca"

#El siguiente metodo nos sirve para verificar si la cadena comienza con el caracter propircionado dentro de los parentesis
empieza_con = cadena1.startswith("m")
print(empieza_con)

#verificamos si la cadena termina con el caracter especifico dentro de los parentesis, esto quiere decir toda la cadena no la palabra al igual que starts
termina_con = cadena2.endswith("ca")
print(termina_con)

#El siguiente método reemplaza el texto por el texto citado en los parentesis, este a diferencia de los demás trabaja con dos parametros, el primero es el texto que será reemplazado, el cuál el segundo parametro es el texto reemplazante
remplaza = cadena2.replace("nada","todo esta")
print(remplaza)

#Este metodo nos permite separar los caracteres por medio del caracter proporcionado...
agrega = cadena1.split(":")
print(agrega)