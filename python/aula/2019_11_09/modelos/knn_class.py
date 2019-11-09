import numpy as np
from scipy.stats import mode


class KNN:

    def __init__(self, k):
        self._k = k

    def fit(self, X, y):
        self._X = X
        self._y = y

    def predict(self, X):
        predicoes = []
        for i in range(len(X)):
            distancia = X[i, :] - self._X
            distancia = np.square(distancia)
            distancia = np.sum(distancia, axis=1)

            indices = np.argsort(distancia)
            top_k = indices[:self._k]
            moda = mode(self._y[top_k])
            predicoes.append(moda.mode[0])
        return predicoes