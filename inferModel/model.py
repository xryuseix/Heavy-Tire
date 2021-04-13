import pandas as pd
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression

# ロジスティック回帰
def logisticRegression(trainX, testX, trainY, testY):
    lr = LogisticRegression(max_iter=300)
    lr.fit(trainX, trainY)
    return lr
"""
Training Accuracy : 0.970163273132383
Testing Accuracy : 0.9594209863328892

CLASSIFICATION REPORT

              precision    recall  f1-score   support

         Bad       0.97      0.89      0.93     38937
        Good       0.96      0.99      0.97     98400

    accuracy                           0.96    137337
   macro avg       0.96      0.94      0.95    137337
weighted avg       0.96      0.96      0.96    137337
"""

# 学習結果を評価
def evaluation(model, trainX, testX, trainY, testY, name=""):
    print("Training Accuracy :", model.score(trainX, trainY))
    print("Testing Accuracy :", model.score(testX, testY))
    print("\nCLASSIFICATION REPORT\n")
    print(
        classification_report(testY, model.predict(testX), target_names=["Bad", "Good"])
    )
