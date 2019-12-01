from sklearn.datasets import load_iris

(X, y) = load_iris(return_X_y=True)

data = train_test_split(X, y, test_size=0.2)
(X_train, X_test, y_train, y_test) = data

# aqui é com vocês

pip install cython
pip install scikit-learn
pip uninstall scikit-learn