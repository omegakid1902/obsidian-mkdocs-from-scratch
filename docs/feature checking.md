## **Tiêu đề**

```
# this is title
```
result:
# This is title

## **Internal linking**
```
[[index]]
```
result:

[[index]]

## **markdown link**
```
[index](index.md)

[Đây là page 2](Đây là page 2.md): unicode character
```
result:

[index](index.md)

[Đây là page 2](Đây là page 2.md): unicode character

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
![image-1](images/image-1.png)
embed internet image
![Engelbart](https://history-computer.com/ModernComputer/Basis/images/Engelbart.jpg)
```
link

[image-1](images/image-1.png)

embed local

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

```js
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'})
  }
}
```

## Highlighting
Use two equal signs to ==highlight text==.

## Footnotes
Here's a simple footnote,[^1] and here's a longer one.[^bignote]

[^1]: meaningful!

[^bignote]: Here's one with multiple paragraphs and code.
