__author__ = 'Steeven Villa'

import cv2 as v
import numpy as np

def dividir(imagen):
    alto = len(imagen)
    ancho = len(imagen[0])
    return [imagen[:alto/2, :ancho/2], imagen[:alto/2, ancho/2:], imagen[alto/2:, :ancho/2], imagen[alto/2:, ancho/2:]]

imagen = v.imread('mosca.png',0)

laplace = v.Laplacian(imagen, v.CV_16S)
laplace = v.convertScaleAbs(laplace)

im1 = dividir(laplace)
out = [dividir(i) for i in im1]


for i in range(4):
    for j in range(4):
        print i, j, np.mean(out[i][j])
        if np.mean(out[i][j])>10:
            v.imshow(str(i)+str(j), out[i][j])

v.imshow('2', laplace)
#v.imshow('1', imagen)
v.waitKey()