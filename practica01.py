import numpy as np

# ej 3
1 + 3
a = 7
b = a + 1
# print("b =", b)

v = np.array([1,2,3,-1])
w = np.array([2,3,0,5])
# print("v + w =", v+w)
# print("2*v =", 2*v)
# print("v**2 =", v**2)

A = np.array([[1,2,3,4,5],[0,1,2,3,4],[2,3,4,5,6],[0,0,1,2,3],[0,0,0,0,1]])
# print(A)
A[0:2,3:5]
A[:2,3:]
A[[0,2,4],:]
ind = np.array([0,2,4])
A[ind,ind]
A[ind,ind[:,None]]

# print(1j*1j)
# print((1+2j)*1j)

A = np.array([[-1,-2,-3,-4,-5],[0,1,2,3,4],[2,3,4,5,6],[0,0,1,2,3],[0,0,0,0,-1]])

# 21 a
def traza(m):
    if np.size(m) == np.size(m[0])**2:
        traza = 0
        for i in range(0, np.size(m[0])):
            traza += m[i][i]
        return traza
    else:
        return "Solo es posible con matrices cuadradas"
# print(traza(A))

# 21 b
def sum_elem(m):
    columnas = np.size(m[0])
    filas = int(np.size(m) / columnas)

    res = 0
    for i in range(0, filas):
        for j in range(0, columnas):
            res += m[i][j]
    return res
print(sum_elem(A))

# 21 c
def hay_mas_pos(m):
    columnas = np.size(m[0])
    filas = int(np.size(m) / columnas)

    positivos = 0
    negativos = 0

    for i in range(0, filas):
        for j in range(0,columnas):
            if m[i][j] >= 0:
                positivos += m[i][j]
            else:
                negativos += m[i][j]
    return positivos >= -(negativos)
print(hay_mas_pos(A))