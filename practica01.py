import numpy as np

# ej 1
ec = np.array([[1, 1, -2, 1], [3, -2, 1, 5], [1, -1, 1, 2]])
sol = np.array([-2, 3, 2])
res = np.linalg.solve(ec, sol)
print(res)
