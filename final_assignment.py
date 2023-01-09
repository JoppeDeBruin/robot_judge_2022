# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 10:36:06 2022

@author: joppe
"""



import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import balanced_accuracy_score

np.random.seed(12345)

X = np.random.normal(0, 1, size = (1100, 5))
y = np.append(np.ones(1000), np.zeros(100))


# The data is slightly unbalanced, so let's sample some extra ones to make the data balanced

y0 = y[y==0]
y1 = y[y==1]
X0 = X[y==0, :]
X1 = X[y==1, :]

y0_appended = y0
X0_appended = X0

for j in range(len(y1)-len(y0)):
    index = np.random.randint(0, len(y0))
    y0_appended = np.append(y0_appended, y0[index])
    X0_appended = np.append(X0_appended, X0[index,:].reshape(1,-1), axis = 0)

X_appended = np.append(X0_appended, X1, axis = 0)
y_appended = np.append(y0_appended, y1, axis = 0)

X_train, X_test, y_train, y_test = train_test_split(X_appended, y_appended, test_size = 0.5, random_state = 12)

model = RandomForestClassifier(n_estimators = 10)
model.fit(X_train, y_train)

print(balanced_accuracy_score(y_test, model.predict(X_test)))


########### With the proper split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.5, random_state = 12)

y0_train = y_train[y_train == 0]
y1_train = y_train[y_train == 1]
X0_train = X_train[y_train == 0, :]
X1_train = X_train[y_train == 1, :]

y0_train_appended = y0_train
X0_train_appended = X0_train

for j in range(len(y1_train)-len(y0_train)):
    index = np.random.randint(0, len(y0_train))
    y0_train_appended = np.append(y0_train_appended, y0_train[index])
    X0_train_appended = np.append(X0_train_appended, X0_train[index, :].reshape(1,-1), axis = 0)


X_train_appended = np.append(X0_train_appended, X1_train, axis = 0)
y_train_appended = np.append(y0_train_appended, y1_train, axis = 0)

model2 = RandomForestClassifier(n_estimators = 10)
model2.fit(X_train_appended, y_train_appended)

print(balanced_accuracy_score(y_test, model2.predict(X_test)))



