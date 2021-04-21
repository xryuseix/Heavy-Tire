![Python](https://img.shields.io/github/pipenv/locked/python-version/xryuseix/Heavy-Tire)

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

```sj
https://heavy-tire.herokuapp.com/?url=utchweb.gtphost.com/zimbra/exch/owa/uleth/index.html
```
