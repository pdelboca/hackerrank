# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 15:55:49 2015

@author: pdelboca
"""
import sys
import numpy as np
from sklearn.linear_model import LinearRegression


def load_data():
    arr = sys.stdin.readline().strip().split(" ")
    features, examples = [int(a) for a in arr]
    train_data = np.empty((0,features+1), float)    
    for i in range(examples):
        arr = sys.stdin.readline().strip().split(" ")
        train_data = np.vstack([train_data, [float(a) for a in arr]])
    p_rows = int(sys.stdin.readline().strip())
    pred_data = np.empty((0,features), float)    
    for i in range(p_rows):
        arr = sys.stdin.readline().strip().split(" ")
        pred_data = np.vstack([pred_data, [float(a) for a in arr]])
    return features, examples, train_data, pred_data
    
def main():
    features, examples, train_data, pred_data = load_data()
    X = train_data[:,0:features]
    y = train_data[:,features]
    model = LinearRegression(normalize=True)
    model.fit(X, y)
    pred = model.predict(pred_data)
    for p in pred:
        sys.stdout.write(str(p) + '\n')
    
    
if __name__ == '__main__':
    main()