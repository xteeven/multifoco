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


def unir(IMG):
    out = np.hstack(np.hstack(IMG).tolist()).astype(np.uint8)
    return out




v.waitKey()

