import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
import processing as proc
import learningModel as model
from sklearn.svm import LinearSVC, SVC
from sklearn.naive_bayes import GaussianNB

# ファイル読み込み
print("1. reading file...")
df = pd.read_csv("PhishingDataset/phishing_site_urls.csv")

# 重複削除
df = df.drop_duplicates()

"""print(df.describe())
                        URL   Label
count                507196  507196
unique               507195       2
top     tommyhumphreys.com/    good
freq                      2  392897
"""

# URLを英単語列でトークン化
print("2. word tokenized...")
df["text_tokenized"] = df.URL.map(lambda url: proc.tokenize(url))

# 英単語を正規化
print("3. word normalization...")
df["text_sent"] = df["text_tokenized"].map(
    lambda urlList: proc.englishNormalization(urlList)
)

print("4. vectirization...")

# 英単語の文字列をintのベクトルに変換
intFeature = proc.wordStr2IntVec(df.text_sent)
trainX_i32, testX_i32, trainY_i32, testY_i32 = train_test_split(intFeature, df.Label)

# 英単語の文字列をtfidfのベクトルに変換
tfidfFeature = proc.wordStr2TfidfVec(df.text_sent)
trainX_tf, testX_tf, trainY_tf, testY_tf = train_test_split(tfidfFeature, df.Label)


print("5. learning...")

model_type = 1

if model_type == 0:
    # ロジスティック回帰で学習
    ## CountVectorizerで学習
    lr_i32 = model.logisticRegression(trainX_i32, trainY_i32)
    model.evaluation(
        lr_i32, trainX_i32, testX_i32, trainY_i32, testY_i32, "LogisticRegression-count"
    )
    joblib.dump(lr_i32, "InferData/phishing.pkl", compress=True)

elif model_type == 1:
    # SVCで学習
    ## TfidfVectorizerで学習
    svc = model.linearSVC(trainX_tf, trainY_tf)
    model.evaluation(svc, trainX_tf, testX_tf, trainY_tf, testY_tf, "LinearSVC-tfidf")
    joblib.dump(svc, "InferData/phishing.pkl", compress=True)

elif model_type == 2:
    # SVC
    def param():
    clf = model.svc(trainX_tf, trainY_tf)
    model.evaluation(clf, trainX_tf, testX_tf, trainY_tf, testY_tf, "gridSearch")
    joblib.dump(clf, "InferData/phishing.pkl", compress=True)
