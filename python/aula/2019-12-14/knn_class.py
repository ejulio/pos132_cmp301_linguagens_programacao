import numpy as np
from scipy.stats import mode


class Knn:
    
    # construtor
    def __init__(self, k):
        self._k = k

    def fit(self, X_train, y_train):
        self._X_train = X_train # X_train
        self._y_train = y_train # y_train

    def predict(self, X_test):
        labels = np.zeros(shape=(len(X_test)))
        for i in range(len(X_test)):
            distancias = X_test[i] - self._X_train
            distancias = np.square(distancias)
            distancias = np.sum(distancias, axis=1)
            indices = np.argsort(distancias)
            top_k = indices[:self._k]
            top_k_labels = self._y_train[top_k]
            y_hat = mode(top_k_labels)[0][0]
            labels[i] = y_hat

        return labels
