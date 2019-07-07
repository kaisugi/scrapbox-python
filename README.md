# scrapbox-python

[![CircleCI](https://circleci.com/gh/7ma7X/scrapbox-python.svg?style=svg)](https://circleci.com/gh/7ma7X/scrapbox-python)
[![PyPI version](https://badge.fury.io/py/scrapbox.svg)](https://badge.fury.io/py/scrapbox)

An unofficial wrapper around the [Scrapbox API](https://scrapbox.io/help-jp/API).

## Installation

```sh
pip install scrapbox
# or `pipenv install scrapbox`
```

## Basic Use

```python
import scrapbox

client = scrapbox.Client()
project = client.get("/pages/help-jp/")
```

## Examples

### Get all the data of a project in JSON format

```python
import json

client = scrapbox.Client()
project = client.get("/pages/help-jp/", limit=10)
# https://scrapbox.io/help-jp/

print(json.dumps(project, ensure_ascii=False, indent=2))
"""
{
  "projectName": "help-jp",
  "skip": 0,
  "limit": 10,
  "count": 73,
  "pages": [
    {
      "id": "57c7d72ad25ef00f00100688",
      "title": "Scrapboxの使い方",
      "image": "https://gyazo.com/7057219f5b20ca8afd122945b72453d3/raw",
      "descriptions": [
        "[https://gyazo.com/7057219f5b20ca8afd122945b72453d3]",
        "Scrapbox（スクラップボックス）の使い方・活用方法についてご紹介します。",
        "[* 編集を始める]",
        "まず最初に[ブラケティング]を読んでみましょう",
        "[* チュートリアルで雰囲気をつかむ]"
      ],
      "user": {
        "id": "566f8b954fb08e1100af5c5b"
      },
      "pin": 9007197717386014,
      "views": 34396,
      "linked": 2,
      "commitId": "5cf9c78742fc7800179f8c19",
      "created": 1472713402,
      "updated": 1559271981,
      "accessed": 1562487581,
      "snapshotCreated": 1559315996
    },
...
"""
```

### Get page data in JSON format

```python
import json

client = scrapbox.Client()
page = client.get("/pages/help-jp/API")
# https://scrapbox.io/help-jp/API

print(json.dumps(page, ensure_ascii=False, indent=2))
"""
{
  "id": "58e67688d0a4fe0011a0249c",
  "title": "API",
  "image": "https://gyazo.com/5bf55bb6223a62bf4477f07a9aad39b8/raw",
  "descriptions": [
    "[https://gyazo.com/5bf55bb6223a62bf4477f07a9aad39b8]",
    "あくまで内部APIです。APIは予告なく変更を行います。",
    "ページデータを取得するAPI",
    "ページリスト",
    "`/api/pages/:projectName`"
  ],
  "user": {
    "id": "5724627723541f110097c291",
    "name": "shokai",
    "displayName": "Sho Hashimoto",
    "photo": "https://lh3.googleusercontent.com/-auiW-ZOVu6Y/AAAAAAAAAAI/AAAAAAAADLg/YwBeR9cziLU/photo.jpg"
  },
  "pin": 0,
  "views": 7072,
  "linked": 1,
  "commitId": "5d135304ff5b5d0017cd83cc",
  "created": 1491498636,
  "updated": 1561547524,
  "accessed": 1562490240,
  "snapshotCreated": 1561586966,
  "persistent": true,
  "lines": [
    {
      "id": "58e67688d0a4fe0011a0249c",
      "text": "API",
      "userId": "5724627723541f110097c291",
      "created": 1491498636,
      "updated": 1491499158
    },
...
"""
```

### Get the body text of a page

```python
client = scrapbox.Client()
text = client.get("/pages/help-jp/Scrapboxの使い方/text")

print(text)
"""
Scrapboxの使い方
[https://gyazo.com/7057219f5b20ca8afd122945b72453d3]
Scrapbox（スクラップボックス）の使い方・活用方法についてご紹介します。

[* 編集を始める]
	まず最初に[ブラケティング]を読んでみましょう

[* チュートリアルで雰囲気をつかむ]
 サンプルプロジェクト
 	Scrapboxを開発するNotaが実際に利用したページを一部そのまま公開します。
  　[Nota社のScrapboxを一部公開 https://scrapbox.io/nota-private-sample/]
	[Scrapboxチュートリアルスライド]
		使い方の概要を掴むことができます
　実践テクニック
 　[エンジニアの生産性をあげるScrapboxの使い方 https://scrapbox.io/business/tutorial]
...
"""
```

### Get the title image of a page

```python
client = scrapbox.Client()

raw_image = client.get("/pages/help-jp/Scrapboxの使い方/icon")
with open("title.jpg", "wb") as f:
    f.write(raw_image)
# Download the top icon as "title.jpg"
```