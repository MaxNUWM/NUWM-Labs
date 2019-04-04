from math import sin, cos, exp, log
import numpy as np
import matplotlib.pyplot as plt

l = 1
n = 20
h = 1/20


g = lambda x: 1
p = lambda x: 1
f = lambda x: -x

fi = lambda x, i: x * (x-1)**(i+1)
dfi = lambda x, i: (x-1)**i * (x*(i+2) - 1)
ddfi = lambda x, i: (i+1)*(x-1)**(i-1)*(x*(i+2)-2)

psi = lambda x, i: x*2**(i*x)
psi = lambda x, i: x*cos(i*x)
psi = lambda x, i: x*cos(x)**i

exact = lambda x: exp(1)*exp(x)/(exp(2) + 1) - exp(1)*exp(-x)/(exp(2) + 1) - x

left_boundary = 0
rigth_boundary = lambda U: U[-2]

def itegrate(f, h, X, i, j):
    return sum([f(x, i, j) * h for x_index, x in enumerate(X)])

fig, (eq, eq_diff) = plt.subplots(1, 2)

X = np.linspace(0, l, n)

A = []
F = []
for i in range(1, n):
    ai = []
    for j in range(1, n):
        firts_int = itegrate(lambda x, i, j:  ddfi(x, j) * psi(x, i), h, X, i, j)
        sec_int = itegrate(lambda x, i, j: g(x) * fi(x, j) * psi(x, i), h, X, i, j)
        aj = - firts_int + sec_int
        ai.append(aj)
    A.append(ai)
    f_i = itegrate(lambda x, i, j: f(x) * psi(x, i), h, X, i, 0)
    F.append(f_i)

A = np.array(A)
F = np.array(F)

C = np.linalg.solve(A, F)

U = [sum([C[j-1] * fi(x, j) for j in range(1, n)]) for x_index, x in enumerate(X)]

exact_U = np.array([exact(x) for x in X])

eq.plot(X, U, label='U')
eq.plot(X, exact_U, label='Exact U')
eq.legend()

eq_diff.plot(X, np.abs(U - exact_U), label='Error np.abs(U - exact_U)')
eq_diff.legend()

plt.show()