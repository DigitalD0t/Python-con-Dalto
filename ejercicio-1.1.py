#En este ejercicio lo que vamos a hacer es sacar el promedio de la duraci´´on del video del curso de dalto a comparación de otros con tiempo minimo maximo y promedio de enseñanza, comenzando por declarar las variables y a definirlas con sus valores, respectivamente.....:

#Promedio de la duración
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
curso_dalto = 1.5

#Diferencias de duración, aun que el resultado para que sea exacto deberíamos ponerlo de la siguiente manera 
diferencias_con_min = 100 - curso_dalto / otros_cursos_min *100
print(f'El curso de dalto dura un {diferencias_con_min}% menos que el más rápido')

diferencia_con_max = 100 - curso_dalto * 1000 // otros_cursos_max / 10
print(f'El curso de Dalto dura un {diferencia_con_max}% menos que el más lento')

diferencia_con_promedio = 100 - curso_dalto / otros_cursos_promedio * 100
print(f'El curso de dalto dura un {diferencia_con_promedio}% menos que el promedio')

#Duración de crudos (osea sin editar)
crudo_promedio = 5
crudo_dalto = 3.5

#Calculando el porcentaje de tiempo vacio removido
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - curso_dalto * 1000 // crudo_dalto / 10
print(f'Un curso en promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'Este curso eliminó un {tiempo_vacio_dalto}% de sus videos')

#Mostramos diferencias si los cursos duraran 10 horas
print(f'Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // curso_dalto / 10} horas de otros cursos')
print(f'Ver 10 horas de otros cursos equivale a ver {curso_dalto *100 // otros_cursos_promedio / 10} horas de este curso')