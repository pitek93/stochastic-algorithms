import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# zad 1
r0 = 5
r1 = 15
sigma0 = 4
sigma1 = 6

def V(r):
    return - (1 / (sigma0 * np.sqrt(2 * np.pi) ) ) * np.exp( (-(r - r0) ** 2) / (2 * sigma0** 2)) \
           - (1 / (sigma1 * np.sqrt(2 * np.pi) ) ) * np.exp( (-(r - r1) ** 2) / (2 * sigma1** 2))

r = np.linspace(-20,50,1000)
plt.plot(r, V(r))
plt.xlabel("r")
plt.ylabel("V(r)")
plt.show()

s = 0.2
t = 10 ** 5
k = 0.002

def p(r1, rNext, T):
    try:
        dr = np.abs(r1 - rNext)
        beta = 1 / (k * T)
        return np.exp(-beta * dr)
    except ZeroDivisionError:
        return 0


def monte_carlo(initial_r=0, initial_T=300, cooling=1):
    r_result = []
    V_result = []
    p_result = []
    r = initial_r
    T = initial_T
    for _ in range(t):
        _r = r + np.random.uniform(-s, s)
        r_result.append(r)
        V_result.append(V(r))
        if V(_r) < V(r):
            p_result.append(1)
        else:
            p_result.append(p(r, _r, T))
        if V(_r) < V(r) or p(r, _r, T) > np.random.uniform(0, 1):
            r = _r
        T *= cooling

    return r_result, V_result, p_result

# zad 2
rr, Vr, pt = monte_carlo(initial_r = 0)

plt.plot(range(t), pt, linewidth = 0.01)
plt.xlabel('t')
plt.ylabel('p(t)')
plt.show()

p_mean = np.mean(pt)
print("mean probability: " + str(p_mean))


#zad 3 nie dziala

plt.hist(r_result, bins = 40, normed = 1)
plt.xlabel('r')
plt.ylabel('p(r)')
plt.show()

# zad 4
rr, Vr, pr = monte_carlo(initial_r = 0, cooling = 0.95)

plt.plot(range(t), Vr)
plt.xlabel('t')
plt.ylabel('V(r)')

print("minimum V(r): " + str(Vr[-1]))


# zad 5 nie dziala

import matplotlib.pyplot as plt
from sklearn import datasets, cluster, metrics
n = datasets.make_circles(n_samples=3000, factor=0.6, noise = 0.1)

x, y = n

method=cluster.DBSCAN(eps=0.01, min_samples=900, metric='euclidean', algorithm='auto', leaf_size=30, p=None, n_jobs=1)
method.fit(x)

colorCondition = ['b' if i else 'r' for i in method.labels_]
plt.scatter(x[:,0],x[:,1],c=colorCondition)
plt.show()