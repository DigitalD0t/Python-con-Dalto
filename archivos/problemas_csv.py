#cambia el tipo de dato de una columna
#importamos la libreria pandas y la asignamos a una variable más corta
import pandas as pd
df = pd.read_csv("readcsv1.csv")

#convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str)

#verificamos el dato cambiado anteriormente, con el primer elemento de la columna edad
print(type(df['edad'][0]))

#se reemplazan los datos "brandon" por "maestro"
df['apellido'].replace("moreno","maestro", inplace=True)

#se eliminan los datos faltantes de las filas si llegasemos a capturar datos incompletos 
print(df)
df= df.dropna()
print(df)

#se eliminarán las columnas repetidas si hubiese 
df = df.drop_duplicates()
print(df)

#guardar el nuevo archivo con las modificaciones 
df.to_csv("datoslimpios.csv")