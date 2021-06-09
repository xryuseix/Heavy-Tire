import pandas as pd
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

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


# ロジスティック回帰
def logisticRegression(trainX, testX, trainY, testY):
    lr = LogisticRegression(max_iter=300)
    lr.fit(trainX, trainY)
    return lr

# CNN
def linearSVC(trainX, testX, trainY, testY):
    svc = LinearSVC(max_iter=3000)
    svc.fit(trainX, trainY)
    return svc

