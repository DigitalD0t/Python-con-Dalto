#la diferencia entre el for y el while es que mientras el for recorre la lista o diccionarios para imprimir los elementos, el while se va a ejecutar siempre y cuando la sentencia ejecutada sea igual a true (==true) siendo así que su ejecución sea infinita, veamos el siguiente ejemplo

num = 1
while num<5:
	print(f'En esta sentencia se ejecutara while hasta que llegue al numero 5 llegando a este numero dejará de ejecutarse la sentencia while {num}')
	num += 1

contador = 0 
while contador < 10:
	contador += 1
	print(contador)