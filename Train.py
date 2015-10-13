__author__ = 'Xteeven'

import numpy as np
import neurolab as nl
import mlpy
import matplotlib.pyplot as plt
import time
from sklearn.lda import LDA
from sklearn.qda import QDA
from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn import neighbors, datasets
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix


datos = np.loadtxt('datasetnew.txt', delimiter=',')
x, y = datos[:, :10], datos[:, 10].astype(np.int)

# x = x - np.mean(x, axis=0)
xn = x / np.sqrt(np.sum(x**2, axis=0))
kfold = mlpy.cv_kfold(len(xn), len(xn))

#-----------------------------------------------------------
# percent = []
# # 0.722916666667
# result = []
# classifier = LDA()
# classifier.fit(xn, y)
# for crossval in range(len(kfold)):
#     trainindex = kfold[crossval][0].tolist()
#     evaluateindex = kfold[crossval][1].tolist()
#     trainx = xn[trainindex]
#     trainy = y[trainindex]
#     evaluatex = xn[evaluateindex]
#     evaluatey = y[evaluateindex]
#
#     classifier.fit(trainx, trainy)
#     result.append(classifier.predict(evaluatex) == evaluatey)
#
# print float(sum(result))/len(result)
#
#-----------------------------------------------------------
# X_train, X_test, y_train, y_test = train_test_split(
#     xn, y, test_size=0.1, random_state=0)
#
# gam = np.arange(1, 10).tolist()
# tuned_parameters = [{'weights': ['uniform', 'distance'], 'n_neighbors': gam}]
# clfa = neighbors.KNeighborsClassifier()
# clf = GridSearchCV(clfa, tuned_parameters, cv=5)
# clf.fit(X_train, y_train)
# print(clf.best_params_)
#
# result = []
# 0.735416666667 {'n_neighbors': 4, 'weights': 'distance'}
# classifier = neighbors.KNeighborsClassifier(weights='distance', n_neighbors=4)
# classifier.fit(xn ,y)
# for crossval in range(len(kfold)):
#     trainindex = kfold[crossval][0].tolist()
#     evaluateindex = kfold[crossval][1].tolist()
#     trainx = xn[trainindex]
#     trainy = y[trainindex]
#     evaluatex = xn[evaluateindex]
#     evaluatey = y[evaluateindex]
#
#     classifier.fit(trainx, trainy)
#     result.append(classifier.predict(evaluatex) == evaluatey)
#
# print float(sum(result))/len(result)
#
#
#-----------------------------------------------------------

# X_train, X_test, y_train, y_test = train_test_split(
#     xn, y, test_size=0.1, random_state=0)
# lim = np.arange(900, 1200, 300/100).tolist()
# gam = np.arange(1, 2, 1.0/100).tolist()
# tuned_parameters = [{'kernel': ['rbf'], 'gamma': gam,
#                      'C': lim}]

#
# clf = GridSearchCV(SVC(C=1), tuned_parameters, cv=5)
# clf.fit(X_train, y_train)
# print(clf.best_params_)
# y_true, y_pred = y_test, clf.predict(X_test)
# print(classification_report(y_true, y_pred))
#

# #{'kernel': 'rbf', 'C': 972, 'gamma': 1.3300000000000003} #0.7625
# classifier = SVC(kernel='rbf', C=972, gamma=1.33)
# classifier.fit(xn,y)
# result = []
# for crossval in range(len(kfold)):
#     trainindex = kfold[crossval][0].tolist()
#     evaluateindex = kfold[crossval][1].tolist()
#     trainx = xn[trainindex]
#     trainy = y[trainindex]
#     evaluatex = xn[evaluateindex]
#     evaluatey = y[evaluateindex]
#     clf.fit(trainx, trainy)
#     result.append(clf.predict(evaluatex) == evaluatey)
# print float(sum(result))/float(len(result))
#
#----------------------------------------------------------------
# X_train, X_test, y_train, y_test = train_test_split(
#     xn, y, test_size=0.1, random_state=0)
# lim = np.arange(1, 37).tolist()
# tuned_parameters = [{'n_estimators': lim}]
# cla = RandomForestClassifier()
# clf = GridSearchCV(cla, tuned_parameters, cv=3)
# clf.fit(X_train, y_train)
# print(clf.best_params_)
#
# result = []
#{'n_estimators': 36} 0.789583333333
# classifier = RandomForestClassifier(n_estimators=36)
# classifier.fit(xn, y)
# for crossval in range(len(kfold)):
#     trainindex = kfold[crossval][0].tolist()
#     evaluateindex = kfold[crossval][1].tolist()
#     trainx = xn[trainindex]
#     trainy = y[trainindex]
#     evaluatex = xn[evaluateindex]
#     evaluatey = y[evaluateindex]
#
#     classifier.fit(trainx, trainy)
#     result.append(classifier.predict(evaluatex) == evaluatey)
#
# print float(sum(result))/len(result)


#print confusion_matrix(classifier.predict(xn), y)



plt.show()