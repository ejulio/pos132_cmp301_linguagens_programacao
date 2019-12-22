import matplotlib.pyplot as plt
import numpy as np


(fig, ax) = plt.subplots(1, 1, figsize=(15, 10))


# idades = np.random.normal(30, 4, size=200).astype(int)
# idades = np.random.exponential(1, size=200)
# idades *= 25
# ax.hist(idades, bins=20)

paises = np.random.choice([0, 1, 2], size=1000)
desemprego = np.random.normal(10, 2, size=1000)
inflacao = np.random.normal(3, 0.1, size=1000)
# inflacao = desemprego + np.random.normal(3, 0.1, size=1000)

# inflacao_por_pais = dict()
# for (p, d, i) in zip(paises, desemprego, inflacao):
#     ip = inflacao_por_pais.get(p, [])
#     ip.append((d, i))
#     inflacao_por_pais[p] = ip

# cores = ('r', 'g', 'b')
# for (cor, valores) in zip(cores, inflacao_por_pais.values()):
#     ax.scatter(
#         [v[0] for v in valores],
#         [v[1] for v in valores],
#         color=cor,
#         marker='o',
#         # alpha=0.1
#     )

# cores = ('r', 'g', 'b')
# ax.scatter(
#     desemprego,
#     inflacao,
#     color=[cores[p] for p in paises]
# )

marcas = np.random.choice([1, 2, 3], size=1000)
contagem = dict()
for m in marcas:
    contagem[m] = len([m1 for m1 in marcas if m1 == m])

ax.bar(
    contagem.keys(),
    contagem.values()
)

ax.set_title('Desemprego x Inflação')
ax.set_xlabel('Desemprego')
ax.set_ylabel('Inflação')

plt.savefig('./grafico.png')
