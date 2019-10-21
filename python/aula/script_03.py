import numpy as np
import pandas as pd


class DeteccaoAnomalia:

    def __init__(self, df, coluna):
        self._coluna = coluna
        self._mean = df[coluna].mean()
        self._std = df[coluna].std()

    def detectar(self, df):
        diffs = np.abs(df[self._coluna] - self._mean)
        return diffs > (2 * self._std)


if __name__ == '__main__':
    dataset = 'household_power_consumption.txt'
    df = pd.read_csv(dataset, delimiter=';', na_values=['?'])
    df['ano'] = df.Date.apply(lambda x: int(x.split('/')[-1]))

    df_2006_2009 = df[df.ano < 2010]
    df_2010 = df[df.ano == 2010]

    modelo = DeteccaoAnomalia(df_2006_2009, coluna='Voltage')
    anomalias = modelo.detectar(df_2010)
    print(df_2010[anomalias])