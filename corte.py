__author__ = 'vaf'

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


def unir1(IMG):
    fila=[]
    out = []

    for k in range(len(IMG)):
        for i in range(0, len(IMG[0][0])-1):
            fila = IMG[k][0][i]
            out.append(np.array(fila, dtype=np.uint8))
    return out


def unir(IMG):
    fila=[]
    out = []
    flag = 0
    try:
        IMG[len(IMG)][len(IMG)][len(IMG[0][0])].tolist()
    except:
        flag = 1
    for k in range(len(IMG)):
        for i in range(len(IMG[0][0])-flag):
            for f in range(len(IMG)):
                fila += IMG[k][f][i].tolist()
            out.append(np.array(fila, dtype=np.uint8))
            fila = []
    return out


v.waitKey()

