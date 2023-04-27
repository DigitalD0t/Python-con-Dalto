#Recordemos que los modulos son los archivos con extensión ".py"
#teniendo esto en claro continuemos, para ver como importar o crear enlaces entre estos archivos (modulos)
#para poder reutilizar codigo de otro modulo sin necesidad de reescribir unicamente con la palabra reservada por python "import" podremos hacer uso del archivo sin ningun problema, recordando que los modulos a importan deberan de estar en la misma carpeta (ruta) para poder usar import en su forma más simple
import crear_funciones

resultado = crear_funciones.saludar("Bradnon","hombre")
print(resultado)