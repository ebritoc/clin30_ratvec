# -*- coding: utf-8 -*-

"""Utilities for evaluation of machine learning methodology."""

import random

import numpy as np
from sklearn.model_selection import cross_val_score, KFold
from sklearn.neighbors import KNeighborsClassifier

__all__ = [
    'mean_cross_val_score',
    'score_overview'
]


def mean_cross_val_score(n_components: int, n_neighbors: int, x, y):
    idx = np.arange(len(y))
    random.seed(0)
    random.shuffle(idx)
    clf = KNeighborsClassifier(n_neighbors=n_neighbors)
    cv_scores = cross_val_score(clf, x[idx, :n_components], y[idx], cv=10)
    return cv_scores.mean()


def score_overview(n_components: int, n_neighbors: int, x, y):
    kf = KFold(n_splits=10, shuffle=True, random_state=0)
    clf = KNeighborsClassifier(n_neighbors=n_neighbors)
    mean_scores = []
    pos_scores = []
    neg_scores = []

    for train_index, test_index in kf.split(x):
        X_train, X_test = x[train_index, :n_components], x[test_index, :n_components]
        y_train, y_test = y[train_index], y[test_index]
        clf.fit(X_train, y_train)
        idx_pos = np.where(y_test)
        idx_neg = np.where(y_test==False)
        mean_scores.append(clf.score(X_test,y_test))
        pos_scores.append(clf.score(X_test[idx_pos], y_test[idx_pos]))
        neg_scores.append(clf.score(X_test[idx_neg], y_test[idx_neg]))

    return np.mean(mean_scores), np.mean(pos_scores), np.mean(neg_scores)

