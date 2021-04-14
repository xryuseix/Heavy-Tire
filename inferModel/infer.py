import joblib
import pandas as pd
import processing as proc


def infer(url: str):
    clf = joblib.load("phishing.pkl")  # モデル読みこみ
    tokenizedUrl = proc.tokenize(url)  # トークン化
    normalizedUrl = proc.englishNormalization(tokenizedUrl)  # 正規化
    feature = proc.wordStr2IntVec(pd.Series(normalizedUrl))  # ベクトル化
    print(feature)
    predictResult = clf.predict(feature)
    return predictResult


if __name__ == "__main__":
    print("good:", infer("facebook.com/people/Desiree-Gordon/507399416"))  # good
    print("bad:", infer("dutchweb.gtphost.com/zimbra/exch/owa/uleth/index.html"))  # bad

