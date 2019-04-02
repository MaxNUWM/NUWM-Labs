n = 20
X = [i-10 for i in range(n)]
dt = 0.1
dx = 1

g = lambda x: x**2
g_h = lambda x: 2 + 1/100*x**2

U = [g(x) for x in X]

U_exact = [g_h(x) for x in X]

# print(U)
# print(U_exact)

def diff(C, i):
	value = C[i+1] - C[i]
	# print(value, C)
	if value == 0:
		value = 1


	return value

z = (dt/dx)
V = [(g_h(X[i]) - g(X[i]))/diff(U, i) * dx/dt for i in range(1, 19)]
# V = []
# for i, x in enumerate(X[1:-1]):
# 	divis = (g(X[i+1]) - g(X[i])) * (dt)/dx
# 	# if divis == 0:
# 	# 	divis = 0.00000001
# 	# value = -(g_h(x) - g(x))/dt/divis/(2*dx)
# 	# print(divis, (2*dx)/dt * (g_h(x) - g(x)), U[i] -  (U[i+1] - U[i-1]))
# 	value = -(g(x) - g_h(x))/divis
# 	V.append(round(value, 3))

# V = [-2*dx/dt * (g_h(x) - g(x))/(g(X[i+1]) - g(X[i-1])) for i, x in enumerate(X[1:-1])]

U_check = []
for i, x in enumerate(X[0:-1]):
	val = U[i] + dt/(dx) * (U[i+1] - U[i]) * V[i-1]
	# print(i, (U[i+1] - U[i]), U)
	U_check.append(val)
# U_check = [U[i] - dt/(dx) * (U[i+1] - U[i]) * V[i-1] for i, x in enumerate(X[1:-1]):]
U_check[0] = U_exact[0]
U_check.insert(len(U_check), U_exact[-1])
print(V)
print(U)
print(U_exact)
print(U_check)