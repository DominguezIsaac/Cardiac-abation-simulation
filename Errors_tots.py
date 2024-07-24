import numpy as np
from matplotlib import pyplot as plt
from numpy import *
import math
import scipy.stats as ss

# Abre el archivo
with open('T_explicit(0.49).txt') as fichero:
    # Lee todas las líneas del archivo
    lineas = fichero.readlines()

# Inicializa una lista de listas para almacenar las columnas
E = [[] for _ in range(len(lineas[0].split()))]

# Procesa cada línea y divide en columnas
for linea in lineas:
    valores = [float(valor) for valor in linea.split()]
    
    

 # Almacena cada valor en la lista correspondiente
    for i, valor in enumerate(valores):
        E[i].append(valor)


# Abre el archivo
with open('T_implicit(0.49dt2).txt') as fichero:
    # Lee todas las líneas del archivo
    lineas = fichero.readlines()

# Inicializa una lista de listas para almacenar las columnas
I = [[] for _ in range(len(lineas[0].split()))]

# Procesa cada línea y divide en columnas
for linea in lineas:
    valores = [float(valor) for valor in linea.split()]
    
    

 # Almacena cada valor en la lista correspondiente
    for i, valor in enumerate(valores):
        I[i].append(valor)

# Abre el archivo
with open('T_CN(0.49dt2).txt') as fichero:
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



E[0].pop(0)
E[len(E)-2].pop(0)
I[len(I)-2].pop(0)
C[len(C)-2].pop(0)


E[0]=np.array(E[0])
E[len(E)-2]=np.array(E[len(E)-2])
I[len(I)-2]=np.array(I[len(I)-2])
C[len(C)-2]=np.array(C[len(C)-2])


z=np.linspace(0,1,101)


def T(z,t):
    
    T=E[1][1]
    for n in range(0,40000):
        T+=(4/(np.pi)**3)*((1-np.exp(-(2*n+1)**2*(np.pi)**2*t))/((2*n+1)**3)*np.sin((2*n+1)*np.pi*z))
        
    return T


#ERROR

sol=np.array([])
sol=T(z,0.025)

errorE=[]
errorI=[]
errorC=[]

for i in range(len(sol)):
    errorE.append(np.abs((E[len(E)-2][i]-sol[i])/sol[i])*100)
    errorI.append(np.abs((I[len(I)-2][i]-sol[i])/sol[i])*100)
    errorC.append(np.abs((C[len(C)-2][i]-sol[i])/sol[i])*100)
    
#TÃ­tol i tÃ­tol dels eixos
ax=plt.axes()
plt.ylabel(r'error relatiu [%]')
plt.xlabel(r'$z$ [cm] ')


#Plot

plt.plot(E[0]*z0,errorE,"-",color="forestgreen",label="Error explícit" )
plt.plot(E[0]*z0,errorI,"-",color="red",label="Error implícit")
plt.plot(E[0]*z0,errorC,"-",color="darkviolet",label="Error Crank-Nicolson" )
#Mida del grÃ fic (relaciÃ³ x:y)
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
