import logging
import sys

from datasets import Dataset


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    df = Dataset('./data').df

    df['ano'] = df.Date.apply(lambda x: int(x.split('/')[-1]))
    entre_2006_e_2009 = df[df.ano.between(2006, 2009)]
    em_2010 = df.query('ano == 2010').copy()

    mu = entre_2006_e_2009.Voltage.mean()
    std = entre_2006_e_2009.Voltage.std()

    em_2010['anomalia'] = (em_2010.Voltage - mu).abs() > 2 * std
    # outra opção:
    # em_2010['anomalia'] = em_2010.Voltage.apply(lambda x: abs(x - mu) > 2 * std)
    em_2010['anomalia'] = em_2010['anomalia'].astype(int)
    em_2010['anomalia'].to_csv(
        './data/resultado.csv',
        header=True,
        index_label='index'
    )
