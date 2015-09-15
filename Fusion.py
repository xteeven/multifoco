__author__ = 'Steeven Villa'

import cv2 as v
import os
import numpy as np
from corte import dividir
from Caracteristicas import eolaplace, eogradient, smlaplacian
from Others import GetImagenes
from easygui import *

numero =1


files = GetImagenes("dataset_gray")
salida = "OUTq"
img = numero*2
print files[img]
A = v.imread('dataset_gray/'+files[img], 0)
B = v.imread('dataset_gray/'+files[img+1], 0)
Ai = dividir(A)
Bi = dividir(B)

datos = open("datasetb"+str(numero)+".txt","w")
try:
    os.mkdir(salida)
except:
    pass

msg = "Que imagen esta mas enfocada?"
title = "Dataset Training"
response = None
for i in range(4):
    for j in range(4):

        v.imshow('A', v.resize(Ai[j][i], (400, 400)))
        v.imshow('B', v.resize(Bi[j][i], (400, 400)))
        v.waitKey()
        response = buttonbox(msg, title, ["A", "INDEFINIDO","B"])
        print response
        Aieol = eolaplace(Ai[j][i])
        Bieol = eolaplace(Bi[j][i])
        Aisml = smlaplacian(Ai[j][i])
        Bisml = smlaplacian(Bi[j][i])
        Aieog = eogradient(Ai[j][i])
        Bieog = eogradient(Bi[j][i])
        Aivar = np.var(Ai[j][i])
        Bivar = np.var(Bi[j][i])
        try:
            #Energia Laplaciano - Energia del Gradiente - Suma Del Laplaciano Modificado - varianza
            #Primero Imagen 1 Luego Imagen 2, Ultima Fila Es el Enfoque.
            datos.write(str(Aieol)+","+str(Aieog)+","+str(Aisml)+","+str(Aivar)+","+str(Bieol)+","+str(Bieog)+","+str(Bisml)+","+str(Bivar)+","+response+"\n")
            if response == "A":
                v.imwrite(salida+"/"+files[img].split("_")[0]+"_1_"+str(i)+str(j)+"_"+"E"+".jpg", Ai[j][i])
                v.imwrite(salida+"/"+files[img+1].split("_")[0]+"_2_"+str(i)+str(j)+"_"+"N"+".jpg", Bi[j][i])
            if response == "B":
                v.imwrite(salida+"/"+files[img].split("_")[0]+"_1_"+str(i)+str(j)+"_"+"N"+".jpg", Ai[j][i])
                v.imwrite(salida+"/"+files[img+1].split("_")[0]+"_2_"+str(i)+str(j)+"_"+"E"+".jpg", Bi[j][i])
            if response == "INDEFINIDO":
                v.imwrite(salida+"/"+files[img].split("_")[0]+"_1_"+str(i)+str(j)+"_"+"I"+".jpg", Ai[j][i])
                v.imwrite(salida+"/"+files[img+1].split("_")[0]+"_2_"+str(i)+str(j)+"_"+"I"+".jpg", Bi[j][i])
        except:
            break

    if response == None:
        break

datos.close()






