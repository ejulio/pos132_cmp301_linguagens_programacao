from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from scipy.stats import mode


def classificar(k, train, X_test):
    (X_train, y_train) = train

    for i in range(len(X_test)):
        x = X_test[i, :]
        
        # calcula distância euclidiana
        diff_quadrado = (X_train - x) ** 2
        distancia = diff_quadrado.sum(axis=1)

        # ordena da menor para a maior distância e pega as primeiras "k" distâncias
        min_k = distancia.argsort()[:k]
        # pega o valor mais frequente (moda)
        label = mode(y_train[min_k]).mode[0]
        yield label


if __name__ == '__main__':
    (X, y) = load_iris(return_X_y=True)
    (X_train, X_test, y_train, y_test) = train_test_split(X, y, test_size=0.2, random_state=42)
    classificacoes = list(classificar(
        k=5,
        train=(X_train, y_train),
        X_test=X_test
    ))

    print('Score:', accuracy_score(y_test, classificacoes))

    # Como seria uma alteração para usar o scikit-learn?
    # https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier
