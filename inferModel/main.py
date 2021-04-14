import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
import processing as proc
import learningModel as model

# ファイル読み込み
print("1. reading file...")
df = pd.read_csv("../Phishing/phishing_site_urls.csv")

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
"""
tfidfFeature = proc.wordStr2TfidfVec(df.text_sent)
trainX_tf, testX_tf, trainY_tf, testY_tf = train_test_split(tfidfFeature, df.Label)
"""

print("5. learning...")

# ロジスティック回帰で学習
## CountVectorizerで学習
lr_i32 = model.logisticRegression(trainX_i32, testX_i32, trainY_i32, testY_i32)
model.evaluation(
    lr_i32, trainX_i32, testX_i32, trainY_i32, testY_i32, "LogisticRegression-count"
)

## TfidfVectorizerで学習(微妙に低い?)
"""
lr_tf = model.logisticRegression(trainX_tf, testX_tf, trainY_tf, testY_tf)
model.evaluation(lr_tf, trainX_tf, testX_tf, trainY_tf, testY_tf, "LogisticRegression-tfidf")
"""

joblib.dump(lr_i32, "phishing.pkl", compress=True)

