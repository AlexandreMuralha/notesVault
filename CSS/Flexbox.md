# CSS Flexbox

## Container (Parent)

```css
.container {
  display: flex; /* Define o elemento como um flex container e todos os seus filhos diretos em flex itens. */
  display: inline-flex; /* Makes the flex container display inline. */
   
  /*Define a direção dos flex itens. Por padrão ele é row (linha), por isso quando o display: flex; é adicionado, 
  os elementos ficam em linha, um do lado do outro. */
  flex-direction: row;            /* esquerda para a direita - default*/
  flex-direction: row-reverse;    /* direita para a esquerda */
  flex-direction: column;         /* cima para baixo */
  flex-direction: column-reverse; /* baixo para cima */
    
  flex-wrap: nowrap; /* todos os items em uma linha - default */
  flex-wrap: wrap;   /* items em multiplas linhas - top to bottom */
  flex-wrap: wrap-reverse;   /* multi-lines - bottom to top */
  
   
  /* This defines the alignment along the main axis: */ 
  justify-content: flex-start; /* items ficam alinhados da esquerda para a direita */
  justify-content: center; /*items ficam centrados */ 
  justify-content: flex-end; /*items ficam alinhados à direita */
  justify-content: space-between; /* items sao distribuidos igualmente na linha */
  justify-content: space-around;  
  justify-content: space-evenly; /* items are distributed so that the spacing between any two items (and the space to the edges) is equal. */
  
  /*This defines the default behavior for how flex items are laid out along the cross axis on the current line. Think of it as the justify-content version for the cross-axis*/
  align-items: flex-start; /* vertical-align to top */
  align-items: flex-end;   /* vertical-align to bottom */
  align-items: center;     /* vertical-align to center */
  align-items: stretch;    /* same height on all (default) */
  align-items: baseline;
  
  
  align-content: _stretch;_// Valor padrão, ele que faz com que os flex itens cresçam igualmente na vertical.
  align-content: _flex-start;_// Alinha todas as linhas de itens ao início.
  align-content: _flex-end;_// Alinha todas as linhas de itens ao final.
  align-content: _center;_// Alinha todas as linhas de itens ao centro.
  align-content: _space-between;_// Cria um espaçamento igual entre as linhas. Mantendo a primeira grudada no topo e a última no bottom.
  align-content: _space-around;_// Cria um espaçamento entre as linhas. Os espaçamentos do meio são duas vezes maiores que o top e bottom.

```


## flex items - child elements

#### align-self
```css
/* This allows the default alignment (or the one specified by align-items) to be overridden for individual flex items. */

.item {
align-self: auto;
align-self: flex-start;
align-self: flex-end;
align-self: center;
align-self: baseline;
align-self: stretch;
}
```

### flex-grow
```css
/* This allows the default alignment (or the one specified by align-items) to be overridden for individual flex items. */

flex-grow: número;_ // Basta definir um número
flex-grow: 0; // Obedece o width do elemento ou o flex-basis.
```

### Re-ordering Items

```css
/* Permite re-ordenar os items no container, independentemente da ordem destes no código fonte. */

.item1 {	
order: 2;
}

.item2 {
order: 1; /*Item2 aparecerá antes do item1*/
}

/* Ambos aparecerão depois de todos os outros items, já que o valor default é zero */
```

Links:
- https://origamid.com/projetos/flexbox-guia-completo/
- https://css-tricks.com/snippets/css/a-guide-to-flexbox/
- https://css-tricks.com/snippets/css/a-guide-to-flexbox/


----
**tags:** #css