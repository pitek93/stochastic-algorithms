# za tydzień zmienne kolektywne i dane wielowymiarowe
# 10 maja kolokwium

# krzywa Morse'a
#głębokość studni
#alfa jak waska jest studnia
#alfa = 1/Arstorn
#wzbudzenie wypromieniowanie
#jesli prawdop pozwala - przaskakujemy na 2 wykr
#przeskoki wyw zew czynnikiem

import numpy as np
import matplotlib.pyplot as plt


r0=1.5             # 1,5
r=1
k=10000            # dla k=0.1 parabola bardziej plaska
t=0
beta=(0.6*300)**-1 # jesli wiecej niz 300 to moze wykonywac wieksze ruchy
b=1
B=10
A=180
rMorsea=np.linspace(0,10,1000)


def V(r):
    return (k/2.0)*((r-r0)**2) #podstawowy

def V1(rMorsea):
    return 30*(np.exp(-4*(rMorsea-r0)) - 2*np.exp(-2*(rMorsea-r0)))

def V2(rMorsea):
    return A*np.exp(-b*rMorsea)-B #wzbudzony

def Vs(r, b): # 0 st podst, 1 st wzbudzony
    if b:
        return V2(r)
    else:
        return V1(r)

                                            # -20kcal/mol
                                            # pot morsa
                                            # prawd mniejsze od stalego

x = list()
y = list()
z=0.05 #prawd ze foton uzezy w uklad
while t < 10000:
    dR = 0.2 * np.random.uniform(-1, 1)
    dV = V1(r + dR) - V1(r)

    if dV < 0:
        r = r + dR
    else:
        z = np.exp(-beta * dV)
        rprim = np.random.uniform(0, 1)

        if rprim < z:
            r = r + dR

    zprim = np.random.uniform(0, 1)
    if zprim < z:



    print("{},{},{}".format(r, dV, z))
    x.append(r)
    y.append(V1(r))
    t = t + 1


plt.plot(x,y)
# p = V1(r)
# q = V2(r)
# plt.plot(p)
# plt.plot(q)
plt.ylim([-30,30])
plt.show()

# plt.scatter(x,y)
# plt.xlabel('r')
# plt.ylabel('V(r)')
# plt.show()

#plt.scatter(x,y)

#przyjmuje r
#zwraca V
#update r
#kontrola V
#jesli v jest mniejsze od poprzedniego - akcepujemy