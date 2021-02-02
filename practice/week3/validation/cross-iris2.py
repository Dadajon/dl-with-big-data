import pandas as pd
from sklearn import svm, metrics, model_selection
import random, re

csv = pd.read_csv('iris.csv')

data = csv[["sepal.length", "sepal.width", "petal.length", "petal.width"]]
label = csv["variety"]

clf = svm.SVC()
scores = model_selection.cross_val_score(clf, data, label, cv=5)
print("각각의 정답률 =", scores)
print("평균 정답률 =", scores.mean())
