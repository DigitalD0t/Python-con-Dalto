import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("pedos.csv")#se carga el documento

sns.lineplot(x="fecha",y="pedos",data=df)#damos los valores de los parametros solicitados por la libreria seaborn en la función lineplot()

plt.plot("01-09",17,"o")#marcando el punto máximo de la gráfica

plt.show()#mostramos la grafica 