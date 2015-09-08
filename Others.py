__author__ = 'vaf'
import numpy as np

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
