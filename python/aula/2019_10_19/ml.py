from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
import numpy as np


(X, y) = load_diabetes(return_X_y=True)

data = train_test_split(X, y, test_size=0.2, random_state=1)
(X_train, X_test, y_train, y_test) = data

modelo = Ridge()
modelo.fit(X_train, y_train)

y_hat = modelo.predict(X_test)

# print(modelo.score(X_test, y_test))

# print(np.sqrt(np.square(y_hat - y_test).mean()))


from sklearn.datasets import load_iris

(X, y) = load_iris(return_X_y=True)
data = train_test_split(X, y, test_size=0.2, random_state=1)
(X_train, X_test, y_train, y_test) = data

p1 = X_train[0, :]
p2 = X_test[0, :]

distancia = np.sum((p1 - p2) ** 2)
print(distancia)