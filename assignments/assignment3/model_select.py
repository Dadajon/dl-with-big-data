#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 16:16:36 2021

@author: dadajonjurakuziev
"""
import pandas as pd
import numpy as np
import pickle as pk

# for dataset spliting
from sklearn.model_selection import train_test_split
from sklearn.model_selection  import cross_val_score


# visualization
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

# classification models
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC


# metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

data = pd.read_csv('data/iris.csv')
print(data.head(2))

#%%
data.describe().T

#%%
data.isnull().values.any()

#%%
data['variety'].unique()

#%%
data.groupby('variety').size()

#%%
def pre_processing(data):
    X = data[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']]
    y = data['variety']

    xtrain,xtest, ytrain, ytest = train_test_split(X,y,test_size=0.33)    
    return  xtrain,xtest, ytrain, ytest
#%%
col_names = ['sepal.length', 'sepal.width', 'petal.length', 'petal.width', 'variety']

data[col_names].plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)

plt.show()

#%%
data[col_names].hist();

#%%
scatter_matrix(data[col_names]);

#%%
xtrain,xtest, ytrain, ytest = pre_processing(data)

#%%
np.random.seed(1000)
# making a list of ml classification models
models = []

def classification_models(xtrain,xtest, ytrain, ytest ):
    models.append( ('LR',  LogisticRegression()) )
    models.append( ('CART', DecisionTreeClassifier()) )
    models.append( ('KNN', KNeighborsClassifier()) )
    models.append( ('NB',  GaussianNB()) )
    models.append( ('LDA',  LinearDiscriminantAnalysis()) )
    models.append( ('SVM',  SVC()) )

    modeloutcomes = []
    modelnames = []
    for name,model in models:
        v_results = cross_val_score(model, xtrain, ytrain, cv = 3, 
                                    scoring='accuracy', n_jobs = -1, 
                                    verbose = 0)
        print(name,v_results.mean())
        modeloutcomes.append(v_results)
        modelnames.append(name)        
    print(modeloutcomes)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xticklabels(modelnames)
    plt.boxplot(modeloutcomes)        
classification_models(xtrain,xtest, ytrain, ytest)

#%%
for name,model in models:
    trainedmodel = model.fit(xtrain,ytrain)
    
    # prediction
    ypredict = trainedmodel.predict(xtest)
    
    acc = accuracy_score(ytest,ypredict)
    classreport = classification_report(ytest,ypredict)
    confMat = confusion_matrix(ytest,ypredict)
    
    print('\n=========================', name, "=========================")
    print('The accuracy: {}'.format(acc))
    print('The Classification Report:\n {}'.format(classreport))
    print('The Confusion Matrix:\n {}'.format(confMat))
    
    with open('models/model_'+name+'.pickle','wb') as f:
        pk.dump(trainedmodel,f)
