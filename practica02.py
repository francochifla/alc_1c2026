# ej 18
import numpy as np

v = np.random.random(3)
norma2_v = np.linalg.norm(v)
x = v/norma2_v

# print(np.linalg.norm(x))
# print(x)

def sucesion(A):

    n = A.shape[0]

    sucesion_res = []
    max_norma2 = 0

    for i in range(100):

        v = np.random.uniform(-1, 1, n)
        norma_v = np.linalg.norm(v)
        x = v / norma_v

        y = A @ x
        norma_y = np.linalg.norm(y)

        if norma_y > max_norma2:
            max_norma2 = norma_y
        
        sucesion_res.append(max_norma2)

    return sucesion_res

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(sucesion(A))


import matplotlib.pyplot as plt

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
res = sucesion(A)
valor_exacto = np.linalg.norm(A, 2)

# Configuración del gráfico
plt.figure(figsize=(10, 5))
plt.plot(res, label="Estimación (s_k)", color="cyan", linewidth=2)
plt.axhline(y=valor_exacto, color="red", linestyle="--", label=f"Valor exacto ({valor_exacto:.4f})")

plt.title("Evolución de la estimación de ||A||2")
plt.xlabel("Número de iteración")
plt.ylabel("Valor")
plt.legend()
plt.grid(True, alpha=0.3)
# En lugar de plt.show()
plt.savefig('mi_grafico.png')
print("Gráfico guardado como mi_grafico.png")