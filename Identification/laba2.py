C_0 = [5 - i/2 for i in range(10)]
C_left = 5
C_rigth = 0
C_0[0] = C_left
C_0[-1] = C_rigth
X = [i for i in range(10)]
delta_x = 1
delta_t = 0.1
q_t = lambda t: 1 + t/10

C_2 = [5 - x**2/20 for x in X]
C_2[0] = C_left
C_2[-1] = C_rigth

def diff(C, i):
	value = C[i+1] - 2*C[i] + C[i-1]
	# print(value, C)
	if value == 0:
		value = 1

	return value
k = 0
t1 = delta_t * k
Dj = (q_t(t1) * delta_x)/(C_0[1] - C_0[0])
C_next = [C_0[i] + Dj * (delta_t/delta_x**2) * diff(C_0, i) for i in range(1, 9)]
C_next.insert(0, C_left)
C_next.insert(9, C_rigth)

for k in range(5):
	t1 = delta_t * k
	Dj = (q_t(t1) * delta_x)/(C_0[1] - C_0[0])
	C_next = [C_0[i] + Dj * (delta_t/delta_x**2) * diff(C_0, i) for i in range(1, 9)]
	C_next.insert(0, C_left)
	C_next.insert(9, C_rigth)

	print(k)
	print(C_0)
	print(Dj)
	print(C_next)

	C_0 = C_next[:]

