#para poder importar unicamente una función de un modulo en particular podremos usar la palabra reservada "from" para hacer referencia desde que modulo se quiere obtener la funcion
from crear_funciones import crear_contraseña_random as pswd_random

psw,numero_usado= pswd_random(9)
print(f'tu contraseña es: {psw} y el numero usado para crearla fue {numero_usado}')