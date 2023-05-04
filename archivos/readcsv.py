#Libreria para leer archivos csv la cual no es muy recomendada encambio, se puede usar la liberia panda
import csv

with open("readcsv.csv") as archivo:
	reader = csv.reader(archivo)
	for row in reader:
		print(f'leyendo con csv: \n{row}')

import pandas as pd

#al realizar la lectura con esta librería nos facilitara la lectura ya que lo leera como una hoja de excel

archivo2 = pd.read_csv("readcsv.csv")
print(f'leyendo archivo con libreria pandas:\n {archivo2}')

#para agregar encabezado a las columnas por demio de la lectura de archivos lo podemos hacer con la funcion read_csv(), usando (names=["name","lastname","age"]) como segundo parametro de la libreria pandas
df = pd.read_csv("readcsv.csv", )#sin esto definido en el archivo de lectura anteriormente toma los primeros 3 objetos como el encabezado

#obteniendo los datos de la columna nombre
nombres = df["nombre"]
#print(f'mostramos la tabla con el encabezado:\n {df}')
print(f'mostramos únicamene la columna "nombre": \n {nombres}')

#ordenando el dataframe (df) por la edad
df_orden_ascendente = df.sort_values("edad")
print(f'Ordenando en modo ascendente: \n {df_orden_ascendente}')

#ordenando el dataframe en descendente
df_orden_descendente = df.sort_values("edad", ascending=False)
print(f'ordenando la lista en modo descendente: \n {df_orden_descendente}')


df2 = pd.read_csv("readcsv.csv", )
#Concatenando dos o más dataframes, con la función concat la cual nos solicita 1 parametro en forma de lista []. Dentro de la lista los dataframe requeridos o necesitados a unir 
df_concatenado =pd.concat([df,df2])
print(f'Contatenando dos o más dataframnes:\n {df_concatenado}')

#Usando head() para mostrar filas 1,2,3, etc, ejemplo, si no se define nada dentro de head este no mostrara ningún dato, el número que se ingrese como parametro serán números de fila, no posición 
filas = df.head(2)
print(f'Mostrando filas para lectura, con función head():\n {filas}')

#con la siguiente función podremos acceder pero a las ultimas filas de igualmanera que con head(), pero con tail() de manera inversa
filas = df.tail(2)
print(f'Mostrando las últimas 5 filas del dataframe con tail():\n {filas}')

#accediendo a la cantidad de filas y columnas con shape
filas_totales, columnas_totales = df.shape
print(f'Estas son las filas totales:\n {filas_totales} \n y estas son las columnas totales:\n {columnas_totales}')

#obteniendo data estadística del dataframe con describe()
df_info = df.describe()
print(f'Información del dataframe:\n {df_info}')

#usando loc, para ser más especificos que con el anterior ya que este únicamente mostrará en la lectura el elemento deseado, con la ayuda de loc lograremos hacer esto, esta función necesitas 2 parametros uno que indica la posición del elemento a desear y el segundo de que columna 
select_elem = df.loc[2,"edad"]
print(f'Seleccionando un elemento en especifico gracias a loc en este caso de la columna edad:\n {select_elem}')

#Accediendo a la edad de la fila 2 con iloc
select_elem = df.iloc[2,2]
print(f'Seleccionando la edad de la fila 2 con iloc[]:\n {select_elem}')

#Accediedno a todos los apellidos de una columna
apellidos = df_concatenado.loc[:,"apellido"]#donde ":" es igual a todo, osea que mostrara toooodos los elementos del segunto argumento
print(apellidos)

#Accediendo a todas los apellidos de una columna usando iloc[]
apellidos = df_concatenado.iloc[:,1]#Donde :es igualmente a todo, y 1 a la columna deseada 
print(f'Mostrando lo mismo de arriba pero con iloc[]:\n {apellidos}')
print('la unica diferencia ente loc e iloc es que en el segundo argumento deseado con loc tenemos que especificar con el nombre del encabezado de la columna, encambio iloc solo basta con poner la posición del elemento requerido.')

#accedemos a la fila de todos los componentes
apellidos = df_concatenado.iloc[3,:]
print(apellidos)