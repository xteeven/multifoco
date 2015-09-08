__author__ = 'Steeven Villa'

import cv2 as v
import numpy as np
from corte import dividir
from Caracteristicas import eolaplace, eogradient, smlaplacian

imagen = v.imread('5.png', 0)














v.imshow('2', imagen)

v.waitKey()