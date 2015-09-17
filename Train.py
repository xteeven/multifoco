__author__ = 'Xteeven'

import numpy as np
import mlpy
import matplotlib.pyplot as plt
import time

datos = np.loadtxt('final.csv', delimiter=';')
x, y = datos[:,:8], datos[:,8].astype(np.int)
#0 =A
#1 =B
#2 =INDEFINIDO

# x = x - np.mean(x, axis=0)
xn = x / np.sqrt(np.sum(x**2, axis=0))





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



# Classification Tree
# tree = mlpy.ClassTree(stumps=0,minsize=1)
# tree.learn(xn,y)
# a = [(tree.pred(xn[i])) == y[i] for i in range(len(y))]
# print float(sum(a))/float(len(y)), a


# Maximum likelihood Classifier
# #
# mlc = mlpy.MaximumLikelihoodC()
#
# mlc.learn(x, y)
#
# a = [(mlc.pred(xn[i])) == y[i] for i in range(len(y))]
# print float(sum(a))/float(len(y)), a

#
# valor = []
# plt.ion()
plt.show()
# for val in np.arange(0.00001,1,0.0001):
#
#     vector = mlpy.LibSvm(svm_type='nu_svc', kernel_type='rbf', gamma=9 , C=10)
#     vector.learn(xn,y)
#     a = [(vector.pred(xn[i])) == y[i] for i in range(len(y))]
#     print float(sum(a))/float(len(y))
#     valor.append(float(sum(a))/float(len(y)))
#     plt.plot(valor)
#     plt.draw()
#     time.sleep(0.000001)


# Cross-Validation

kfold = mlpy.cv_kfold(len(xn), len(xn))
#
#
# percent = []
# rango = np.arange(0, 3.1, 0.1) #delta 1 - 70%
# for var in rango:
#     result = []
#     classifier = mlpy.DLDA(delta=var)
#     for crossval in range(len(kfold)):
#         trainindex = kfold[crossval][0].tolist()
#         evaluateindex = kfold[crossval][1].tolist()
#         trainx = xn[trainindex]
#         trainy = y[trainindex]
#         evaluatex = xn[evaluateindex]
#         evaluatey = y[evaluateindex]
#
#         classifier.learn(trainx, trainy)
#         result.append(classifier.pred(evaluatex) == evaluatey)
#     percent.append(float(sum(result))/float(len(result)))
# plt.plot(rango, np.asarray(percent)*100)
# plt.title("DLDA (Lineal)")
# plt.xlabel("delta")
# plt.ylabel("Cross-Validation Result")
# plt.show()



# percent = []
# rango = range(1, 50)
# for var in rango:
#     result = []
#     classifier = mlpy.KNN(k=var)
#     for crossval in range(len(kfold)):
#         trainindex = kfold[crossval][0].tolist()
#         evaluateindex = kfold[crossval][1].tolist()
#         trainx = xn[trainindex]
#         trainy = y[trainindex]
#         evaluatex = xn[evaluateindex]
#         evaluatey = y[evaluateindex]
#         classifier.learn(trainx, trainy)
#         result.append(classifier.pred(evaluatex) == evaluatey)
#     percent.append(float(sum(result))/float(len(result)))
#
# plt.plot(rango, np.asarray(percent)*100)
# plt.title("KNN")
# plt.xlabel("k")
# plt.ylabel("Cross-Validation Result")
# print [rango, percent]

#
# percent = [] #0.782258064516129 best
# rango = np.arange(0, .0002,0.00005)
# for var in rango:
#     result = []
#     classifier = mlpy.ClassTree(stumps=0,minsize=0)
#     for crossval in range(len(kfold)):
#         trainindex = kfold[crossval][0].tolist()
#         evaluateindex = kfold[crossval][1].tolist()
#         trainx = xn[trainindex]
#         trainy = y[trainindex]
#         evaluatex = xn[evaluateindex]
#         evaluatey = y[evaluateindex]
#         classifier.learn(trainx, trainy)
#         result.append(classifier.pred(evaluatex) == evaluatey)
#     percent.append(float(sum(result))/float(len(result)))
#
# plt.plot(rango, np.asarray(percent)*100)
# plt.title("Clas-tree")
# plt.xlabel("Minsize")
# plt.ylabel("Cross-Validation Result")
# print [rango, percent]

# percent = []
# rango = np.arange(0, 1, 0.3) #gamma = 900 - 7842741935483871
# for var in rango:
#     itera=time.clock()
#     result = []
#     classifier = mlpy.LibSvm(svm_type='nu_svc', kernel_type='rbf', gamma=var , C=1)
#     for crossval in range(len(kfold)):
#         trainindex = kfold[crossval][0].tolist()
#         evaluateindex = kfold[crossval][1].tolist()
#         trainx = xn[trainindex]
#         trainy = y[trainindex]
#         evaluatex = xn[evaluateindex]
#         evaluatey = y[evaluateindex]
#         classifier.learn(trainx, trainy)
#         result.append(classifier.pred(evaluatex) == evaluatey)
#     print time.clock()-itera
#     percent.append(float(sum(result))/float(len(result)))
#
# plt.plot(rango, np.asarray(percent)*100)
# plt.title("SVM")
# plt.xlabel("gamma")
# plt.ylabel("Cross-Validation Result")
# print [rango, percent]

plt.show()