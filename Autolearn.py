__author__ = 'steeven'
from Others import GetImagenes
import cv2 as v
import numpy as np
import mlpy
from Caracteristicas import eolaplace, eogradient, smlaplacian
from corte import dividir, unir

#print GetImagenes('OUT')[0]