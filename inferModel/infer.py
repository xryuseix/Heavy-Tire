import joblib, json
import pandas as pd
import processing as proc

# 英単語辞書管理クラス
class wordStr2IntVec:
    def __init__(self):
        with open("vocabulary.json") as f:
            self.vocabulary = json.load(f)

    # 英単語を数字に変換
    def convert(self, normalizedUrl: str):
        urlList = normalizedUrl.split(" ")
        convertedList = [self.vocabulary[word] for word in urlList]
        return convertedList


def infer(url: str, w2iClass):
    clf = joblib.load("phishing.pkl")  # モデル読みこみ
    tokenizedUrl = proc.tokenize(url)  # トークン化
    normalizedUrl = proc.englishNormalization(tokenizedUrl)  # 正規化
    print(w2iClass.convert(normalizedUrl))
    return
    feature = proc.wordStr2IntVec(pd.Series(normalizedUrl))  # ベクトル化
    predictResult = clf.predict(feature)
    return predictResult


if __name__ == "__main__":
    w2i = wordStr2IntVec()
    print("good:", infer("facebook.com/people/Desiree-Gordon/507399416", w2i))  # good
    exit()
    print(
        "bad:", infer("dutchweb.gtphost.com/zimbra/exch/owa/uleth/index.html", w2i)
    )  # bad

