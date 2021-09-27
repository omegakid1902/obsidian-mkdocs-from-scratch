---
title: Flask lib
UID: 210927231239
created: 27-Sep-2021
tags:
  - '#created/2021/Sep/27'
  - '#seed🥜'
  - '#permanent/concept'
publish: True
aliases:
  - Flask
  - Thư viện Flask
  - Thư viện Flask của python
---
# Flask lib

## Notes:
Flask là một thư viện [[Python]], link website flask [tại đây](https://flask.palletsprojects.com/en/2.0.x/) dùng để xây dựng website html bằng python code.

[Sample](https://flask.palletsprojects.com/en/2.0.x/quickstart/#a-minimal-application):
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

## Ideas & thoughts:
- Công nhân python mạnh thật, dễ dùng mà lại nhiều chức năng

## Questions:

## Relate to:
- [[Python]]