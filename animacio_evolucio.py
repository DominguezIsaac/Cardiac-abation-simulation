#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 21:49:53 2023

@author: jupiter
"""
import numpy as np
from matplotlib import pyplot as plt
from numpy import *
import math
import matplotlib.animation as animation
import ffmpeg



z=np.linspace(0,1,101) #genera puntos aleatorios "normalizados" de z

#funcion solucion analitica
def T(z,t):
    T=0.459227
    for n in range(0,100):
        T+=(4/(np.pi)**3)*((1-np.exp(-(2*n+1)**2*(np.pi)**2*t))/((2*n+1)**3)*np.sin((2*n+1)*np.pi*z))   
        #deshacer normalitzacion
        zz=z*2
        TT=(T*674.285714)-273.15
    return (TT,zz) #devuelve tuple con dos columnas, primera temperatura, segunda espacio a un tiempo t

#valors inicials de temperatura en todos z a t=0
T0=np.array([]) 
T0=T(z,0.0)

temps=np.linspace(0,0.025,1000) #genera intervalos de tiempo

#plot animación 
fig = plt.figure()
ax = fig.add_subplot(111)

#crear primer frame y definir plot
plt.ylabel('T [°C]')
plt.xlabel('z [cm]')
plt.axvline(x=0.75, color='k', linestyle='--', label='regió malalta')
plt.axvline(x=1.25, color='k', linestyle='--')
plt.axhline(y=50, color='r', linestyle='--' )
plt.axhline(y=80, color='r', linestyle='--')
tx = ax.set_title('Distribució de calor a t=0s')
curva, = ax.plot(T0[1], T0[0], 'g', label ='T(t,z)') 
plt.legend(loc='upper right')

#funcion que cada "frame" (cada tiempo) se actualiza
def update(i):
   f=np.array([])
   f=T(z,temps[i])
   curva.set_ydata(f[0])
   curva.set_xdata(f[1])
   tx.set_text('Distribució de calor a t={0}s'.format(int(temps[i]*2846.118571))) #actualiza tiempo en segundos
   return curva,
   
#ejecutar y guardar animacion 
ani = animation.FuncAnimation(fig, update, frames=1000, interval=10) 
ani.save('animacio_evolucio_calor.gif', writer='Pillow')
ani.save('animacio_evolucio_calor.mp4', writer='ffmpeg')

plt.show()