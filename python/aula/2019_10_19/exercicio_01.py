import pandas as pd

dataset = 'household_power_consumption.txt'
df = pd.read_csv(dataset, delimiter=';', na_values=['?'])
df['ano'] = df.Date.apply(lambda x: int(x.split('/')[-1]))

df_2006_2009 = df[df.ano < 2010]
df_2010 = df[df.ano == 2010]

mean = df_2006_2009.Voltage.mean()
std = df_2006_2009.Voltage.std()

anomalias = (df_2010.Voltage - mean).abs() > (2 * std)

print(df_2010[anomalias])
# print(anomalias)
