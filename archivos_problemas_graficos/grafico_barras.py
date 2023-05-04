import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns #con esta libreria se dan a conocer los datos para con pyplot mostrar el gráfico

df = pd.read_csv("cofla_ingresos.csv")

#se crea el grafico
sns.barplot(x="fuente",y="ingresos",data=df)#siempre se deberan de definir 3 parametros 1; equivale al primer punto de referencia, el 2; equivale al porcentaje del punto de referencia y por ultimo, los datos.

total_ingresos = df['ingresos'].sum()

print(f'ingresos totales al mes es de: {total_ingresos}')
 
#Se muestra el gráfico
plt.show()