__author__ = 'Xteeven'

import numpy as np
import mlpy
import matplotlib.pyplot as plt

datos = np.loadtxt('final.csv', delimiter=';')
x, y = datos[:,:8], datos[:,8].astype(np.int)
#0 =A
#1 =B
#2 =INDEFINIDO
print x

pca = mlpy.PCA()
pca.learn(x)
z= pca.transform(x, k=2)
#plt.set_cmap(plt.cm.Paired)
plot = plt.scatter(z[:,0],z[:,1],c=y)
plt.show()
# mysvm = mlpy.LibSvm()
# mysvm.learn(x,y)
# print mysvm.pred(x[15])
