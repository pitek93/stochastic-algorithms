from sklearn import cluster, datasets, metrics
import numpy as np
import matplotlib.pyplot as plt

 
nc = datasets.make_circles(n_samples=3000, factor=0.6, noise=0.1)
#nc = datasets.make_moons(n_samples=1800,noise = 0.05)
#nc = np.random.rand(1500,2),np.zeros(1500)

x,y = nc
 
 
colorArray=['b' if i else 'r' for i in y]
 
 
m=cluster.MiniBatchKMeans(n_clusters=2)
m.fit(x)
colorArrayM=['b' if i else 'r' for i in m.labels_]
 
m2=cluster.SpectralClustering(n_clusters=2,eigen_solver='arpack', affinity='nearest_neighbors')
m2.fit(x)
colorArrayM2=['b' if i else 'r' for i in m2.labels_]
 
m3=cluster.DBSCAN(eps=0.8, min_samples=900, metric='euclidean', algorithm='auto', leaf_size=30, p=None, n_jobs=1)
m3.fit(x)
colorArrayM3=['b' if i else 'r' for i in m3.labels_]
 
m4=cluster.Birch(n_clusters=2)
m4.fit(x)
colorArrayM4=['b' if i else 'r' for i in m4.labels_]
 
 
plt.figure(1)
 
plt.subplot(321)
plt.title("")
plt.scatter(x[:,0],x[:,1],c=colorArray)
 
plt.subplot(322)
plt.title("k means")
plt.scatter(x[:,0],x[:,1],c=colorArrayM)
 
plt.subplot(323)
plt.title("spectral clustering")
plt.scatter(x[:,0],x[:,1],c=colorArrayM2)
 
plt.subplot(324)
plt.title("DBSCAN")
plt.scatter(x[:,0],x[:,1],c=colorArrayM3)
 
plt.subplot(325)
plt.title("Birch")
plt.scatter(x[:,0],x[:,1],c=colorArrayM4)

plt.show()
