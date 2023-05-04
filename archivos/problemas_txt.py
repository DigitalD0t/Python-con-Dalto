#Vamos a crear un archivo txt desde cero con las llaves y claves correspondientes 
#2 listas, una con nombres otra con apellidos
nombres = ["brandon","paul", "mauricio","juan"]
apellidos = ["moreno","moreno","mercedez","benitez"]

#registrar estar información en un TXT de forna óptima
with open("nombres_apellidos.txt", "w") as arch:
	arch.writelines("los datos son: \n")
	[arch.writelines(f'Nombre:{n}\nApellidos:{a}\n-----------------------\n') for n,a in zip(nombres,apellidos)]
