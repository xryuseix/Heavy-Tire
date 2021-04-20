import joblib, json
import pandas as pd
import processing as proc

# 英単語辞書管理クラス
class wordStr2IntVec:
    def __init__(self):
        with open("../InferData/vocabulary.json") as f:
            self.vocabulary = json.load(f)

    # 英単語を数字に変換
    def convert(self, normalizedUrl: str):
        urlList = normalizedUrl.split(" ")
        convertedList = [0] * len(self.vocabulary)
        for word in urlList:
            if word in self.vocabulary:
                convertedList[self.vocabulary[word]] += 1
        return convertedList


def infer(url: str, w2iClass):
    clf = joblib.load("../InferData/phishing.pkl")  # モデル読みこみ
    tokenizedUrl = proc.tokenize(url)  # トークン化
    normalizedUrl = proc.englishNormalization(tokenizedUrl)  # 正規化
    feature = w2iClass.convert(normalizedUrl)
    predictResult = clf.predict([feature])
    return predictResult


if __name__ == "__main__":
    w2i = wordStr2IntVec()
    print("good:", infer("facebook.com/people/Desiree-Gordon/507399416", w2i))  # good
    print(
        "bad:", infer("dutchweb.gtphost.com/zimbra/exch/owa/uleth/index.html", w2i)
    )  # bad
    print(
        "bad:",
        infer(
            "9d345009-a-62cb3a1a-s-sites.googlegroups.com/site/stickamcomlogindo/login.html?amp\%3Battredirects=1&amp;attachauth=ANoY7cp-XSsmMBKPpKQvZiVxuuXfsdv2WcmvUeBVlqd-wj6bdc3iHYq5i11PmWp4Xsjb6atTOxDkMSfoyV6ZHbfGCxfhmMQurfGmfbNSUEYWheq-BZhSyaCCAR8LDOpliWjNIkanhEPTtt6U8zbycYD6u8lVo8vEsK0NszMk_hXJe2ivppyywrORJo9Nsu5LTZZpnxMsrh3rvEiD-gffbsd01hn88jj5hg\%3D\%3D&amp;attredirects=0",
            w2i,
        ),
    )
    print(
        "good:",
        infer(
            "guitarcenter.com/Basslines-ASB-BO-4s-Blackouts-for-Bass---Neck-and-Bridge-Set-105486211-i1474993.gc",
            w2i,
        ),
    )

