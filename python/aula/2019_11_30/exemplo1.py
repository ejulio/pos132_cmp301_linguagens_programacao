
# comentário
idades = [30, 24, 25, 83]
# for idade in idades:
#     print(idade)

# c = 0
# while c < 10:
#     print(c)
#     c += 1

# for (i, idade) in enumerate(idades):
#     print(i, idade)

# for i in range(len(idades)):
#     print(i, idades[i])

# for idade in idades:
#     if idade % 2 == 0:
#         print('par', idade)
#     else:
#         print('ímpar', idade)

# idades_pares = []
# for idade in idades:
#     if idade % 2 == 0:
#         idades_pares.append(idade)
# print(idades_pares)

# idades_pares = [v for v in idades if v % 2 == 0]
# print(idades_pares)

# print(idades)
# print(sorted(idades))

# for idade in idades:
#     if idade % 3 == 0:
#         pass
#     elif idade % 2 == 0:
#         pass
#     else:
#         ...

def soma(a, b=9):
    return a + b

print(soma(b=4, a=3))
print(soma(3))

print(sum(idades))

def obter_idades():
    idades = []
    while True:
        try:
            idade = int(input('Idade:'))
            idades.append(idade)
        except:
            break
    return idades

def obter_idades_2():
    while True:
        try:
            idade = int(input('Idade:'))
            yield idade
        except:
            break

# for idade in obter_idades_2():
#     if idade % 2 == 0:
#         print('par', idade)
#     else:
#         print('ímpar', idade)

def idades_fixas():
    yield 3
    yield 2
    yield 1

gen = idades_fixas()
gen1 = idades_fixas()
print(next(gen))
print(next(gen1))
print(next(gen))

b = [v ** 2 for v in range(10000000)]
b = (v ** 2 for v in range(10000000))

b = map(lambda x: x ** 2, range(10000000000000))

gen = obter_idades_2()
while True:
    try:
        idade = next(gen)
        
    except StopIteration:
        break