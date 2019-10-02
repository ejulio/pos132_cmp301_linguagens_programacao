import logging
import sys

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


logging.basicConfig(
    level=logging.DEBUG,
    stream=sys.stdout,
)

logging.info('Carregando dataset')
(X, y) = load_diabetes(return_X_y=True)
# inspecionar
logging.debug(f'X ({type(X)}, {X.shape})')
logging.debug(f'y ({type(y)}, {y.shape})')

# verifica a média e desvio padrão das colunas
logging.debug(f'X mean: {X.mean(axis=0)}')
logging.debug(f'X std: {X.std(axis=0)}')

logging.info('Separando 20% para teste')
(X_train, X_test, y_train, y_test) = train_test_split(X, y, test_size=0.2, random_state=42)

# que tal testar com outros modelos (Lasso, Ridge, ElasticNet)?
# https://scikit-learn.org/stable/modules/classes.html#module-sklearn.linear_model
modelo = LinearRegression()
logging.info('Treinando o modelo')
modelo.fit(X_train, y_train)
logging.info('Terminou o treino do modelo')

logging.info(f'Resultado no conjunto de teste. R^2 = {modelo.score(X_test, y_test)}')

# avalia os resultados, mostrando do menor ao maior erro (diferença/residual)
resultados = modelo.predict(X_test)
# qual a diferença de list comprehension com "[]" ou "()"
# É possível mudar esse list comprehension para um map()?
# o que acontece se remover o abs()?
diffs = (abs(r - v) for (r, v) in zip(resultados, y_test))
data = sorted(zip(diffs, resultados, y_test))
for (i, (diff, resultado, valor_esperado)) in enumerate(data):
    logging.info(
        f'Resultado {i:02d}: '
        f'modelo ({round(resultado, 3)}), dataset ({valor_esperado}) '
        f'diff {round(diff, 3)}'
    )
