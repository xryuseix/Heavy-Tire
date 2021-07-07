import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.svm import LinearSVC, SVC

# 学習結果を評価
def evaluation(model, trainX, testX, trainY, testY, name=""):
    print("\n=== CLASSIFICATION REPORT ===")
    print("model :", name)
    print("Training Accuracy :", model.score(trainX, trainY))
    print("Testing Accuracy :", model.score(testX, testY))
    print(
        "\n",
        classification_report(
            testY, model.predict(testX), target_names=["Bad", "Good"]
        ),
    )
    plot_confusion_matrix(model, testX, testY, cmap="YlOrRd")
    # plot_confusion_matrix(model, testX, testY)
    plt.savefig("result.png")


# ロジスティック回帰
def logisticRegression(trainX, trainY):
    lr = LogisticRegression(max_iter=300)
    lr.fit(trainX, trainY)
    return lr


# CNN
def linearSVC(trainX, trainY):
    svc = LinearSVC(max_iter=3000)
    svc.fit(trainX, trainY)
    return svc


# グリッドサーチ
def gridSearch(trainX, trainY, model_name, param):
    gscv = GridSearchCV(model_name, param, cv=4, verbose=3)
    gscv.fit(trainX, trainY)
    return gscv


# グリッドサーチ
def svc(trainX, trainY):
    svc = SVC(verbose=1)
    svc.fit(trainX, trainY)
    return svc
