__author__ = 'steeven'
from Others import GetImagenes
import cv2 as v
import os
import numpy as np
from easygui import *
import mlpy
from Caracteristicas import eolaplace, eogradient, smlaplacian, varianza, morphgradient
from corte import dividir, unir

files = GetImagenes('OUT')


salida = "Salida"
datos = open("datasetnewtesast.txt", "w")
try:
    os.mkdir(salida)
except:
    pass


response = None
while len(files) != 0:
    Img1 = files.pop()
    Img2 = Img1.split('_')
    Img2[1] = '1' if Img2[1] == '2' else '2'
    Img2[3] = 'N.jpg' if Img2[3] == 'E.jpg' else 'E.jpg' if Img2[3] == 'N.jpg' else 'I.jpg'
    Img2 = Img2[0]+'_'+Img2[1]+'_'+Img2[2]+'_'+Img2[3]
    Img2 = files.pop(files.index(Img2))
    clase = 0 if Img1[-5:-4] == 'E' else 1 if Img2[-5:-4] == 'E' else 2
    Img1 = v.imread('OUT/'+Img1, 0)
    Img2 = v.imread('OUT/'+Img2, 0)
    Iaeol = eolaplace(Img1)
    Iaeog = eogradient(Img1)
    Iasml = smlaplacian(Img1)
    Iavar = varianza(Img1)
    Iamrp = morphgradient(Img1)
    Ibeol = eolaplace(Img2)
    Ibeog = eogradient(Img2)
    Ibsml = smlaplacian(Img2)
    Ibvar = varianza(Img2)
    Ibmrp = morphgradient(Img2)
    #print Iaeol, Iaeog, Iasml, Iavar, Iamrp, Ibeol, Ibeog, Ibsml, Ibvar, Ibmrp, clase
    print Iaeol, Ibeol
    Img1 = v.cvtColor(Img1, v.COLOR_GRAY2RGB)
    Img2 = v.cvtColor(Img2, v.COLOR_GRAY2RGB)
    v.circle(Img1,(len(Img1[0])/2,len(Img1)/2),len(Img1)/2,[0,0,255],3) if clase ==0 else v.circle(Img2,(len(Img1[0])/2,len(Img1)/2),len(Img1)/2,[0,0,255],3) if clase ==1 else 0
    v.imshow('A', Img1)
    v.imshow('B', Img2)
    v.waitKey()
    response = buttonbox("verdadero?", "Verificacion", ["SI", "NO"])
    if response == "SI":
        datos.write(str(Iaeol)+","+str(Iaeog)+","+str(Iasml)+","+str(Iavar)+","+str(Iamrp)+","+str(Ibeol)+","+str(Ibeog)+","+str(Ibsml)+","+str(Ibvar)+","+str(Ibmrp)+","+str(clase)+"\n")
    else:
        print "Falso"

    print len(files)

datos.close()
