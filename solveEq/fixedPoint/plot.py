import matplotlib.pyplot as plt
import numpy as np

def g1(x):
    return np.exp(x**2 - 2)

def g2(x):
    return np.sqrt(np.log(x) + 2)

def g3(x):
    return -np.sqrt(np.log(x) + 2)

def limit(x):
    return 1

def limit2(x):
    return -1

x = np.linspace(0, 2, 100)
plt.plot(x, g1(x), label='g1')
plt.plot(x, g2(x), label='g2')
plt.plot(x, g3(x), label='g3')
plt.title('Fixed Point Iteration')
plt.legend()
plt.show()