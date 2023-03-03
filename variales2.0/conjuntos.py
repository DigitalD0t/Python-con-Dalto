#creando conjtos con set()
conjunto = set(["dato 1 "])

#metiendfo un conjunto dentro de otro conjunto
conjunto1= frozenset(["dato 1","dato 2"])
conjunto2 = {conjunto1, "dato3"}
print(conjunto2)

#teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado2 = conjunto2 <= conjunto1

#verificando si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado3 = conjunto1 > conjunto2

#verifiamos si hay algun numero en comun, cuando haya un elemento que concida este dará false, porque mismo se esta preguntando si hay un elemento distintivo o no por lo cual ene ste ejemplo dará false ya que los numeros son los mismos e el conjunto 1 como en el 2
resultado4 = conjunto2.isdisjoint(conjunto1)
print(resultado4)