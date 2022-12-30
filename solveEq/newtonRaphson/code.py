import numpy as np
import matplotlib.pyplot as plt

def newtonRaphson(f, df, x0, eps):
    x = x0
    while True:
        x1 = x - f(x)/df(x)
        if abs(x1 - x) < eps:
            return x1
        x = x1

def f(x):
    return np.log(x) - x**2 + 2

def df(x):
    return 1/x - 2*x

x0 = 0.3
eps = 0.001
x = newtonRaphson(f, df, x0, eps)

x = np.linspace(0.1, 1, 100)
y = f(x)
plt.plot(x, y)
plt.plot(x, np.zeros(len(x)))
plt.plot(x0, f(x0), 'ro')
plt.plot(x, df(x)*(x-x0) + f(x0))
plt.plot(x, df(x)*(x-x) + f(x))
plt.plot(x, df(x)*(x-x) + f(x0))
plt.plot(x, df(x)*(x-x0) + f(x))
plt.plot(x, df(x)*(x-x) + f(x0) - eps)
plt.plot(x, df(x)*(x-x0) + f(x0) + eps)

plt.show()
