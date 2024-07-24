import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


fig= plt.figure()
ax= Axes3D(fig)

z=np.linspace(0,1,50)
t=np.linspace(0,0.025,50)
X,Y=np.meshgrid(z,t)



z0=2
t0=2846.118571
T0=674.285714

def T(z,t):
    
    T=0.459227
    for n in range(0,4000):
        T+=(4/(np.pi)**3)*((1-np.exp(-(2*n+1)**2*(np.pi)**2*t))/((2*n+1)**3)*np.sin((2*n+1)*np.pi*z))
        
    return T

print(np.exp(-9*np.pi**2))
             

ax.plot_surface(X*z0,Y*t0,T(X,Y)*T0-273.15)
ax.set_xlabel('z[cm]')
ax.set_ylabel('t[s]')
ax.set_zlabel('T[°C]')
plt.show()