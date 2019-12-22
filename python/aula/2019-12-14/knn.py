from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
from scipy.stats import mode


(X, y) = load_iris(return_X_y=True)

data = train_test_split(X, y, test_size=0.3, random_state=1)
(X_train, X_test, y_train, y_test) = data

test = X_test[0, :]

distancias = np.zeros(shape=(len(X_train)))
for i in range(len(X_train)):
    diff = test - X_train[i]
    #diff = diff ** 2
    diff = np.square(diff)
    diff = np.sum(diff)
    distancias[i] = diff

k = 5

indices = np.argsort(distancias)
top_k = indices[:k]
top_k_labels = y_train[top_k]
y_hat = mode(top_k_labels[0][0])
