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
def wordStr2IntVec(url: str):
    cv = CountVectorizer()
    return cv.fit_transform(url)

# 英単語の文字列をtfidfのベクトルに変換
def wordStr2IntVec(url: str):
    tv = TfidfVectorizer()
    return tv.fit_transform(url)