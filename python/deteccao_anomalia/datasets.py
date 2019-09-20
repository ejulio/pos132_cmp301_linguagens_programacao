import logging
import io
from os import path
import zipfile

import requests
import pandas as pd


class Dataset:

    def __init__(self, diretorio_dataset):
        self._df = None
        self._diretorio_dataset = diretorio_dataset
        self._caminho_dataset = path.join(
            diretorio_dataset,
            'household_power_consumption.txt'
        )

    @property
    def df(self):
        if self._df is None:
            self._download_dataset()
            self._df = self._ler_dataset()
        return self._df

    def _download_dataset(self):
        if path.exists(self._caminho_dataset):
            logging.info('Dataset já existe....')
            return

        logging.info('Fazendo download do dataset....')

        url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00235/household_power_consumption.zip'  # noqa
        response = requests.get(url)
        if not response.ok:
            raise Exception('Ocorreu um erro ao baixar o dataset')

        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            z.extractall(self._diretorio_dataset)

        logging.info('Terminou o download do dataset....')

    def _ler_dataset(self):
        df = pd.read_csv(
            self._caminho_dataset,
            sep=';',
            na_values=['?'],
            # nrows=100000  # remova o comentário para carregar apenas uma parte dos dados
        )
        return df
