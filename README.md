# obsidian-mkdocs-from-scratch

```requirement.in
git+https://github.com/jldiaz/mkdocs-plugin-tags.git
```

```mkdocs.yml
plugins:
  - tags:
      tags_folder: /tags
#      tags_template: docs/theme/tags.md.template
```

### Footer
Xem chi tiết tại [link](https://squidfunk.github.io/mkdocs-material/setup/setting-up-the-footer/)

select more icon on material repo
[icon](https://github.com/squidfunk/mkdocs-material/tree/master/material/.icons)
```
extra:
  social:                             # config footer
    - icon: fontawesome/brands/github # select icon in https://github.com/squidfunk/mkdocs-material/tree/master/material/.icons
      link: https://github.com/omegakid1902
      name: Dung Tran on Twitter
  generator: false # Autogenerate copyright 
```
