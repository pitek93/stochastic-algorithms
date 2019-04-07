import matplotlib.pyplot as plt
import numpy as np

def gauss(x,y):
    return np.exp( -(x**2+y**2) )

x = np.linspace(-0.1, 0.1, 100)
y = np.linspace(-0.1, 0.1, 100)
x,y = np.meshgrid(x,y)

print(x,y)

g = gauss(x,y)
min=g.min()
max=g.max()
plt.contourf(x,y,g, levels=np.linspace(min,max,10))
plt.colorbar()
plt.show()