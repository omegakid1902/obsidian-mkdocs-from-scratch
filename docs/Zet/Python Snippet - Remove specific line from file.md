---
title: Python Snippet - Remove specific line from file
UID: 220503120252
created: 03-May-2022
tags:
  - 'created/2022/May/03'
  - 'evergreen'
  - 'permanent/concept'
aliases: 220503120252
publish: True
---
## Notes:

```python
import os

base_docs_url = "./_notes/"

for root, dirs, files in os.walk(base_docs_url):
    for file_name in files:
        abs_link_url = os.path.join(root, file_name)
        if abs_link_url.endswith('.md'):
            with open(abs_link_url, 'r+', encoding='utf_8') as fi:
                content = fi.readlines()
                fi.seek(0)
                for line in content:
                    if not line.startswith("# "):
                        fi.write(line)
                fi.truncate()
```


## Created:
- [[2022-05-03]]
