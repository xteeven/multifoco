__author__ = 'vaf'

import cv2 as v
import numpy as np

def dividir(imagen, rows=2,cols=2):
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




imagen = v.imread('mosca.png',0)
cut = dividir(imagen)


v.waitKey()

