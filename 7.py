#parallel temepering

import numpy as np

class ParallelTempering(object):

     def _init_(self,T,n,tlist):
        self.T=T
        self.n=n
        self.np.tlist=np.tlist
        k=0.6
        beta = ((0.6*np.tlist)**-1)


     def P(r1, r2, T):
        k=0.6
        dr = np.abs(r1 - r2)
        beta = 1 / (k * T)
        return np.exp(-beta * dr)


    _i = range(1000)
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


tlist = [100,200,300,400,500]

# min (1,exp((Ei-Ej)-(1/k*Ti-1/k*Tj)))


# for t in time
# *****************
# for r in replicas
#   krok
#   akceptacja?


#1 klasa ze schematem Metropolisa dla N replik
#2 Wymiana replik z PPBstwem Boltzmana