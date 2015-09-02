# -*- coding: utf-8 -*-
#!/usr/bin/env python
# https://www.hackerrank.com/challenges/predicting-office-space-price

import sys
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

def load_data():
    arr = sys.stdin.readline().strip().split(' ')
    features = int(arr[0])
    n_rows = int(arr[1])
    train_data = []
    test_data = []
    for i in range(n_rows):
        arr = sys.stdin.readline().strip().split(' ')
        train_data.append([float(a) for a in arr])
    p_rows = int(sys.stdin.readline().strip())
    for i in range(p_rows):
        arr = sys.stdin.readline().strip().split(' ')
        test_data.append([float(a) for a in arr])
    return features, n_rows, train_data, test_data


def main():
    features, n_rows, train_data, test_data = load_data()
    train_data = np.mat(train_data)
    test_data = np.mat(test_data)
    X = train_data[:, 0:features]
    y = train_data[:, features]
    min_var = 99999
    final_degree = 2
    for degree in [2, 3, 4, 5]:
        model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
        model.fit(X, y)
        predictR = model.predict(X)
        if np.var(predictR - y) < min_var:
            final_degree = degree
            min_var = np.var(predictR - y)
    model = make_pipeline(PolynomialFeatures(final_degree), LinearRegression())
    model.fit(X, y)
    result = model.predict(test_data)
    for r in result:
        sys.stdout.write(str(r[0]) + '\n')
        #print r[0]


if __name__ == '__main__':
    main()