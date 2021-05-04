![Python](https://img.shields.io/github/pipenv/locked/python-version/xryuseix/Heavy-Tire) ![Python](https://img.shields.io/badge/Python-v3.9.1-yellow?logo=python) [![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)

# 「Heavy-Tire」 - フィッシングサイト検知システム

## フィッシング検知 API

フィッシングサイトかどうか判定します．

### クエリパラメータ

- url

### 結果

json で返ります．値が 0 の場合は正常サイト，値が 1 の場合はフィッシングサイトです．

```js
{"result":1}
```

### Example

Good

```sh
https://heavy-tire.herokuapp.com/?url=twitter.com
```

Bad

```sh
https://heavy-tire.herokuapp.com/?url=utchweb.gtphost.com/zimbra/exch/owa/uleth/index.html
```

## 環境について

![Python](https://img.shields.io/github/pipenv/locked/python-version/xryuseix/Heavy-Tire)
[Pipfile](./Pipfile) + [requirements.txt](WebAPI-Python/requirements.txt) の環境設定ファイルは x86_64(intel) 環境の場合に用います．

![Python](https://img.shields.io/badge/Python-v3.9.1-yellow?logo=python)
[requirements.yaml](WebAPI-Python/requirements.yaml) の環境設定ファイルは aarch64(ARM) 環境の場合に用います．
こちらの環境の場合，sklearn や pandas などを使用するために conda, conda-forge 環境を用意する必要があります．
