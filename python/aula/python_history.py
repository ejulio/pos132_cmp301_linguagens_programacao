# Este arquivo contém os comandos executados no shell interativo do python
# durante a aula.
# lembre-se que eles foram executados em momentos diferentes, mas o conteúdo
# deve ajudar quem perdeu alguma parte desse momento
quit()
1
2 / 3
a = 21
print(a)
print('Hellow worlds')
print('Hellow world')
numeros = [1, 2, 3, 4]
len(numeros)
range(3)
list(range(3))
list(range(3, 10))
import this
import numpy as np
help(np.random.randint)
dir(np.random)
import csv
f = open('household_power_consumption.txt', 'r')
f.read()
f.seek(0)
help(csv.DictReader)
r = csv.DictReader(f)
r[0]
next(r)
r = csv.DictReader(f, delimiter=';')
next(r)
import pandas as pd
df = pd.read_csv('household_power_consumption.txt')
len(df)
df.head(5)
df.columns
len(df.columns)
df = pd.read_csv('household_power_consumption.txt', delimiter=';')
len(df.columns)
df.columns
df.head(5)
df = pd.read_csv('household_power_consumption.txt', delimiter=';', nrows=10000)
len(df)
df.info()
df = pd.read_csv('household_power_consumption.txt', delimiter=';', nrows=10000, na_values=['?'])
df.info()
df.describe()
a = df.describe()
type(a)
a['Sub_metering_3']
df['Sub_metering_3']
df['Sub_metering_3'].mean()
df['Sub_metering_3'].std()
import numpy as np
np.mean(df['Sub_metering_3'])
df.mean()
df.max()
collulna = 'Date'
coluna = 'Date'
df[coluna]
df.Date
df.query('"/12/" in Date')
df['ano'] = df.Date.apply(lambda x: int(x.split('/')[-1]))
df.ano
eh_par = lambda x: x % 2 == 0
eh_par(2)
eh_par(3)
'18/12/2006'.split()
'18/12/2006'.split('/')
'18/12/2006'.split('/')[0]
'18/12/2006'.split('/')[1]
'18/12/2006'.split('/')[2]
'18/12/2006'.split('/')[-1]
'18/12/2006'.split('/')[-2]
'18/12/2006'.split('/')[-3]
df = pd.read_csv('household_power_consumption.txt', delimiter=';', na_values=['?'])
df['ano'] = df.Date.apply(lambda x: int(x.split('/')[-1]))
df.ano
df[df.ano == 2010]
df.ano == 2010
df[df.ano == 2010]
df[df.ano < 2010]
df.query('ano == 2010')
import numpy as np
numeros = np.array([1, 2, 3, 4, 5])
numeros
numeros[[True, True, False, False, False]]
numeros[numeros % 2 == 0]
numeros % 2 == 0
numeros[numeros % 2 == 0] = 100
numeros
numeros[2:]
numeros[:3]
numeros = list(range(10))
numeros
numeros[1]
numeros[-1]
numeros[0:5]
numeros[:5]
numeros[2:5]
numeros[-1:-3]
numeros[-3:-1]
numeros[:5]
numeros[:5:1]
numeros[:5:2]
numeros[:5:3]
numeros[:5:1]
numeros[::]
numeros[::-1]
numeros = tuple(range(10))
numeros
numeros[::-1]
numeros = list(range(10))
numeros
numeros[1] = 10
numeros
numeros.append(9)
numeros
numeros = tuple(range(10))
numeros
numeros[1] = 10
numeros.append
tupla = (1, 2)
tupla
a = [1]
a
b = (1)
b
b = (1,)
b
[1, 2] + [3, 4]
(1, 2) + (3, 4)
lista = [10] * 10
lista
lista = [[]] * 10
lista
lista[0].append(1)
lista
set([1, 2, 3, 4])
{1, 2, 3, 4}
{1, 2, 3, 4, 4}
{1, 2, 3, 4, 4} + {2, 3}
{1, 2, 3, 4, 4} | {2, 3}
{1, 2, 3, 4, 4} | {2, 5}
{1, 2, 3, 4, 4} - {2, 5}
{1, 2, 3, 4, 4} & {2, 5}
a = {'Blumenau', 'Pomerode'}
a
'Gaspar' in a
'Blumenau' in a
'Blumenau' in ['Bnu', 'Blu']
'Blumenau' in ['Bnu', 'Blumenau']
'Blumenau' in 'Blumenau, Gaspar, Indaial'
{'chave': 'valor'}
pessoas = {'id': 'Júlio'}
pessoas
pessoas['id']
'id' in pessoas
'id2' in pessoas
pessoas['id2'] = 'João'
pessoas
'id2' in pessoas
pessoas['id3']
pessoas.get('id3')
if 'id3' in pessoas:
	pessoas['id3']
pessoas.keys()
pessoas.values()
pessoas.items()
list(pessoas)
(a, b) = ('a', 'b')
a
b
(a, b, c) = ('a', 'b', 45)
a
b
c
(a, b, c) = ['a', 'b', 45]
a
b
c
a, b, c = ['a', 'b', 45]
a
b
c
a, b= {'a': 21, 'b': 45}
a
b
a = list(range(10))
a
a[0]
(b, *_) = a
b
_
(*_, b) = a
b
a
(c, *_, b) = a
c
b
