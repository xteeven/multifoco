__author__ = 'vaf'

import cv2 as v
import numpy as np

def dividir(imagen, rows=2,cols=2):
    alto = len(imagen)
    ancho = len(imagen[0])
    print 'ancho alto', ancho, alto

    for i in range(rows):
        for j in range(cols):
            print 'coord', i, j

            print 'imagen[',((i*1.0/rows))*ancho,':',((i*1.0+1)/(rows))*alto,',',((j*1.0/cols))*ancho,':',((j*1.0+1)/(cols))*alto,']'
            out = imagen[(i*1.0/rows)*ancho:(i*1.0+1)/(rows)*alto, (j*1.0/cols)*ancho:(j*1.0+1)/(cols)*alto]
            v.imshow(str(i)+str(j), out)



imagen = v.imread('mosca.png',0)

dividir(imagen)
