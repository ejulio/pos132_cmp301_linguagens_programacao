import logging
import sys

from datasets import Dataset


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    dataset = Dataset('./data')
    df = dataset.df
    mensagem = f'Informe uma coluna ({", ".join(df.columns)}): '
    coluna = input(mensagem).strip()
    # Qual é a alteração para ler o nome de uma coluna em loop
    # até que uma linha em branco (ou um nome especial) seja informado?

    # Ao acessar df[coluna] temos um pandas.Series
    # Documentação de pandas.Series
    # https://pandas.pydata.org/pandas-docs/stable/reference/series.html
    print(f'===== Estatísticas da coluna {coluna} =====')
    print('Quantidade itens não nulos:', df[coluna].count())
    print('Média:', round(df[coluna].mean(), 2))
    print('Desvio Padrão:', round(df[coluna].std(), 2))
    print('Variância:', round(df[coluna].var(), 2))
    print('Mediana:', round(df[coluna].median(), 2))
    print('Moda:', round(df[coluna].mode()[0], 2))
    print('Min:', round(df[coluna].min(), 2))
    print('Max:', round(df[coluna].max(), 2))
