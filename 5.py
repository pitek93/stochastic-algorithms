#connectivity, manifold learning
#dbscan monte carlo, podejmowanie decyzji cy wykonac krok czy nie
#mpl

from sklearn import cluster, datasets
import matplotlib.pyplot as plt
import numpy as np

#np.random.rand(1500,2),np.zeros(1500)
nc =  datasets.make_moons(n_samples=1500, noise=0.5) #rozne zestawy danych
X,y = nc

m = cluster.MiniBatchKMeans(n_clusters=2)
sp = cluster.SpectralClustering(n_clusters=2, eigen_solver='arpack', affinity='nearest_neighbors')
DB = cluster.DBSCAN(eps=0.1) #gestosc danych #epsilon - najmn odleglosc miedzy klastrami
bir = cluster.Birch(n_clusters=2)

m.fit(X)
sp.fit(X)
DB.fit(X)
bir.fit(X)

mCol = ['b' if i else 'r' for i in m.labels_]
spCol = ['b' if i else 'r' for i in sp.labels_]
DBCol = ['b' if i else 'r' for i in DB.labels_]
birCol = ['b' if i else 'r' for i in bir.labels_]

fig, ax = plt.subplots(2,2)
ax[0,0].scatter(X[:,0],X[:,1],c=mCol)
ax[0,1].scatter(X[:,0],X[:,1],c=spCol)
ax[1,0].scatter(X[:,0],X[:,1],c=DBCol)
ax[1,1].scatter(X[:,0],X[:,1],c=birCol)
plt.show()
