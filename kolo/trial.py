import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# zad 1

r_0 = 5
r_1 = 15
sigma_0 = 4
sigma_1 = 6


# funkcja potencjału
def V(r):
    return (-(1.0 / (sigma_0 * np.sqrt(2 * np.pi))) * np.exp(-(r - r_0) ** 2 / (2 * sigma_0 ** 2)) \
            - (1.0 / (sigma_1 * np.sqrt(2 * np.pi))) * np.exp(-(r - r_1) ** 2 / (2 * sigma_1 ** 2)))


s = 0.2  # [Å] długość kroku
t = 10 ** 5  # ilość kroków czasu
k = 0.002  # [kcal / (mol * K)] stała Boltzmanna


# prawdopodobieństwo akceptacji kroku z r_1 do r_2 z wyższym potencjałem
def p(r_1, r_2, T):
    try:
        dr = np.abs(r_1 - r_2)
        beta = 1 / (k * T)
        return np.exp(-beta * dr)
    except ZeroDivisionError:
        return 0


# metoda monte carlo
def monte_carlo(initial_r, initial_T=300, cooling=1):
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

r = np.linspace(-25, 50, 10000)
plt.plot(r, V(r))
plt.xlim(-25, 50)
plt.xlabel('r [Å]')
plt.ylabel('V')
plt.show()

# zad 2
rr, Vr, pt = monte_carlo(initial_r = 0)

plt.plot(range(t), pt)
plt.xlabel('t')
plt.ylabel('p(t)')
plt.show()

p_mean = np.mean(pt)
print("średnie p wynosi " + str(p_mean))


# zad 3
#nie dziala
#plt.hist(p_result, bins = 40)
#plt.show()

# zad 4

rr, Vr, pr = monte_carlo(initial_r = 0, cooling = 0.95)

plt.plot(range(t), Vr)
plt.xlabel('t')
plt.ylabel('V(r)')

print()