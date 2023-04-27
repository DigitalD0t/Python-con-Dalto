#si el modulo estuviera en una carpeta afuera de la ruta misma se usa la palabra reservada "sys"
import sys 
sys.path.append("'/home/an0n8693/Documentos/Knowledge/Python-con-Dalto/funciones'")
from crear_funciones import saludar as salut
hi = salut("Bradnon","hombre")
print(hi)