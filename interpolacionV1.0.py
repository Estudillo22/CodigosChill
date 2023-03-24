"""
Creado por Alberto Estudillo
11 de Marzo de 2023

Ultima edicion: 14 de Marzo de 2023
    
"""
############## Funcion ###############
"""
El codigo toma una lista de puntos e interpola puntos faltantes
o puntos que sean de interes cambiar, empezando con posiciones 
en 0
"""

from scipy.interpolate import lagrange
import numpy as np
import matplotlib.pyplot as plt 
import time

in_time = time.time()

pathtrack = ('F:\\Rastreo\\')
pathout = ('F:\\Rastreo\\Outframes\\')
outname = ('out_frames9-.txt')
trackname = ('datosprueba2.dat')

copy_track = np.loadtxt(pathtrack+trackname)
np.savetxt(pathtrack+trackname[0:10]+'_fixed.dat',copy_track)

out = np.loadtxt(pathout+outname)
j=0
for i in out:
    pos = int(i)+j
    fila = int(pos-2)
    filamax = int(2)
###### Se pueden saltar filas y limitar filas con loadtxt
    track = np.loadtxt(pathtrack+trackname[0:10]+'_fixed.dat')
    X = np.loadtxt(pathtrack+trackname[0:10]+'_fixed.dat', usecols=[0], skiprows=fila, max_rows=filamax)
    Y = np.loadtxt(pathtrack+trackname[0:10]+'_fixed.dat', usecols=[1], skiprows=fila, max_rows=filamax)

####### Polinomio de Lagrange para interpolar
    pol = lagrange(X,Y)
    print(pol)
####### Calcular un X medio entre i e i-1 para evaluar en Lagrange
    X1 = int((X[0]+X[1])/2)
    Y1 = int(pol(X1))
    
####### Insertar el dato interpolado en los datos de tracking
    data = np.array(track)
    add = np.array([X1,Y1])
    new_data = np.insert(data, pos-1, add, axis=0)
    j+=1

    np.savetxt(pathtrack+trackname[0:10]+'_fixed.dat', new_data)

end_time = time.time()
print('El proceso finalizo en: %.2f' % ((end_time-in_time)/60) + 'minutos.')