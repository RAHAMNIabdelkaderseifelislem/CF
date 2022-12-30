# Dechotomie Method

is a method to solve an equation of the form $f(x)=0$.
It is based on the fact that if $f$ is continuous on $[a,b]$ and $f(a)f(b)<0$ then there is a $c\in[a,b]$ such that $f(c)=0$.
The method consists in dividing the interval $[a,b]$ in two parts $[a,c]$ and $[c,b]$ and to keep the part where $f$ changes sign.
The algorithm is the following:

1. Choose $a$ and $b$ such that $f(a)f(b)<0$.
2. Compute $c=\frac{a+b}{2}$.
3. If $f(c)=0$ then stop and return $c$.
4. If $f(a)f(c)<0$ then set $b=c$ and go to step 2.
5. If $f(c)f(b)<0$ then set $a=c$ and go to step 2.
6. If $f(a)f(b)>0$ then stop and return an error message.

## Example

We want to solve the equation $x^2-2=0$ on $[1,2]$ with a precision of $10^{-4}$.

1. We choose $a=1$ and $b=2$.
2. We compute $c=\frac{1+2}{2}=1.5$.
3. $f(c)=1.5^2-2=0.25>0$.
4. $f(a)f(c)<0$ so we set $b=c$ and go to step 2.
5. We compute $c=\frac{1+1.5}{2}=1.25$.
6. $f(c)=1.25^2-2=-0.0625<0$.
7. $f(c)f(b)<0$ so we set $a=c$ and go to step 2.
8. we can't stop because $|b-a|>10^{-4}$ so we compute $c=\frac{1.25+1.5}{2}=1.375$.
9. $f(c)=1.375^2-2=0.140625>0$.
10. $f(a)f(c)<0$ so we set $b=c$ and go to step 2.
11. we can't stop because $|b-a|>10^{-4}$ so we compute $c=\frac{1.25+1.375}{2}=1.3125$.
12. $f(c)=1.3125^2-2=-0.03125<0$.
13. $f(c)f(b)<0$ so we set $a=c$ and go to step 2.
14. we can't stop because $|b-a|>10^{-4}$ so we compute $c=\frac{1.3125+1.375}{2}=1.34375$.
15. $f(c)=1.34375^2-2=0.01171875>0$.
16. $f(a)f(c)<0$ so we set $b=c$ and go to step 2.
17. we can't stop because $|b-a|>10^{-4}$ so we compute $c=\frac{1.3125+1.34375}{2}=1.328125$.
18. $f(c)=1.328125^2-2=-0.015625<0$.
19. $f(c)f(b)<0$ so we set $a=c$ and go to step 2.
20. we can't stop because $|b-a|>10^{-4}$ so we compute $c=\frac{1.328125+1.34375}{2}=1.3359375$.
21. $f(c)=1.3359375^2-2=0.00390625>0$.
22. $f(a)f(c)<0$ so we set $b=c$ and go to step 2.
23. we can't stop because $|b-a|>10^{-4}$ so we compute $c=\frac{1.328125+1.3359375}{2}=1.3310546875$.
24. $f(c)=1.3310546875^2-2=-0.0078125<0$.
25. $f(c)f(b)<0$ so we set $a=c$ and go to step 2.
26. we can't stop because $|b-a|>10^{-4}$ so we compute $c=\frac{1.3310546875+1.3359375}{2}=1.3332672119140625$.
27. $f(c)=1.3332672119140625^2-2=0.0001220703125>0$.
28. $f(a)f(c)<0$ so we set $b=c$ and go to step 2.
29. we can't stop because $|b-a|>10^{-4}$ so we compute $c=\frac{1.3310546875+1.3332672119140625}{2}=1.3321609497070312$.
30. $f(c)=1.3321609497070312^2-2=-0.00390625<0$.
31. $f(c)f(b)<0$ so we set $a=c$ and go to step 2.
32. we can't stop because $|b-a|>10^{-4}$ so we compute $c=\frac{1.3321609497070312+1.3332672119140625}{2}=1.3327140808105469$.
33. $f(c)=1.3327140808105469^2-2=0.0001220703125>0$.
34. $f(a)f(c)<0$ so we set $b=c$ and go to step 2.
35. we stop because $|b-a|<10^{-4}$ so we return $c=\frac{1.3321609497070312+1.3332672119140625}{2}=1.3327140808105469$.

### we Can summarize the process in the following table

| $a$ | $b$ | $c$ | $f(a)$ | $f(b)$ | $f(c)$ | $f(a)f(c)$ | $f(c)f(b)$ |
|-----|-----|-----|--------|--------|--------|------------|------------|
| 1   | 2   | 1.5 | 1      | 0.25   | 0.25   | -1         | 0          |
| 1   | 1.5 | 1.25| 1      | 0.25   | -0.0625| -1         | -0.015625  |
| 1.25| 1.5 | 1.375| -0.0625| 0.25   | 0.140625| 0.009765625| 0          |
| 1.25| 1.375| 1.3125| -0.0625| 0.140625| -0.03125| -0.001953125| -0.0048828125|
| 1.3125| 1.375| 1.34375| -0.03125| 0.140625| 0.01171875| -0.0003662109375| 0|
| 1.3125| 1.34375| 1.328125| -0.03125| 0.01171875| -0.015625| 0.00048828125| -0.00018310546875|
| 1.328125| 1.34375| 1.3359375| -0.015625| 0.01171875| 0.00390625| -0.00006103515625| 0|
| 1.328125| 1.3359375| 1.3310546875| -0.015625| 0.00390625| -0.0078125| 0.0001220703125| -0.000030517578125|
| 1.3310546875| 1.3359375| 1.3332672119140625| -0.0078125| 0.00390625| 0.0001220703125| -9.5367431640625e-07| 0|
| 1.3310546875| 1.3332672119140625| 1.3321609497070312| -0.0078125| 0.0001220703125| -0.00390625| 3.0517578125e-05| -4.76837158203125e-07|
| 1.3321609497070312| 1.3332672119140625| 1.3327140808105469| -0.00390625| 0.0001220703125| 0.0001220703125| -4.76837158203125e-07| 0|


## Implementation

The following code implements the dechotomie method.

```python
def dechotomie(f, a, b, eps):
    while abs(b-a) > eps:
        c = (a+b)/2
        if f(c) == 0:
            return c
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
    return (a+b)/2
```

## Example

We want to solve the equation $x^2-2=0$ on $[1,2]$ with a precision of $10^{-4}$.

```python
>>> dechotomie(lambda x: x**2-2, 1, 2, 1e-4)
1.3327140808105469
```
