# Fixed Point Method

is a method to solve equations of the form $f(x)=0$ by changing it to the form of $g(x)=x$. It is a root finding method that uses a fixed point of the function $g(x)$ as the starting point for iteration. The fixed point of a function $g(x)$ is a value $x$ such that $g(x)=x$. The fixed point iteration method is defined as follows:

1. write $f(x)=0$ as $g(x)=x$
2. verify that $|{g'(x)}|<1$ for all $x$ in the domain of $g(x)$
3. choose an initial value $x_0$ and a tolerance $\epsilon$
4. repeat until $|{x_{n+1}-x_n}|<\epsilon$:
    1. $x_{n+1}=g(x_n)$

## Example

We want to solve the equation $\log(x) - x^2 + 2 = 0$.

1. we can define various $g(x)$ functions
    1. $g_1(x)=\exp(x^2 - 2)$
    2. $g_2(x)=\sqrt {\log(x) + 2}$
    3. $g_3(x)=-\sqrt {\log(x) + 2}$

2. we can verify that $|{g'(x)}|<1$ for all $x$ in the domain of $g(x)$ as we can see in the following graph:

```python
import matplotlib.pyplot as plt
import numpy as np

def g1(x):
    return np.exp(x**2 - 2)

def g2(x):
    return np.sqrt(np.log(x) + 2)

def g3(x):
    return -np.sqrt(np.log(x) + 2)

x = np.linspace(0, 2, 100)
plt.plot(x, g1(x), label='g1')
plt.plot(x, g2(x), label='g2')
plt.plot(x, g3(x), label='g3')
plt.plot(x, x, label='x')
plt.legend()
plt.show()
```
