#7.	Crear arreglo de 5x4 con valores del 1-20
import numpy as np

x = np.arange(21)
f1 = x[1:5]
f2 = x[5:9]
f3 = x[9:13]
f4 = x[13:17]
f5 = x[17:21]

arreglo1 = np.array([f1,f2,f3,f4,f5])
print(arreglo1)

#Llenar un arreglo de 3x3 de los valores q corresponden
#de la fila 3,4 y 5 y la de la columna 1,2,3

arreglo2 = np.array([f3[0:3],f4[0:3],f5[0:3]])
print("Este es el arreglo de 3x3:")
print(arreglo2)

#Crear un arreglo con la misma forma que el anterior ¿? 

arreglo3 = np.empty_like(arreglo2)
for i in range(3):
    arreglo3[i,:]=arreglo2[i,:]+1
print("Nuevo arreglo", arreglo3)
