__author__ = 'Steeven Villa'

import cv2 as v
import numpy as np

def dividir(imagen):
    alto = len(imagen)
    ancho = len(imagen[0])
    return [imagen[:alto/2, :ancho/2], imagen[:alto/2, ancho/2:], imagen[alto/2:, :ancho/2], imagen[alto/2:, ancho/2:]]

imagen = v.imread('b_bigbug0004_croppped.png',0)

laplace = v.Laplacian(imagen, v.CV_16S)
laplace = v.convertScaleAbs(laplace)

im1 = dividir(laplace)
out = [dividir(i) for i in im1]
print np.mean(out[0][0])

for i in range(4):
    for j in range(4):
        print i, j, np.mean(out[i][j])

v.imshow('2', laplace)
#v.imshow('1', imagen)
v.waitKey()