# Horner method

is method to find the value of a polynomial at a given point. It is a fast way to evaluate a polynomial. and also a way to find the roots of a polynomial.

## Example

We want to evaluate the polynomial $f(x) = x^3 + 2x^2 - 5x + 3$ at $x = 2$.

1. we can define the polynomial $f(x)$

```python
import numpy as np

def f(x):
    return x**3 + 2*x**2 - 5*x + 3
```

2. we can define the horner method

```python
def horner(f, x, a):
    n = len(a) - 1
    p = a[n]
    for i in range(n-1, -1, -1):
        p = p*x + a[i]
    return p
```

3. we can evaluate the polynomial at $x = 2$

```python
a = [3, -5, 2, 1]

x = 2

p = horner(f, x, a)

print(p)
```

result:

```python
9
```

we can sumrize the result in a table:

| $a_k$ | 1 | 2 | -5 | 3 |
|-------|---|---|----|---|
| $x=2$ |   | 2 | 8  | 6 |
| $p$   | 1 | 4 | 3  | 9 |

now we can also write $f(x)$ as: $f(x) = (x-2)\times(1x^3 + 4x^2 + 3x) + 9$

## Implementation and Plot

```python
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
```

