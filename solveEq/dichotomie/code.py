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

print(dechotomie(lambda x: x**2-2, 1, 2, 1e-4))