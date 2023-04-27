#en caso de tener un modulo con un nombre demasiado extenso python cuenta con una carcateristica para cambiar el nomre del modulo importado, esto se logra con la palabra reservada "as", as no solo sirve para acortar los nombre de los odulos sino de cualquier otro objeto importado
import crear_funciones as cf

resultado = cf.saludar("Juana","no hay genero")
print(resultado)