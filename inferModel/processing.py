import json
import numpy as np
from nltk.tokenize import RegexpTokenizer 
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# --------- ここは共通で使う ---------#

# URLを英単語列でトークン化
def tokenize(url:str) :
    tokenizer = RegexpTokenizer(r'[A-Za-z]+')
    return tokenizer.tokenize(url)

# 英単語を正規化
def englishNormalization(urlList: list):
    stemmer = SnowballStemmer("english") # choose a language
    return ' '.join([stemmer.stem(word) for word in urlList])


# --------- ここからはモデル次第で使う ---------#

# 英単語の文字列をintのベクトルに変換
vocabulary = {}
def wordStr2IntVec(urlDf):
    cv = CountVectorizer()
    count = cv.fit_transform(urlDf)
    vocabularySave(cv.vocabulary_)
    return count

# 英単語の辞書をファイル書き込み
def vocabularySave(vocabulary):
    class MyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, np.integer):
                return int(obj)
            elif isinstance(obj, np.floating):
                return float(obj)
            elif isinstance(obj, np.ndarray):
                return obj.tolist()
            else:
                return super(MyEncoder, self).default(obj)
    with open('InferData/vocabulary.json', 'w') as f:
        json.dump(vocabulary, f, indent=4, cls = MyEncoder)

# 英単語の文字列をtfidfのベクトルに変換
def wordStr2TfidfVec(url: str):
    tv = TfidfVectorizer()
    return tv.fit_transform(url)