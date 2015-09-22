__author__ = 'root'

import numpy as np
import mlpy
import matplotlib.pyplot as plt
datos = np.loadtxt('final.csv', delimiter=';')
x, y = datos[:,:8], datos[:,8].astype(np.int)
#0 =A
#1 =B
#2 =INDEFINIDO

# x = x - np.mean(x, axis=0)
xn = x / np.sqrt(np.sum(x**2, axis=0))



vector = mlpy.LibSvm(svm_type='nu_svc', kernel_type='rbf', gamma=900 , C=1)
vector.learn(xn,y)
xf = vector.pred(xn)
matriz = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(y)):
    matriz[(y[i])][int(xf[i])] += 1.0
print "     E,   NE,     ND"
print np.asarray(matriz)

