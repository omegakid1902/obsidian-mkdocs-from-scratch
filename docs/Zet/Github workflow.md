---
title: Github workflow
UID: 211001203814
created: 01-Oct-2021
tags:
  - '#created/2021/Oct/01'
  - 'garden🏡'
  - 'permanent/howto'
aliases:
  - Github action
publish: True
---
# Github workflow

## Notes:
### Common templates
#### Fetch code
Fetch all history
```yml
- uses: actions/checkout@v2
  with:
    fetch-depth: 0
```
#### Push code
Commit and push use TOKEN setup by `checkout` plugin
```yml
      - uses: actions/checkout@v2
      - run: |
          date > generated.txt
          git config user.name github-actions
          git config user.email github-actions@github.com
          git add .
          git commit -m "generated"
          git push
```
otherwise, we need to setup Secret token by:
```yml
      - name: Publish gh-pages-obsidian-mkdocs
        uses: ad-m/github-push-action@master
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          branch: 'gh-pages-obsidian-mkdocs'
```

Note: we can configure author of that commit by set user/email
```
git config --local user.email "41898282+github-actions[bot]@users.noreply.github.com"
git config --local user.name "github-actions[bot]"
```

#### Dispatch multiple repos/workflows
Send dispatch to other repos/workflows by option `repo`, `owner`

```yml
name: Alert Some Repos to build

on:
  push:
    branches:
      - main

jobs:
  build:
    name: Dispatch to other repo
    runs-on: ubuntu-latest
    steps:
      - name: Alert repository_dispatch to gatsby-garden repo
        uses: mvasigh/dispatch-action@main
        with:
          token: ${{ secrets.ZET_ACCESS_TOKEN }}
          repo: gatsby-garden
          owner: omegakid1902
          event_type: update_zettelkasten_none
```
-> send dispatch `update_zettelkasten_none` to `omegakid1902/gatsby-garden`
 
 On `omegakid1902/gatsby-garden` repo, add workflow:
```yml
name: Gatsby garden get

on:
  repository_dispatch:
    types: [update_zettelkasten]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Catch it
	    run: echo "I catched update_zettelkasten signal"
 ```
 #### Setup environment
 Install python
 ```yml
       - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.7.7
          architecture: x64
 ```