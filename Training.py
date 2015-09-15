__author__ = 'Steeven'

import mlpy
import numpy as np
import matplotlib.pyplot as plt

iris = np.loadtxt('iris.csv', delimiter=',')
#print iris
x, y = iris[:, :4], iris[:, 4].astype(np.int)

print x, y