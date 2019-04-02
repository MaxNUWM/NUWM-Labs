from math import sin, cos, exp
import numpy as np
import matplotlib.pyplot as plt

l = 1
n = 100
h = l/n


g = lambda x: 1
p = lambda x: 1
f = lambda x: -x

def fi(x, i, x_index):
    if i == x_index:
        value = x * sin(cos(x)**i)
    else:
        value = 0
    return value
# fi = lambda x, i: x**i * exp(i*x) #9
# fi = lambda x, i, x_index: x**i * (sin(x)**i + cos(x)**i) #10
# fi = lambda x, i, x_index: x/(1 + x)**i #15 WIn
fi = lambda x, i, x_index: x * sin(cos(x)**i) #24


def dfi(x, i, x_index):
    if i == x_index:
        value = sin(cos(x)**i) - x*i*sin(x)*cos(x)**(i-1)*cos(x)**i
    else:
        value = 0
    return value

dfi = lambda x, i, x_index: sin(cos(x)**i) - x*i*sin(x)*cos(x)**(i-1)*cos(cos(x)**i)
# dfi = lambda x, i, x_index: x*1
# dfi = lambda x, i, x_index: i*x**(i-1) * (sin(x)**i + cos(x)**i - x* sin(x)*cos(x)**(i-1) + x*cos(x)*sin(x)**(i-1))

exact = lambda x: exp(1)*exp(x)/(exp(2) + 1) - exp(1)*exp(-x)/(exp(2) + 1) - x

left_boundary = 0
rigth_boundary = lambda U: U[-2]

def itegrate(f, h, X, i, j):
    return sum([f(x, i, j, x_index) * h for x_index, x in enumerate(X)])

# X = np.linspace(0, 1, 100)
# print(itegrate(lambda x, i, j: x**2, 1/100, X, 0, 0))


fig, (eq, eq_diff) = plt.subplots(1, 2)

X = np.linspace(0, l, n)

A = []
F = []
for i in range(1, n):
    ai = []
    for j in range(1, n):
        firts_int = itegrate(lambda x, i, j, x_index: p(x) * dfi(x, j, x_index) * dfi(x, i, x_index), h, X, i, j)
        sec_int = itegrate(lambda x, i, j, x_index: g(x) * fi(x, j, x_index) * fi(x, i, x_index), h, X, i, j)
        aj = firts_int + sec_int
        ai.append(aj)
    A.append(ai)
    f_i = itegrate(lambda x, i, j, x_index: f(x) * fi(x, i, x_index), h, X, i, 0)
    F.append(f_i)

A = np.array(A)
F = np.array(F)

C = np.linalg.solve(A, F)
print(len(range(1, n)))

U = [sum([C[j-1] * fi(x, j, x_index) for j in range(1, n)]) for x_index, x in enumerate(X)]

exact_U = np.array([exact(x) for x in X])
    
# for i in range(n):
#     Y1 = np.array([fi(x, i) for _, x in enumerate(X)])
#     func.plot(X, Y1, label=f'Bassis i={i}')

#     Y2 = np.array([dfi(x, i) for _, x in enumerate(X)])
#     dif.plot(X, Y2, label=f'Derivative from bassis i={i}')

eq.plot(X, U, label='U')
eq.plot(X, exact_U, label='Exact U')

eq.legend()

eq_diff.plot(X, np.abs(U - exact_U), label='Error np.abs(U - exact_U)')
eq_diff.legend()

# ax1.plot(X1, Y2)

plt.show()