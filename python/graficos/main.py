from argparse import ArgumentParser
import io
from os import path, mkdir
import zipfile

import requests
import pandas as pd
import matplotlib.pyplot as plt


def parse_args():
    ap = ArgumentParser()

    ap.add_argument(
        '--grafico',
        type=str,
        required=True,
        choices=['histograma', 'scatter', 'barra', 'linha'],
        help='Qual gráfico você deseja criar?'
    )

    ap.add_argument(
        '--arquivo-saida',
        type=str,
        required=True,
        help='Onde deve ser salvo o arquivo com o gráfico?'
    )

    return ap.parse_args()


def download_dataset(diretorio_para_extrair):
    if path.exists(path.join(diretorio_para_extrair, 'household_power_consumption.txt')):
        print('Dataset já existe....')
        return

    print('Fazendo download do dataset....')

    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00235/household_power_consumption.zip'  # noqa
    response = requests.get(url)
    if not response.ok:
        raise Exception('Ocorreu um erro ao baixar o dataset')

    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        z.extractall(diretorio_para_extrair)

    print('Terminou o download do dataset....')


def ler_dataset(diretorio_dataset):
    df = pd.read_csv(
        path.join(diretorio_dataset, 'household_power_consumption.txt'),
        sep=';',
        na_values=['?'],
        # nrows=100000  # remova o comentário para carregar apenas uma parte dos dados
    )
    df = df.dropna()
    return df

def histograma(df, ax):
    ax.hist(df.Voltage, bins=30)
    ax.set_title('Histograma de "Voltage"')
    ax.set_ylabel('Quantidade observações')
    ax.set_xlabel('Voltage')


def scatter(df, ax):
    hora = df.Time.apply(lambda x: int(x[:2]))
    ax.scatter(hora, df.Voltage, alpha=0.1)
    ax.set_title('Scatter de "Voltage" por Hora')
    ax.set_ylabel('Voltage')
    ax.set_xlabel('Hora')


def barra(df, ax):
    df['dia'] = df.Date.apply(lambda x: int(x.split('/')[0]))
    media_por_dia = df.groupby(by='dia')['Voltage'].mean()
    ax.bar(media_por_dia.index, media_por_dia)
    ax.set_yscale('log')
    ax.set_title('Consumo de Voltage médio (log) por dia do mês')
    ax.set_ylabel('Voltage (log)')
    ax.set_xlabel('Dai do mês')


def linha(df, ax):
    df['mes'] = df.Date.apply(lambda x: int(x.split('/')[1]))
    df['ano'] = df.Date.apply(lambda x: int(x.split('/')[-1]))
    maxima_por_mes = df.groupby(by=['ano', 'mes'])['Voltage'].max()
    x = ['_'.join(map(str, v)) for v in maxima_por_mes.index]
    ax.plot(x, maxima_por_mes)
    # ax.set_yscale('log')
    ax.set_title('Consumo de Voltage médio (log) por dia do mês')
    ax.set_ylabel('Voltage (log)')
    ax.set_xlabel('Dia do mês')
    ax.tick_params(axis='x', rotation=90)


if __name__ == '__main__':
    args = parse_args()
    (caminho_diretorio, _) = path.split(args.arquivo_saida)
    if not path.exists(caminho_diretorio):
        mkdir(caminho_diretorio)
    
    download_dataset(diretorio_para_extrair='./data')
    df = ler_dataset('./data')

    (_, ax) = plt.subplots(1, 1, figsize=(15, 10))
    if args.grafico.lower() == 'histograma':
        histograma(df, ax)
    elif args.grafico.lower() == 'scatter':
        scatter(df, ax)
    elif args.grafico.lower() == 'barra':
        barra(df, ax)
    elif args.grafico.lower() == 'linha':
        linha(df, ax)

    plt.savefig(args.arquivo_saida)
