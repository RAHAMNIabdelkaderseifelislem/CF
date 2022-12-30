# Newton Raphson method

is a method to solve equations of the form $f(x)=0$ by using the first derivative of the function $f(x)$. It is a root finding method that uses the tangent line of the function $f(x)$ as the starting point for iteration. The Newton Raphson method is defined as follows:

1. choose an initial value $x_0$ and a tolerance $\epsilon$
2. repeat until $|{x_{n+1}-x_n}|<\epsilon$:
    1. $x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}$

## Example

We want to solve the equation $\log(x) - x^2 + 2 = 0$.

1. we can define the function $f(x)$ and its derivative $f'(x)$

```python
import numpy as np

def f(x):
    return np.log(x) - x**2 + 2

def df(x):
    return 1/x - 2*x
```

2. we can choose an initial value $x_0$ and a tolerance $\epsilon$

```python
x0 = 0.3
eps = 0.001
```

3. we can repeat until $|{x_{n+1}-x_n}|<\epsilon$:

```python
def newtonRaphson(f, df, x0, eps):
    x = x0
    while True:
        x1 = x - f(x)/df(x)
        if abs(x1 - x) < eps:
            return x1
        x = x1
```

4. we can solve the equation

```python
x = newtonRaphson(f, df, x0, eps)
print(x)
```

result:

```python
0.5671432904097838
```

## Convergence

The Newton Raphson method converges quadratically. It means that the error is reduced by a factor of 4 at each iteration. The following graph shows the convergence of the Newton Raphson method:

```python
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
```
