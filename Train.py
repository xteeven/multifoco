__author__ = 'Xteeven'

import numpy as np
import mlpy
import matplotlib.pyplot as plt


datos = np.loadtxt('final.csv', delimiter=';')
x, y = datos[:,:8], datos[:,8].astype(np.int)
#0 =A
#1 =B
#2 =INDEFINIDO


def normalizar(vector):
    total = []
    for i in range(len(vector.T)):
        total.append(vector.T[i]/np.linalg.norm(vector.T[i]))
    return np.array(total).T
xn = normalizar(x)

## Delta
# delta = mlpy.DLDA(delta=1.5)
# delta.learn(xn, y)
# a =  [(delta.pred(xn[i]))==y[i] for i in range(len(y))]
# print float(sum(a))/float(len(y)), a

# # Knn
# Knn = mlpy.KNN(k=3)
# Knn.learn(xn,y)
# a = [(Knn.pred(xn[i])) == y[i] for i in range(len(y))]
# print float(sum(a))/float(len(y)), a

# Parzen-based classifier


# Classification Tree
# tree = mlpy.ClassTree(stumps=0,minsize=1)
# tree.learn(xn,y)
# a = [(tree.pred(xn[i])) == y[i] for i in range(len(y))]
# print float(sum(a))/float(len(y)), a


# Maximum likelihood Classifier
#
# mlc = mlpy.MaximumLikelihoodC()
#
# mlc.learn(x, y)
#
# a = [(mlc.pred(xn[i])) == y[i] for i in range(len(y))]
# print float(sum(a))/float(len(y)), a
