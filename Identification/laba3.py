n = 20
X = [i for i in range(n+1)]
dt = 0.1
dx = 1

g = lambda x: x**2
g_h = lambda x: 2 + 1/100*x**2

U = [g(x) for x in X]

U_exact = [g_h(x) for x in X]

print(U)
print(U_exact)

V = []
for i, x in enumerate(X[1:-1]):
	divis = (g(X[i+1]) - g(X[i-1]))
	if divis == 0:
		divis = 1
	# value = -(g_h(x) - g(x))/dt/divis/(2*dx)
	# print(divis, (2*dx)/dt * (g_h(x) - g(x)), U[i] -  (U[i+1] - U[i-1]))
	value = (2*dx)/dt * (g_h(x) - g(x))/divis
	V.append(value)

# V = [-2*dx/dt * (g_h(x) - g(x))/(g(X[i+1]) - g(X[i-1])) for i, x in enumerate(X[1:-1])]
U_check = [U[i] - dt/(2*dx) * (U[i+1] - U[i-1]) * V[i-1] for i, x in enumerate(X[1:-1])]
U_check.insert(0, U_exact[0])
U_check.insert(len(U_check), U_exact[-1])
print(V)
print(U)
print(U_exact)
print(U_check)