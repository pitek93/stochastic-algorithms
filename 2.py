import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.random.normal(size=100)
y = np.random.normal(size=100)
z = np.random.normal(size=100)

ax = fig.add_subplot(111, projection='3d')

plt.scatter(x,y,z)
plt.show()