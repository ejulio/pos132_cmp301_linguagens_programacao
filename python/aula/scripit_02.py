import numpy as np

idades = np.random.randint(24, 50, size=30)

for (i, idade) in enumerate(idades):
    print(i, idade)

print(sum(idades))

idades2 = np.random.randint(24, 50, size=30)

for i in range(len(idades)):
    print(i, idades[i], idades2[i])

for (idade1, idade2) in zip(idades, idades2):
    print(idade1, idade2)

for (i, (idade1, idade2)) in enumerate(zip(idades, idades2)):
    print(i, idade1, idade2)

media = idades.mean()
diffs = []
for idade in idades:
    diffs.append(idade - media)
print(diffs)

diffs = [idade - media for idade in idades]
diffs = [idade - media for idade in idades if idade % 2 == 0]

diffs = (idade - media for idade in idades if idade % 2 == 0)
print(diffs)

diffs = filter(lambda idade: idade % 2 == 0, idades)
diffs = map(lambda idade: idade - media, diffs)
# print(next(diffs))