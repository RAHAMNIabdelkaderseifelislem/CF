import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 + 2*x**2 - 5*x + 3

def horner(f, x, a):
    n = len(a) - 1
    p = a[n]
    for i in range(n-1, -1, -1):
        p = p*x + a[i]
    return p

a = [3, -5, 2, 1]

x = np.linspace(-2, 4, 100)

p = horner(f, x, a)
# plot horner polynomial and f(x)
plt.plot(x, p, label='horner polynomial')
plt.plot(x, f(x), label='f(x)')
plt.legend()
plt.show()
