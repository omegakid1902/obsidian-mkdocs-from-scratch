---
title: feature checking
tags:
  - pages
  - notes
---
## **Tiêu đề**

```
# this is title
```
result:
# This is title

## **Internal linking**
```
[[index]]

[[index|alternative name]]

[[Đây là page 2#Header 1]]

[docker](https://squidfunk.github.io/mkdocs-material/getting-started/#with-docker)

```
result:

[[index]]

[[index#Feature checking]]

[[index|alternative name]]

sub/subpage.md
[[subpage]]

[[Đây là page 2]]

[[Đây là page 2#Header 1]]

[docker](https://squidfunk.github.io/mkdocs-material/getting-started/#with-docker)

## **markdown link**
```
[index](index.md)

[Đây là page 2](Đây là page 2.md): unicode character

[Đây là page 2](Đây là page 2.md#Header 1)
```
result:

[index](index.md)

[Đây là page 2](Đây là page 2.md): unicode character

[Đây là page 2](Đây là page 2.md#Header 1)

[subpage](pagesub.md)

## **Code style**
```
code style
`code`
```
result:

`code`

## Images
Must direct to folder
```
link
[image-1](images/image-1.png)
embed local
![image-1](image-1.png)
![image-1](images/image-1.png)
embed internet image
![Engelbart](https://history-computer.com/ModernComputer/Basis/images/Engelbart.jpg)
```
link

[image-1](images/image-1.png)

embed local

![image-1](image-1.png)
![image-1](images/image-1.png)

embed internet image

![Engelbart](https://history-computer.com/ModernComputer/Basis/images/Engelbart.jpg)

## Heading

```
# This is a heading 1
## This is a heading 2
### This is a heading 3 
#### This is a heading 4
##### This is a heading 5
###### This is a heading 6
```
# This is a heading 1
## This is a heading 2
### This is a heading 3 
#### This is a heading 4
##### This is a heading 5
###### This is a heading 6

## Emphasis
```
*This text will be italic*
_This will also be italic_
```

*This text will be italic*

_This will also be italic_

```
**This text will be bold**
__This will also be bold__
```
**This text will be bold**

__This will also be bold__

```
_You **can** combine them_
```
_You **can** combine them_

## Lists
```
- Item 1
- Item 2
  - Item 2a
  - Item 2b

1. Item 1
1. Item 2
1. Item 3
   1. Item 3a
   1. Item 3b
```

- Item 1
- Item 2
	- Item 2a
	- Item 2b

1. Item 1
2. Item 2
3. Item 3
	1. Item 3a
	2. Item 3b
	
## quotes
```
> Human beings face ever more complex and urgent problems, and their effectiveness in dealing with these problems is a matter that is critical to the stability and continued progress of society.
\- Doug Engelbart, 1961
```
>Human beings face ever more complex and urgent problems, and their effectiveness in dealing with these problems is a matter that is critical to the stability and continued progress of society.
\- Doug Engelbart, 1961

## Code block

``` c
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'})
  }
}
```

## Highlighting
Use two equal signs to ==highlight text==.

## Markdown extension
mkdocs.yml
```
markdown_extensions:
  - pymdownx.keys
```
put it in *.md
```
<span class="keys">
  <kbd class="key-ctrl">Ctrl</kbd>
  <span>+</span>
  <kbd class="key-alt">Alt</kbd>
  <span>+</span>
  <kbd class="key-delete">Delete</kbd>
</span>
```
Result:

<span class="keys">
  <kbd class="key-ctrl">Ctrl</kbd>
  <span>+</span>
  <kbd class="key-alt">Alt</kbd>
  <span>+</span>
  <kbd class="key-delete">Delete</kbd>
</span>
or
put it in *.md
```
++ctrl+alt+del++
```
++ctrl+alt+del++
## syntax highlight
```
markdown_extensions:
  - pymdownx.superfences
  - pymdownx.highlight:
```
``` python
import tensorflow as tf
```
```
theme:
  features:
    - content.code.annotate
```

``` js
document$.subscribe(function() { // (1)
  var tables = document.querySelectorAll(/* (2) */ "article table")
  tables.forEach(function(table) {
    new Tablesort(table)
  })
})
```

1. ...
2. ...

### add line num for code block
Chi tiết [tại đây](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/)
```
markdown_extensions:
  - pymdownx.superfences
  - pymdownx.highlight:
      linenums: true
```
- Can set linenumber start by add `linenums="<start-number>"`
``` linenums="3"
markdown_extensions:
  - pymdownx.superfences
  - pymdownx.highlight:
      linenums: true
```

## Highlight code block line
add this to code block `hl_lines="2 3"`
``` hl_lines="2 3"
markdown_extensions:
  - pymdownx.superfences
  - pymdownx.highlight:
      linenums: true
```
## inline syntax highlight
```
markdown_extensions:
  - pymdownx.inlinehilite
```
```
The `#!python range()` function is used to generate a sequence of numbers.
```
The `#!python range()` function is used to generate a sequence of numbers.

## Color
[color](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/#custom-syntax-theme)

## inline tab
```
markdown_extensions:
  - pymdownx.superfences
  - pymdownx.tabbed
```
```
=== "C"
<2 tabs space>
    ```c
    #include <stdio.h>

    int main(void) {
      printf("Hello world!\n");
      return 0;
    }
    ```

=== "C++"

    ```c++
    #include <iostream>

    int main(void) {
      std::cout << "Hello world!" << std::endl;
      return 0;
    }
    ```
```

=== "C"

    ```c
    #include <stdio.h>

    int main(void) {
      printf("Hello world!\n");
      return 0;
    }
    ```

=== "C++"

    ```c++
    #include <iostream>

    int main(void) {
      std::cout << "Hello world!" << std::endl;
      return 0;
    }
    ```
Day laf tab list
=== "Unordered list"

    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

=== "Ordered list"

    1. Sed sagittis eleifend rutrum
    2. Donec vitae suscipit est
    3. Nulla tempor lobortis orci

!!! example

    === "Unordered List"

        _Example_:

        ``` markdown
        * Sed sagittis eleifend rutrum
        * Donec vitae suscipit est
        * Nulla tempor lobortis orci
        ```

        _Result_:

        * Sed sagittis eleifend rutrum
        * Donec vitae suscipit est
        * Nulla tempor lobortis orci

    === "Ordered List"

        _Example_:

        ``` markdown
        1. Sed sagittis eleifend rutrum
        2. Donec vitae suscipit est
        3. Nulla tempor lobortis orci
        ```

        _Result_:

        1. Sed sagittis eleifend rutrum
        2. Donec vitae suscipit est
        3. Nulla tempor lobortis orci
## Admotion
```
markdown_extensions:
  - admonition
```
!!! Day-la-ad

      inside

```
markdown_extensions:
  - pymdownx.details
```
```
!!! note "Phasellus posuere in sem ut cursus"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
```
!!! note "Phasellus posuere in sem ut cursus"
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

```
!!! note ""
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
```
!!! note ""
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
## Collapsible blocks

??? note
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
See more [admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions)

Table

| Method      | Description                          |
| ----------- | ------------------------------------ |
| `GET`       | :material-check:     Fetch resource  |
| `PUT`       | :material-check-all: Update resource |
| `DELETE`    | :material-close:     Delete resource |

```
markdown_extensions:
  - footnotes
```

## [Footnotes](https://squidfunk.github.io/mkdocs-material/reference/footnotes/)

```
Here's a simple footnote,[^1] and here's a longer one.[^bignote]
```

Here's a simple footnote,[^1] and here's a longer one.[^bignote]

[^1]: meaningful!

[^bignote]: Here's one with multiple paragraphs and code.

## Format
### Caret, Mark & Tilde
```
markdown_extensions:
  - pymdownx.caret
  - pymdownx.mark
  - pymdownx.tilde
```
Example:
```
- H~2~0
- A^T^A
```
Result:

- H~2~0
- A^T^A

## Checkbox
```
markdown_extensions:
  - pymdownx.tasklist:
      clickable_checkbox: true
```
```
- [x] Lorem ipsum dolor sit amet, consectetur adipiscing elit
- [ ] Vestibulum convallis sit amet nisi a tincidunt
    * [x] In hac habitasse platea dictumst
    * [x] In scelerisque nibh non dolor mollis congue sed et metus
    * [ ] Praesent sed risus massa
- [ ] Aenean pretium efficitur erat, donec pharetra, ligula non scelerisque
```

- [x] Lorem ipsum dolor sit amet, consectetur adipiscing elit
- [ ] Vestibulum convallis sit amet nisi a tincidunt
    * [x] In hac habitasse platea dictumst
    * [x] In scelerisque nibh non dolor mollis congue sed et metus
    * [ ] Praesent sed risus massa
- [ ] Aenean pretium efficitur erat, donec pharetra, ligula non scelerisque

```
markdown_extensions:
  - abbr
```
The HTML specification is maintained by the W3C.

--8<-- "includes/abbreviations.md"

## matjax
```
  - pymdownx.arithmatex:
      generic: true

extra_javascript:
  - javascripts/config.js
  - https://polyfill.io/v3/polyfill.min.js?features=es6
  - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js
```

javascripts/config.js
```js
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

document$.subscribe(() => {
  MathJax.typesetPromise()
})
```
[matjax](https://squidfunk.github.io/mkdocs-material/reference/mathjax/)

$$
\operatorname{ker} f=\{g\in G:f(g)=e_{H}\}{\mbox{.}}
$$

https://facelessuser.github.io/pymdown-extensions/extensions/magiclink/

https://facelessuser.github.io/pymdown-extensions/extensions/smartsymbols/
```
  - pymdownx.smartsymbols
```
https://squidfunk.github.io/mkdocs-material/setup/setting-up-site-search/
```
theme:
    features:
      - search.suggest          # sugess when use plugin.search
      - search.highlight        # highlight match text in page
      - separator: '[\s\-\.]+']
```
```
Code block việt ngữ 
```
