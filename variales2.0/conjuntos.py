#creando conjuntos con la función set(), los conjuntos no se pueden modificar, sirven par almacenar datos inmutables.
conjunto = set(["dato 1 "])
print(f'Creando conjunto con la función set() {conjunto}')

#metiendo un conjunto dentro de otro conjunto
conjunto1= frozenset(["dato 1","dato 2"])
conjunto2 = {conjunto1, "dato3"}
print(f'Agregamos un conjunto dentro de otro conjunto con la función frozenset() {conjunto2}')

#teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado2 = conjunto2 <= conjunto1
print(f'La siguiente función es para verificar con los nuevos valores de conjunto 1 y 2 uno es subconjunto del otro con el cual nos va a servir la función issubset() y dento de los parentesis el conjunto por el que se quiere validar {resultado}')

#verificando si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado3 = conjunto1 > conjunto2
print(f'Con esta función verificamos si es un super conjunto {resultado}')

#verifiamos si hay algun numero en comun, cuando haya un elemento que concida este dará false, porque mismo se esta preguntando si hay un elemento distintivo o no por lo cual ene ste ejemplo dará false ya que los numeros son los mismos e el conjunto 1 como en el 2
resultado4 = conjunto2.isdisjoint(conjunto1)
print(f'Verificamos con la función isdisjoint() si es un conjunto2 está unido a conjunto1 {resultado4}')