__author__ = 'root'

from Others import GetImagenes
import cv2 as v
import numpy as np
import mlpy
from Caracteristicas import eolaplace, eogradient, smlaplacian
from corte import dividir, unir

datos = np.loadtxt('final.csv', delimiter=';')
x, y = datos[:, :8], datos[:, 8].astype(np.int)
norm = np.sqrt(np.sum(x**2, axis=0))
xn = x / norm
vector = mlpy.LibSvm(svm_type='nu_svc', kernel_type='rbf', gamma=900 , C=1)
vector.learn(xn, y)

numero =10
files = GetImagenes("dataset_gray")
img = numero*2
A = v.imread('dataset_gray/'+files[img], 0)
B = v.imread('dataset_gray/'+files[img+1], 0)
particiones = 40
Ai = dividir(A, particiones, particiones)
Bi = dividir(B, particiones, particiones)


out = Ai
for i in range(len(Ai[0])):
    for j in range(len(Ai)):

        Aieol = eolaplace(Ai[j][i])
        Bieol = eolaplace(Bi[j][i])
        Aisml = smlaplacian(Ai[j][i])
        Bisml = smlaplacian(Bi[j][i])
        Aieog = eogradient(Ai[j][i])
        Bieog = eogradient(Bi[j][i])
        Aivar = np.var(Ai[j][i])
        Bivar = np.var(Bi[j][i])
        caract = np.asarray([Aieol, Aieog, Aisml, Aivar, Bieol, Bieog, Bisml, Bivar])/norm
        imagefocus = vector.pred(caract)
        alpha = abs(Aivar/(Aivar+Bivar)) if abs(Aivar/(Aivar+Bivar)) > 0 else 0.5
        out[j][i] = Ai[j][i] if imagefocus == 0 else Bi[j][i] if imagefocus == 1 else Ai[j][i]*(alpha) + Bi[j][i]*(1-alpha)



v.imshow('1', unir(out))
v.imshow('2', A)
v.imwrite('out'+files[img]+'.jpg', unir(out))
v.waitKey()

