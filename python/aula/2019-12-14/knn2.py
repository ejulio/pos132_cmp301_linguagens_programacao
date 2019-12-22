from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
from scipy.stats import mode


(X, y) = load_iris(return_X_y=True)

data = train_test_split(X, y, test_size=0.3, random_state=1)
(X_train, X_test, y_train, y_test) = data
k = 5

labels = np.zeros(shape=(len(X_test)))
for i in range(len(X_test)):
    # a operação vetorizada no numpy faz a subtração elemento a elemento do vetor
    # aqui, ainda tem a operação de broadcasting, porque
    # X_test[i] é um vetor 1 x M e X_train é uma matriz N x M
    # o broadcasting vai replicar os valores de X_test[i] em cada linha
    # para que X_test[i] seja N x M
    distancias = X_test[i] - X_train
    distancias = np.square(distancias)  # ao quadrado
    # distancias é uma matriz de N x M
    # porém o resultado esperado é N x 1 (distância de uma amostra para as demais N)
    # np.sum() soma os valores, axis=1 indica que a soma é das colunas
    distancias = np.sum(distancias, axis=1)
    # obtém os índices ordenados, ao invés dos elementos ordenados
    indices = np.argsort(distancias)
    top_k = indices[:k]
    top_k_labels = y_train[top_k]
    y_hat = mode(top_k_labels)[0][0]
    labels[i] = y_hat

acertos = np.sum(labels == y_test)
print(acertos / len(X_test))
