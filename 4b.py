

import numpy as np
import matplotlib.pyplot as plt

# krzywa Morse'a
def V1(r, r0 = 1, De = 30, alpha = 2):
    c = -alpha * (r - r0)
    return De * (np.exp(2 * c) - 2 * np.exp(c))

# przeskok na potencjał przy uderzeniu fotonu
def V2(r, A = 180, b = 1, B = 10):
    return A * np.exp(- b * r) - B

# potencjał Mullera
def V3(x,
       y,
       A = [-200, -100, -175, 0],
       a = [-1, -1, -6.5, 0.7],
       b = [0, 0, 11, 0.6],
       c = [-10, -10, -6.5, 0.7],
       x0 = [1, 0, -0.5, -1],
       y0 = [0, 0.5, 1.5, 1]):
    return sum(A[i] * np.exp(
               a[i]*(x-x0[i])**2)+\
               b[i]*(x-x0[i])*(y-y0[1])+\
               c[i]*(y-y0[i])**2)

x = np.linspace(0, 5)
y = np.linspace(0, 5)
x, y = np.meshgrid(x, y)


r = np.linspace(0, 5)
plt.plot(r, V1(r))
plt.plot(r, V2(r))
plt.ylim(-40, 40)
plt.xlim(0, 5)


# monte carlo
_i = range(1000)

_r = 1 # [Å]
step = 0.2 # [Å]
T = 300 # [K]
k = 0.002 # [kcal / (mol * K)] Boltzmann constant

_r_result = []
_V_result = []

def P(r1, r2, T):
    dr = np.abs(r1 - r2)
    beta = 1 / (k * T)
    return np.exp(-beta * dr)

ps = 0.05 # prawdopodobieństwo zmienienia krzywych

f = V1
rc = 3
dt = 1e-12

def V_alternate(f):
    if f == V1: return V2
    if f == V2: return V1
    
########## landau-zener
# nachylenia
# f = V1'(rc), g = V2'(rc)
h = 0.0001
_f = (V1(rc + h) - V1(rc - h)) / (2 * h)
_g = (V2(rc + h) - V2(rc - h)) / (2 * h)

h = 6.626070e-34 * 1.44e20 * 1/dt
delta = 0.05 # [kcal / mol]
coeff = -2 * np.pi * (2 * np.pi * delta**2) / (h * np.abs(_f - _g)) #wspolczynnik
# P = np.exp(coeff * (1 / v))
#########################

for i in _i:
    __r = _r + np.random.uniform(-step, step)
    
    # landau-zener
    if np.abs(__r - rc) < 0.1:
        p_lz = np.exp(coeff / (np.abs(__r - _r)))
        if p_lz > np.random.uniform(0, 1):
            f = V_alternate(f)
    elif ps > np.random.uniform(0, 1):
        if ((__r > rc and f == V1) or
            (__r < rc and f == V2) or
            (__r < rc and f == V1 and V1(__r) < -20)):
            f = V_alternate(f)
    
    if f(__r) < f(_r) or P(__r, _r, T) > np.random.uniform(0, 1):
        _r = __r
    _r_result.append(_r)
    _V_result.append(f(_r))



plt.xlabel('r [Å]')
plt.ylabel('V')
plt.ylim(-40, 40)
plt.xlim(0, 5)
plt.plot(_r_result, _V_result)
plt.show()





