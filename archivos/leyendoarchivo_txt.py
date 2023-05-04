#en este apartado vamos a comenzar a leer archivos en este caso usaremos la extensión .txt
#un archivo se puede manipular con las funciones de python las cuales son:
#open()
#read()
#write()
#close()
#este último es indispensable cuando se abre, lee, o edita el archivo, sin esta función el archivo se dañaría, ya que nunca se cerra a lo que no guarda la información 

abriendo_archivo = open('readme.txt')
leyendo_archivo = abriendo_archivo.read()
abriendo_archivo.close()
print(leyendo_archivo)

#la función readline y readlines sirve únicamente para especificar leer ciertas lineas, solo que readline lee de caracter en caracter 
