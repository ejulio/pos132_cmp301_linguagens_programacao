import numpy as np

# idades = np.random.randint(24, 50, size=31)
# print(idades.mean())
# print(np.mean(idades))
# print(mean(idades))
# print(int(mean(idades)))
# print(np.median(idades))
# print(idades)

idades1 = np.random.normal(30, 3, size=31).astype(np.int)
idades2 = np.random.normal(30, 3, size=31).astype(np.int)

print(idades1)

idades1 = np.random.normal(30, 3, size=31)
print(np.round(idades1, 3))
# diff = idades1 - idades2
# print(np.round(diff.mean(), 3))
