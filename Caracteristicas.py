__author__ = 'Xteeven'


import cv2 as v
import numpy as np

imagen = v.imread('1.jpg',0)

#convolucion con kernel de laplace energy  segun Wei Huang, Zhongliang Jing
energy = v.filter2D(imagen, -1, np.asarray(([-1,-4,-1],[-4,20,-4],[-1,-4,-1])))
#v.imshow('2',energy**2)
#print sum(sum(energy**2))

#definicion: aplicada punto a punto  segun Wei Huang, Zhongliang Jing
def eol(imagen):
    sumenergy = 0
    imagen = v.copyMakeBorder(imagen, 1, 1, 1, 1, v.BORDER_CONSTANT)
    for x in range(1, len(imagen[0])-1):
        for y in range(1, len(imagen)-1):
            fxxfyy = 20*imagen[y][x]-imagen[y-1][x-1]-imagen[y+1][x+1]-imagen[y+1][x-1]-imagen[y-1][x+1]-4*imagen[y-1][x]-4*imagen[y+1][x]-4*imagen[y][x-1]-4*imagen[y][x+1]
            sumenergy += fxxfyy**2
    return sumenergy

#definicion 2: partiendo del histograma segun Carlos Platero.
def eol2(imagen):
    sumenergy = 0
    laplace = v.Laplacian(imagen, v.CV_16S)
    laplace = v.convertScaleAbs(laplace)
    histograma = v.calcHist(laplace, [0], None, [256], [0, 256])
    p = histograma/(len(imagen[0])*len(imagen))
    for i in range(len(p)):
        sumenergy += p[i]**2
    return sumenergy
#print eol(imagen)
#print eol2(imagen)

#Suma laplaciano modificado segun Wei Huang, Zhongliang Jing
def sml(imagen, border=1):
    sumlaplacian = 0
    imagen = v.copyMakeBorder(imagen, border, border, border, border, v.BORDER_CONSTANT)
    for x in range(border, len(imagen[0])-border):
        for y in range(border, len(imagen)-border):
            modified = abs(2*imagen[y][x]-imagen[y][x-border]-imagen[y][x+border])+abs(2*imagen[y][x]-imagen[y-border][x]-imagen[y+border][x])
            sumlaplacian += modified
    return sumlaplacian
#print sml(imagen)


def eog(imagen):
    sumgradient = 0
    imagen = v.copyMakeBorder(imagen, 1, 1, 1, 1, v.BORDER_CONSTANT)
    for x in range(1, len(imagen[0])-1):
        for y in range(1, len(imagen)-1):
            fx = imagen[y][x+1]-imagen[y][x]
            fy = imagen[y+1][x]-imagen[y][x]
            sumgradient += fx**2+fy**2
    return sumgradient

print eog(imagen)

v.waitKey()