import sys
from argparse import ArgumentParser

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from knn_class import Knn


def parse_args():
    ap = ArgumentParser()

    ap.add_argument(
        '-k',
        type=int,
        required=True,
        choices=[1, 3, 5, 7, 9, 11, 13, 25],
        help='KNN K hyper parameter'
    )

    ap.add_argument(
        '-rs',
        type=int,
        required=False,
        default=42,
        help='scikit-learn random_state'
    )

    return ap.parse_args()


def main(args):
    (X, y) = load_iris(return_X_y=True)
    data = train_test_split(
        X,
        y,
        test_size=0.3,
        random_state=args.rs
    )
    (X_train, X_test, y_train, y_test) = data

    knn = Knn(k=args.k)
    knn.fit(X_train, y_train)
    preds = knn.predict(X_test)

    acuracia = sum(preds == y_test) / len(y_test)
    print(acuracia)


if __name__ == '__main__':
    args = parse_args()
    try:
        main(args)
        sys.exit(0)
    except:
        sys.exit(1)
