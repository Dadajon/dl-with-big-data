#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 16:16:18 2021

@author: dadajonjurakuziev
"""


from sklearn import svm, metrics
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.8, random_state=42)


clf = svm.SVC()
clf.fit(X_train, y_train)

predict = clf.predict(X_test)

ac_score = metrics.accuracy_score(y_test, predict)
cl_report = metrics.classification_report(y_test, predict)

print('정답률 =', ac_score)
print('리포트 =\n', cl_report)
