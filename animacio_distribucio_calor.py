#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 10:16:14 2023

@author: jupiter
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import ffmpeg
from matplotlib import colormaps


#importar valors calculats 
# Abre el archivo
with open('T_explicit(0.25).txt') as fichero:
    # Lee todas las líneas del archivo
    lineas = fichero.readlines()

# Inicializa una lista de listas para almacenar las columnas
T = [[] for _ in range(len(lineas[0].split()))]

# Procesa cada línea y divide en columnas
for linea in lineas:
    valores = [float(valor) for valor in linea.split()]
    
 # Almacena cada valor en la lista correspondiente
    for i, valor in enumerate(valores):
        T[i].append(valor)
"""T[0] serà la primera columna del bloc de notas de les dades"""
 
ay=np.array(T)
columnes, linies = ay.shape
#print(len(T),'linien:', linies,'columnes', columnes) # len() == columnes 


#valors de normalització:
z0=2
t0=2846.118571
T0=674.285714


#re normalitzar valors calculats: T[c][l]
A = np.empty((columnes, linies)) 
t=[] 
        
for c in range(columnes):
    A[c][0]=T[c][0]*t0
    t.append(A[c][0])  
        
for l in range(1,linies):
    for c in range(1, columnes):
       A[c][l]=T[c][l]*T0-273.15

#plot animacion

fig = plt.figure()
ax = fig.add_subplot(111)

#crear matrix con los valores para la animación
D=[]
for j in range(len(A)):
  data=A[j][:, np.newaxis]  #*dim
  D.append(data)


#crear primer frame y definir plot
cv0 = D[1] #frame 1 a t0
im = ax.imshow(cv0, extent=[0,5,0,2],cmap='Reds', vmax=60, vmin=30) 
cb = fig.colorbar(im, ax=ax)
ax.set_ylabel('Z [cm]')
ax.set_xlabel('X')
plt.axhline(y=0.75, color='k', linestyle='--' )
plt.axhline(y=1.25, color='k', linestyle='--')
tx = ax.set_title('Distribució de calor a t=0s')

# funcion que se actuliza cada i(cada tiempo=frame) y que actualiza el frame dentro del plot ya definido
def animate(i): 
    arr = D[i]
    temps=t[i]
    im.set_data(arr)
    im.set_clim(30, 60)
    ax.set_ylabel('Z [cm]')
    ax.set_xlabel('X')
    plt.axhline(y=0.75, color='k', linestyle='--' )
    plt.axhline(y=1.25, color='k', linestyle='--')
    tx.set_text('Distribució de calor a t={0}s'.format(int(temps)))
   
#ejecutar y guardar animació (como gif y mp4)
ani = animation.FuncAnimation(fig, animate, frames=len(D), interval=10) 
ani.save('animació_distribució_calor.gif', writer='Pillow')
ani.save('animació_distribució_calor.mp4', writer='ffmpeg')
plt.show()
