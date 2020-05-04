import cmath
import math
import random
import matplotlib.pyplot as plt
import time
import numpy as np
from cmath import exp, pi

N = 1024
n = 6
W = 2100

minimal_range = 0
maximum_range = 1


# Функція генератора стаціонарного випадкового сигналу
def stat_random_signal(n, W):
    A = [random.random() for _ in range(n)]
    phi = [random.random() for _ in range(n)]

    def f(t):
        x = 0
        for i in range(n):
            x += A[i]*math.sin(W / n * t * i + phi[i])
            #x *= (math.cos((2*math.pi/N)*i*t))
        return x
    return f


s_gen = stat_random_signal(n, W)
s = [s_gen(i) for i in range(N)]
dft = np.fft.fft(s)


# Функція для обчислення Дискретного перетворення Фур'є
def dft(x):
    t = []
    N_ = len(x)
    for k in range(N_):
        a = 0
        for n_ in range(N):
            a += x[n_]*cmath.exp(-2j*cmath.pi*k*n_*(1/N_))
        t.append(a)
    return t


ddd = dft(s)
print(s)


plt.plot(range(N), s)
plt.plot(range(N), np.array(ddd).real)


plt.show()