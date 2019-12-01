from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

(X, y) = load_diabetes(return_X_y=True)

data = train_test_split(X, y, test_size=0.2)
(X_train, X_test, y_train, y_test) = data

print(X_train.shape, X_test.shape)
print(y_train.shape, y_test.shape)

lr = LinearRegression()
lr.fit(X_train, y_train)
score = lr.score(X_test, y_test)
print(score)

preds = lr.predict(X_test)
print(preds)
