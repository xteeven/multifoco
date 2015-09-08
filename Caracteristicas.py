__author__ = 'Xteeven'


import cv2 as v
import numpy as np
import time

imagen = v.imread('1.jpg',0)

#convolucion con kernel de laplace energy  segun Wei Huang, Zhongliang Jing

#v.imshow('2',energy)

def eolaplace(image):
    energy = v.filter2D(image, -1, np.asarray(([-1,-4,-1],[-4,20,-4],[-1,-4,-1])))
    return sum(sum(energy**2))*1.0/((len(image))*(len(image[0])))*1.0

def eol(imagen):
    sumenergy = 0
    imagen = v.copyMakeBorder(imagen, 1, 1, 1, 1, v.BORDER_CONSTANT)
    for x in range(1, len(imagen[0])-1):
        for y in range(1, len(imagen)-1):
            fxxfyy = 20L*imagen[y][x]-imagen[y-1][x-1]-imagen[y+1][x+1]-imagen[y+1][x-1]-imagen[y-1][x+1]-4*imagen[y-1][x]-4*imagen[y+1][x]-4*imagen[y][x-1]-4*imagen[y][x+1]
            sumenergy += fxxfyy**2
    return sumenergy/((len(imagen)-1)*(len(imagen[0])-1))

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

#Suma laplaciano modificado segun Wei Huang, Zhongliang Jing
def smlaplacian(imagen, border=1):
    sumlaplacian = 0
    imagen = v.copyMakeBorder(imagen, border, border, border, border, v.BORDER_CONSTANT)
    for x in range(border, len(imagen[0])-border):
        for y in range(border, len(imagen)-border):
            modified = abs(2*imagen[y][x]-imagen[y][x-border]-imagen[y][x+border])+abs(2*imagen[y][x]-imagen[y-border][x]-imagen[y+border][x])*1L
            sumlaplacian += modified
    return sumlaplacian/((len(imagen)-1)*(len(imagen[0])-1))*1.0



def eogradient(imagen):
    sumgradient = 0
    imagen = v.copyMakeBorder(imagen, 1, 1, 1, 1, v.BORDER_CONSTANT)
    for x in range(1, len(imagen[0])-1):
        for y in range(1, len(imagen)-1):
            fx = imagen[y][x+1]*1L-imagen[y][x]*1L
            fy = imagen[y+1][x]*1L-imagen[y][x]*1L
            sumgradient += fx**2+fy**2
    return sumgradient/((len(imagen)-1)*(len(imagen[0])-1))*1.0


v.waitKey()