import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = 'household_power_consumption.txt'
df = pd.read_csv(dataset, delimiter=';', na_values=['?'])

(_, ax) = plt.subplots(1, 1, figsize=(15, 10))

df['mes'] = df.Date.apply(lambda x: int(x.split('/')[1]))
df['ano'] = df.Date.apply(lambda x: int(x.split('/')[-1]))
maxima_por_mes = df.groupby(by=['ano', 'mes'])['Voltage'].max()
x = ['_'.join(map(str, v)) for v in maxima_por_mes.index]
ax.plot(x, maxima_por_mes)
# ax.set_yscale('log')
ax.set_title('Consumo maximo por mes')
ax.set_ylabel('Voltage (log)')
ax.set_xlabel('Dia do mês')
ax.tick_params(axis='x', rotation=90)

plt.savefig('grafico.png')
