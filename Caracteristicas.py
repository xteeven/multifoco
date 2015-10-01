__author__ = 'Xteeven'


import cv2 as v
import numpy as np
import time

imagen = v.imread('OUT/3_1_00_I.jpg',0)



def eolaplace(image, value=True):
    energy = v.filter2D(image, -1, np.asarray(([-1,-4,-1],[-4,20,-4],[-1,-4,-1])))
    energy = np.array(np.array(energy, dtype=np.uint16)**2)
    energy = (energy/float(np.amax(energy)))*float(255)
    if value:
        return sum(sum(energy))/((len(image))*(len(image[0])))*1.0
    else:
        return np.array(energy, dtype=np.uint8)


def smlaplacian(imagen, stepx=1, stepy=1,value=True):
    kernx = np.array([[-1]+[0]*stepy+[2]+[0]*stepy+[-1]]).astype(np.float)
    kerny = np.array([[-1]+[0]*stepx+[2]+[0]*stepx+[-1]]).astype(np.float).T
    energy = v.filter2D(imagen,-1, kerny) + v.filter2D(imagen,-1, kernx)
    if value:
        return float(sum(sum(energy)))/((len(imagen))*(len(imagen[0])))
    else:
        return energy


def eogradient(imagen, value=True):
    eog = (np.array(v.Sobel(imagen, -1, 0, 1), dtype=np.uint16)**2 + np.array(v.Sobel(imagen, -1, 1, 0), dtype=np.uint16)**2)
    eog = np.array((eog/float(np.amax(eog)))*float(255))
    if value:
        return sum(sum(np.array(eog)))/((len(imagen))*(len(imagen[0])))*1.0
    else:
        return np.array(eog, dtype=np.uint8)

def morphgradient(imagen, size = 3, value=True):
    it=1
    mgd = v.dilate(imagen, v.getStructuringElement(v.MORPH_RECT, (size, size)),iterations=it)-v.erode(imagen, v.getStructuringElement(v.MORPH_RECT, (size, size)), iterations=it)
    rt, bin = v.threshold(mgd, 128, 255, v.THRESH_BINARY)
    if value:
        return float(sum(sum(mgd)))/((len(imagen))*(len(imagen[0])))*1.0
    else:
        return mgd

def varianza(imagen):
    return float(np.var(imagen))/((len(imagen))*(len(imagen[0])))*1.0


# print smlaplacian(imagen)
# print eolaplace(imagen)
# print eogradient(imagen)
# print morphgradient(imagen)
# print varianza(imagen)
# v.imshow('1',smlaplacian(imagen, value=False))
# v.imshow('2',eolaplace(imagen, value=False))
# v.imshow('3', eogradient(imagen, value=False))
# v.imshow('4', morphgradient(imagen, value=False))
# v.imshow('0',imagen)
# v.waitKey()

print 'damm'