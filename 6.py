from sklearn import manifold, datasets #obnizanie wymiarowosci
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
import numpy as np
#%matplotlib notebook

x1, c1 = datasets.samples_generator.make_blobs(1000, 10)
x2, c2 = datasets.samples_generator.make_blobs(1000, 10)
#x, c = datasets.samples_generator.make_s_curve(1000,noise = 0.5) #c-color
print(x1,x2)
#set(c)

x=np.vstack([x1,x2])
c=np.vstack([c1,c2+3])

t0=time.time()
y= manifold.LocallyLinearEmbedding(n_neighbors=900, n_components=2, eigen_solver="auto", method="standard").fit_transform(x)
#y= manifold.TSNE(init="pca").fit_transform(x)
t1=time.time()

print(t1-t0)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(y[:,0],y[:,1],c=c)
plt.show()

'''
1. Milestoning na modelowym potencjale
2. Nieliniowa redukcja wymiarowości metoda T-SNE
3. Landu Zener na N krzywych potencjalnych
4. Dyfuzja liganda CO z neuroglobing pod wysokim cisnieniem

5. Pakiet w pythonie do redukcji wymiarowosci i klasteryzacji struktur bialek
(reprezentacja w formacie grafu)
6. reimplementacja maze do programu Plumed
'''