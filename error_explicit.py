import numpy as np
from matplotlib import pyplot as plt
from numpy import *
import math
import scipy.stats as ss

# Abre el archivo
with open('T_explicit(0.25).txt') as fichero:
    # Lee todas las líneas del archivo
    lineas = fichero.readlines()

# Inicializa una lista de listas para almacenar las columnas
A = [[] for _ in range(len(lineas[0].split()))]

# Procesa cada línea y divide en columnas
for linea in lineas:
    valores = [float(valor) for valor in linea.split()]
    
    

 # Almacena cada valor en la lista correspondiente
    for i, valor in enumerate(valores):
        A[i].append(valor)



# Abre el archivo
with open('T_explicit(0.49).txt') as fichero:
    # Lee todas las líneas del archivo
    lineas = fichero.readlines()

# Inicializa una lista de listas para almacenar las columnas
B = [[] for _ in range(len(lineas[0].split()))]

# Procesa cada línea y divide en columnas
for linea in lineas:
    valores = [float(valor) for valor in linea.split()]
    
    

 # Almacena cada valor en la lista correspondiente
    for i, valor in enumerate(valores):
        B[i].append(valor)

# Abre el archivo
with open('T_explicit(0.51).txt') as fichero:
    # Lee todas las líneas del archivo
    lineas = fichero.readlines()

# Inicializa una lista de listas para almacenar las columnas
C = [[] for _ in range(len(lineas[0].split()))]

# Procesa cada línea y divide en columnas
for linea in lineas:
    valores = [float(valor) for valor in linea.split()]
    
    

 # Almacena cada valor en la lista correspondiente
    for i, valor in enumerate(valores):
        C[i].append(valor)
        
z0=2
t0=2846.118571
T0=674.285714

#Agafem la columna N-1 que es la que correspon al temps ta
#treiem el primer element ja que correspon al temps i no el volem per al plot
A[0].pop(0)
A[len(A)-2].pop(0) 
B[len(B)-2].pop(0)
C[len(C)-2].pop(0)


A[0]=np.array(A[0])
A[len(A)-2]=np.array(A[len(A)-2])
B[len(B)-2]=np.array(B[len(B)-2])
C[len(C)-2]=np.array(C[len(C)-2])



z=np.linspace(0,1,101)

#funció analítica
def T(z,t):
    
    T=A[1][1]
    for n in range(0,4000):
        T+=(4/(np.pi)**3)*((1-np.exp(-(2*n+1)**2*(np.pi)**2*t))/((2*n+1)**3)*np.sin((2*n+1)*np.pi*z))
        
    return T


sol=np.array([])
sol=T(z,0.025)

errorA=[]
errorB=[]
errorC=[]
#càlcul de l'error relatiu
for i in range(len(sol)):
    errorA.append(np.abs((A[len(A)-2][i]-sol[i])/sol[i])*100)
    errorB.append(np.abs((B[len(B)-2][i]-sol[i])/sol[i])*100)
    errorC.append(np.abs((C[len(C)-2][i]-sol[i])/sol[i])*100)
    

#TÃ­tol i tÃ­tol dels eixos
ax=plt.axes()
plt.ylabel(r'error relatiu [%]')
plt.xlabel(r'$z$ [cm] ')


#Plot
plt.plot(A[0]*z0,errorA,"-",color="forestgreen",label="Error amb $\Delta t= 0,25\Delta z^2$")
plt.plot(A[0]*z0,errorB,"-",color="blue",label="Error amb $\Delta t=0.49\Delta z^2$")
plt.plot(A[0]*z0,errorC,"-",color="red",label="Error amb $\Delta t=0.51\Delta z^2$")

#Mida del grÃ fic (relaciÃ³ x:y)
plt.rcParams["figure.figsize"] = (8, 5)

#Grid
plt.rcParams.update({
    "grid.color": "0.1",
    "grid.linestyle": "-",
    "grid.linewidth": 0.2})
plt.grid(True,color='gray')

#Color i gruix dels eixos
ax.spines['bottom'].set_linewidth(1.2)
ax.spines['left'].set_linewidth(1.2)
ax.spines['top'].set_visible(1.2)
ax.spines['right'].set_visible(1.2)

#Ticks dels eixos
ax.tick_params(axis='x', direction='in', length=6, color='black')
ax.tick_params(axis='y', direction='in', length=6, color='black')

secax = ax.secondary_xaxis('top')
secay = ax.secondary_yaxis('right')

secax.tick_params(axis='x', direction='in', length=6, color='black')
secay.tick_params(axis='y', direction='in', length=6, color='black')

secay.set_yticklabels([])
secax.set_xticklabels([])

#Rang dels eixos
#plt.ylim([9.8, 11])
#plt.xlim([0,0.6])

#Llegenda: s'ha de posar 'label="hola"' al plt.plot()
plt.legend(loc='best', facecolor='w', fontsize=12)


plt.show()
