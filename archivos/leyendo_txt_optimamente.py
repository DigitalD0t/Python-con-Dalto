with open("readme.txt"): #esto únicamente para abrir y cerrar el archivo para no estar olvidando cerrarlo
	print("listo!") #indicamos que ya esta abierto y cerrado


with open("readme.txt") as archivo:
	print(archivo.read()) #Leemos el archivo

#implementando esta forma con with, evitamos cerrar el archivo, y la aplicacion gastaría menos recursos

#con la funcion write lo que haríamos con el archivo es sobreescribir en el no agregar nuevas lineas de texto para ello tenemos la función writelines
with open("readme.txt",'w') as archivo:
	archivo.write("Este es el nuevo texto desde python")

#con writelines al agregar el texto lo haremos en forma de lista, esto quiere indicar que cada objeto será tratado como una línea neva del texto, miremos el ejemplo
with open("readme.txt",'w') as writting:
	writting.writelines(["Hola yo soy una ueva linea agregada con la función writelines desde python \n", "Y yo soy otra línea agregada con la anterior para ver mejor el ejemplo.\n"])
	writting.writelines(["Agregamos otras 2 líneas al archivo \n","Y a me gusto esto :)\n"])

#para poder agregar texto sin tener que sobreescribir el archivo como lo hace write podremos usar la función de append (a), es lo mismo que write (w) pero sin reescribir el archivo
with open("readme.txt",'a') as addingtext:
	addingtext.write("Soy el nuevo texto agregado, quiere decir que no eliminarpe nada de lo anteriormente escrito, tchao")
