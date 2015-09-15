__author__ = 'Xteeven'

import numpy as np

numero=0
Datos = np.loadtxt('Datatxt/dataset'+str(numero)+'.txt', delimiter=',')

def maximo(mat ,column=0):
    max=0
    for i in range(len(mat)):
        max = mat[i][column] if max < mat[i][column] else max
    return max

for i in range(len(Datos[0])-1):
    for j in range(len(Datos)):
        Datos[j][i] = Datos[j][i]/maximo(Datos, i)


datas = open(str(numero)+".txt", "w")
for j in range(len(Datos)):
    for i in range(len(Datos[0])):

        datas.write(str(Datos[j][i])+',')
    datas.write("\n")