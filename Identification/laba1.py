C_0 = [5 - i/2 for i in range(10)]
C_left = 5
C_rigth = 0
C_0[0] = C_left
C_0[-1] = C_rigth
X = [i for i in range(10)]
delta_x = 1
delta_t = 0.1

C_2 = [5 - x**2/20 for x in X]
C_2[0] = C_left
C_2[-1] = C_rigth
level = 2

def diff(C, i):
	value = C[i+1] - 2*C[i] + C[i-1]
	# print(value, C)
	if value == 0:
		value = 1


	return value

# D = []
# for i in range(1, 9):
# 	
# 	value = C_0[i] + z * 

z = (delta_t/delta_x**2)
Di = [((C_2[i] - C_0[i])/diff(C_0, i)) * (delta_x**2/delta_t) for i in range(1, 9)]


C_check = [C_0[i] + z*Di[i-1]*diff(C_0, i) for i in range(1, 9)]
C_check.insert(0, C_left)
C_check.insert(9, C_rigth)


print(Di)
print(C_0)
print(C_check)
print(C_2)
print(C_check == C_2)