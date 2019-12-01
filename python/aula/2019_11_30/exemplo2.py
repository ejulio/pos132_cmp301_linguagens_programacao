import numpy as np


M = np.array([
    # idade, altura, peso
    [10, 1.3, 20],
    [34, 1.83, 79.7],
    [87, 1.6, 69],
])

print(M)

print(M[:, 1].mean())
print(np.mean(M[:, 1]))

peso = M[:, 2]
altura = M[:, 1]
imc = peso / (altura ** 2)
# imc = M[:, 2] / np.power(M[:, 1], 2)
# imc = M[:, 2] / np.square(M[:, 1])
print(imc)

# peso[1] = 100
# altura[1] = 100
# print(M)

print(np.mean(M, axis=0))
print(M.mean(axis=0))

print(M.T)

idades = np.array([13, 44, 46, 76, 87, 41])
mask = idades % 2 == 0
print(mask, idades[mask])

mask = M[:, 0] < 60
print(M[mask, :])