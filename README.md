![Python](https://img.shields.io/github/pipenv/locked/python-version/xryuseix/Heavy-Tire) [![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)

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
