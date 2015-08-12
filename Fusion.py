__author__ = 'Steeven Villa'

import cv2 as v
import numpy as np

def dividir(imagen, rows=4,cols=4):
    ancho = len(imagen)*1.0
    alto = len(imagen[0])*1.0
    cortes = []
    total = []
    for i in range(rows):
        for j in range(cols):
            posx = lambda pos, num: round((pos*1.0+num)/(rows)*ancho)
            posy = lambda pos, num: round((pos*1.0+num)/(cols)*alto)
            out = imagen[posx(i, 0):posx(i, 1), posy(j, 0):posy(j, 1)]
            cortes.append(out)
        total.append(cortes)
        cortes = []
    return total

def promedio(out):
    prom = 0
    for i in range(len(out)):
        for j in range(len(out[0])):
            prom += np.mean(out[i][j])/(len(out)*len(out[0]))
    return prom

def isfocus(out, promed = 0):
    salida = []
    fila = []
    for i in range(len(out)):
        for j in range(len(out[0])):
            if np.mean(out[i][j])>promed:
                fila.append(1)
            else:
                fila.append(0)
        salida.append(fila)
        fila=[]
    print np.asarray(salida)


imagen = v.imread('mosca.png',0)
laplace = v.Laplacian(imagen, v.CV_16S)
laplace = v.convertScaleAbs(laplace)

out = dividir(laplace, 20, 37)
prom = promedio(out)
isfocus(out,prom)




v.imshow('2', laplace)

v.waitKey()