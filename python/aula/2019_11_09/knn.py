from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
from scipy.stats import mode


(X, y) = load_iris(return_X_y=True)

data = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=1
)

(X_train, X_test, y_train, y_test) = data
# X_train, y_train = o que eu conheço
# X_test, y_test = o que eu quero descobrir


k = 7
predicoes = []
for i in range(len(X_test)):
    distancias = []
    for j in range(len(X_train)):
        distancia = X_test[i, :] - X_train[j, :]
        distancia = np.square(distancia)
        distancia = np.sum(distancia)

        distancias.append(distancia)

    indices = np.argsort(distancias)
    top_k = indices[:k]
    
    labels = y_train[top_k]
    moda = mode(labels)
    predicoes.append(moda.mode[0])


acuracia = [p == yt for (p, yt) in zip(predicoes, y_test)]

acuracia = float(sum(acuracia)) / len(acuracia)
print(acuracia)