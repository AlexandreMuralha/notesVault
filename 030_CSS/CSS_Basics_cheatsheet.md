### Selectors

```css
.class {font-weight: bold;}
```

### Básicos

```css
* { }              /* Todos os Elementos */
div { }            /* Elementos */
.class { }         /* Classe */
#id { }            /* ID */
```

### Combinadores

```css
.parent .child { } / ul li { }   /* Descendant */
.parent > .child { }             /* Descendante Direto */
.child + .child { }              /* Elemento irmão adjacente */
.class1.class2 { }               /* tem as duas classes */
.child ~ .sibling { }
```

### Por Atributo

```css
[atribute]         /* Atributo */
-----
-----
-----
```

### Pseudo-classes

```css
seletor:pseudo-classe {propriedade: valor;} 
```

```css
:target {} /* */
:disabled {} /* */
:focus { }
:active { }

:nth-child(3)
:nth-child(3n+2)

:nth-last-child(2)
:nth-of-type(3)

:empty /* Elementos sem filhos */
```

### Propriedades

```css
{font-family: Arial, Helvetica, sans-serif;}
{font-size: 15px|medium|150% }            /* Tamanho da fonte */
{letter-spacing: 2px|-1px|normal|initial|inherit}
{line-height: normal|80%|1.6|initial|inherit}

{font-weight:100|200|300|400|500|600|700|800|900;} /* 400 = normal 700 = bold */
{font-weight:normal|bold|bolder|lighter|initial|inherit;}


{text-align: left | right | center | justify }
{text-transform: capitalize | uppercase | lowercase }
```

```css
{background-color: coral | #ffffd1 | rgb(201, 76, 76) | rgba(201, 76, 76, .5)}
{background-image: url("file.jpg") }
{background-position: ;}
{background-size: ;}
{background-clip: ;}
{background-repeat: repeat|no-repeat|repeat-x /*horizontally*/|repeat-y/*vertically*/ }
{background-attachment: ;}
```

------
