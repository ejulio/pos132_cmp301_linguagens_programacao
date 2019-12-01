import numpy as np
import pandas as pd

df = pd.read_csv(
    'household_power_consumption.txt',
    delimiter=';',
    # nrows=50000,
    na_values=['?']
)

def parse_ano(data):
    return int(data.split('/')[-1])

df['ano'] = df.Date.apply(parse_ano)

# parse_ano_2 = lambda data: int(data.split('/')[-1])
# df['ano'] = df.Date.apply(parse_ano_2)
# df['ano'] = df.Date.apply(lambda x: int(x.split('/')[-1]))
# print(df.groupby(by=['ano']).Voltage.mean())
# print(df.groupby(by=['ano']).agg({
#     'Voltage': ['mean', 'max', 'min', 'median'],
#     # 'Global_intensity': ['mean', 'max', 'min', 'median'],
# }))

# print(df.ano.value_counts())

ano_referencia = 2010
# df_anterior = df[df.ano < ano_referencia]
# df_anterior = df.query('ano < %d' % ano_referencia)
# df_anterior = df.query('ano < {}'.format(ano_referencia))
df_anterior = df.query(f'ano < {ano_referencia}')

df_referencia = df.query(f'ano == {ano_referencia}')

media = df_anterior.Voltage.mean()
desvio_padrao = df_anterior.Voltage.std()

print(media, desvio_padrao)

# mask = np.abs(df_referencia.Voltage - media) > 2 * desvio_padrao
mask = (df_referencia.Voltage - media).abs() > 2 * desvio_padrao

print(len(df_referencia), len(df_referencia[mask]))

media = df_referencia[mask].Voltage.mean()
std = df_referencia[mask].Voltage.std()

print(media, std)
print(df_referencia[mask].Voltage.min())