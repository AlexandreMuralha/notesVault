# Javascript
- [Estrutura Léxica Básica](#Estrutura-Léxica-Básica)
- [Comentários](#Comentários)
- [Variáveis](#Variáveis)
- [Diferença entre var e let](#Diferença-entre-var-e-let)
- [Tipos de dados](#Tipos-de-dados)
- [Constantes](#Constantes)
- [Operadores Aritméticos](#Operadores-Aritméticos)
- [Operadores Comparativos](#Operadores-Comparativos)
- [Arrays](#Arrays)
- [Métodos](#Métodos)
- [Conversão de Tipos de Dados](#Conversão-de-Tipos-de-Dados)
- [Conditionals](#Conditionals)
- [Truthy Falsy](#Truthy-Falsy)
- [Operadores_Lógicos](#Operadores_Lógicos)
- [Loops](#Loops)
- [Funções](#Funções)
- [Manipulando o DOM](#Manipulando-o-DOM)
- [Objetos](#Objetos)
- [DOM Events](#DOM-Events)
- [Arrow_Functions](#Arrow-Functions)
- [Destructuring](#Destructuring)
- [ES7](#ES7)
- [ES8](#ES8)
---

## Estrutura Léxica Básica

   **Case Sensitive** - Javascript diferencia letras maiúsculas de minúsculas.

  ** Identificadores** (usados para nomear as variáveis ou as funções) podem conter:
   - _ ou $
   - letras de A a Z (maiusculas ou minusculas)
   - Digitos de 0 a 9
   - Caracteres Unicode (não aconselhável, considerado má prática)

   O javascript possui algumas palavras reservadas. Não podem ser usadas como identificadores, porque já possuem uma função especifica no core da linguagem.

   Lista de palavras reservadas [aqui.](https://www.w3schools.com/js/js_reserved.asp)

---
## Comentários
```jsx
    // Este é um comentário de uma linha
    /* Este é um comentário de várias linhas
    Outra linha...
    Outra linha.... */
```

---

## Variáveis

   Uma **variável** é um objeto (uma posição, frequentemente localizada na [memória](https://pt.wikipedia.org/wiki/Mem%C3%B3ria_%28computador%29)) capaz de reter e representar um valor ou expressão.

   Regras para nomear variáveis:
   - Nomes de variáveis devem começar por letras ou underscore ou cifrão, não podem contudo começar por números.
   - Os nomes atribuídos às variáveis são case-sensitive.

   Boas práticas:

   - É considerado boa prática que o nome da variável dê uma ideia o mais precisa possível do que ela representa, facilitando posteriormente a leitura do código.
   - Apesar de não obrigatório é recomendado o uso da notação “CamelCase” quando o nome da variável tiver mais de uma palavra.
   - Existem também um conjunto de palavras que não podem ser usadas para nomear variáveis. Pois já fazem parte do core da linguagem.
   São exemplos: alert, array, goto, function, etc.


   ### Diferença entre var e let

   - Variáveis definidas com a palavra **var** podem ter escopo de global ou de função.
   - Variáveis definidas com a palavra **let** podem ter escopo global, de função e de bloco.

---

## Constantes

Como se fosse uma variável mas o seu valor é permanente.

   As vantagens de usar uma constante prende sobretudo com a questão da segurança e performance. Uma outra vantagem da constante relativamente à variável é que seja o valor desta necessite ser alterado no código, ela apenas precisa ser alterada uma vez.

   É considerado uma boa prática nomear as constantes com letras maiúsculas para ser mais facilmente diferenciadas das variáveis.

   Sintaxe:

  ```jsx
    const nome = x
  ```

---

## Tipos de dados
   1. **Tipos de dados**

   Apesar do Javascript ser uma linguagem **não tipada**, os seus valores tem tipos. Eles podem ser:

   - [Number](Javascript.md###Number) (inteiro ou de ponto flutuante)
   - [String](Javascript.md###String) (texto)
   - Booleano (verdadeiro ou falso)
   - Undefined
   - Null
   - Object

   como descobrir o tipo de uma variável:

   Operador **typeof**

   Ex:

```jsx
    var a = 10, b = "Pedra", c = 45, d = true, e = 0;
    document.write("a é " + typeof a + "<br>")
    document.write("b é " + typeof b + "<br>")
    document.write("c é " + typeof c + "<br>")
    document.write("d é " + typeof d + "<br>")
```

### Number

   Atribuir um número a uma variável:

```jsx
    const peso1 = 1.0
    const peso2 = Numbem('2.0') // Forma Alternativa
```

  Verificando se é um número inteiro:

```jsx
    const a = 3.5
    Number.isInteger(a)

   false //valor retornado
```

 Modificando a quantidade de casas décimais de um número não inteiro:

```jsx
    const b = 8.43421341
    b.toFixed(2)

    '8.43'//valor retornado
```

 **Objeto Math**

   Ex:
   Obtendo um número aleatório entre 0 e 100:
   O método **Math.random()** retorna um número aleatório entre 0 e 1.
   O método **Math.trunc()** descarta as casas decimais.

   Assim:

```jsx
    let result = Math.random() * 100;
    result = Math.trunc(result);

    console.log(result);
```

### String

Retornando uma letra especifica de uma string:

```jsx
    const nome = "maria"
    undefined //valor retornado

    nome.charAt(3)"i" 
    //valor retornado

    nome.charAt(5)'' 
    //valor retornado
```

 Obtendo o digito associado a uma determinada posiçao na string:

```jsx
    ----
```

 Retornando o valor da tabela ASCII correspondente à letra de uma string:

```jsx
    const nome = 'maria'
    undefined //valor retornado

    nome.charCodeAt(2)114 
    //valor retornado
```

**Template Strings (ES6)**

```jsx
    const nome = 'Rebeca'
    const concatenacao = 'Olá ' + nome + '!'
    const template = `
        Olá    
    		${nome}!`

    console.log(concatenacao, template)

    // Nas template strings usa-se backtip (acento grave)*
    Olá Rebeca!   
    		Olá    
    		Rebeca!
```

### Null e Undefined

O valor **null** indica que um objeto tem um valor nulo. Como se este não tivesse sido inicializado.

O valor **undefined** indica que a variável em questão não foi definida ou alguém a declarou undefined (para que fique sem valor definido).

Na prática, utiliza-se o valor undefined quando uma variável não possui um valor definido. Por sua vez o null é utilizado quando intencionalmente queremos dizer que há uma ausência efetiva de valor para a variável em questão.

Quando uma variável é inicializada mas não lhe é atribuido um valor, esta por defeito será undefined.

> Geralmente os desenvolvedores não atribuem o valor undefined a uma variável, já que o próprio javascript o faz. Caso queiramos eliminar o valor em uma variável, geralmente é aconselhado definirmos o seu valor para null. 
> Esta prática é apenas uma convenção que permite a um desenvolvedor rapidamente entender a origem, se intencional (null) ou por defeito (undefined), da ausência de valor naquela variável.

---

## Operadores Aritméticos
- Soma (+)
- Subtração (-)
- Multiplicação (*)
- Divisão (/)
- Módulo (%)

Operador módulo retorna o resto da divisão entre dois valores:

Ex:
```jsx
    5 / 5 = 2.5
    5 % 2 = 1
    4 % 2 = 0
```

Ex:

imprimindo todos os numeros pares entre 0 e 20. (divisiveis por 2, dando resto 0):

```jsx
    //numero é par quando dividido por 2 tem resto 0.
    num = 0
    while(num <= 20) {  
    	num % 2 === 0 ? console.log(num) : " ";  
    	num++;
    }
```

**++** Pré ou pós incremento
```

```
 **--** Pré ou pós decremento
 
 ---

## Operadores_Comparativos

Operadores Comparativos servem para testar e comparar valores.

### == Igual

Serve para testar se um valor é igual a outro, retornando True ou False.

```jsx
    1 == 1
    true

    1 == 3
    false
```

### != Não igual (diferente)

Serve para testar se um valor é diferente de outro, retornando True ou False.

```jsx
    1 != 2
    true

    2 != 2
    false
```

### === Estritamente igual

### !== Estritamente não igual

Além de testarem a igualdade da valores, testam tambem o tipo de dado dos valores

```jsx
    1 === "1"
    false

    "coisa" !== "coisa"
    false

    var nome = "maria"
    nome === "maria"
    true
```

### > Maior que

### >= Maior ou igual que

### < Menor que

### <= Menor ou igual que

Servem para testar se um valor é maior ou menor do que outro.

```jsx
    1 > 20
    false

    355 < 500
    true

    x = 10
    y = 20
    x >= y
    false
```

---

## Arrays

Arrays são usadas para armazenar vários valores em uma única variável.

Ex:

```jsx
    var animais = ["tigre", "girafa" , "macaco", "cavalo"]
```

chamando um dado da array no console:

```jsx

    console.log(animais[1]);
```

no caso o dado chamado foi girafa (o primeiro dado corresponde a 0)

---

**Método shift** - Remove o primeiro item do array

```jsx
    animais.shift();

    // resultado do array animais fica:
    ["girafa" , "macaco", "cavalo"]
```

**Método pop** - Remove o ultimo item do array

```jsx
    animais.pop();
    // resultado no nosso array passa a ser:
    ["tigre", "girafa" , "macaco"]
```

Método **push** - Adiciona um item ao array

```jsx
    animais.push("porco");
    // resultado no nosso array passa a ser:
    var animais = ["tigre", "girafa" , "macaco", "cavalo","porco"]
```

Método **concat** - Adiciona outro array ao existente

```jsx
    animais.concat(["ovelha", "papagaio"])
    // resultado no nosso array passa a ser:
    ["tigre", "girafa" , "macaco", "cavalo", "ovelha", "papagaio"]
```

Método **.length** retorna a quantidade de elementos que o array possuí.

```jsx
    var animais = ["tigre", "girafa" , "macaco", "cavalo"]

    console.log(animais.length)
    4 //retorno
```

Método **splice** -

```jsx
    ------
```

**delete** apaga o valor de uma determinada posição no array:

```jsx
    var animais = ["tigre", "girafa" , "macaco", "cavalo"]
    delete animais[2]
    [ 'tigre', 'girafa', '<1 empty item>', 'cavalo'] // resultado
```

Lista de métodos Array:

[https://www.w3schools.com/jsref/jsref_obj_array.asp

---

## Métodos

### document.write
Permite escrever texto e HTML em um documento.

```jsx
    document.write("argumentos")
```


### alert
Exibe uma caixa de diálogo com a mensagem.

```jsx
    alert("mensagem")
```


### prompt
Exibe uma caixa de dialogo para inserção de dados.

```jsx
    prompt("mensagem","[dica]")
```

A mensagem fica entre aspas, uma sugestão padrão de resposta pode ser indicada para o usuário, ele fica entre parentes retos e é opcional.

O usuário pode confirmar os dados inseridos clicando Ok, ou cancelar.

Os dados retornados podem ser usados em uma variável. Caso o usuário aperte o botão cancelar o valor retornado será Null.


### confirm
 Exibe uma caixa de dialogo com opção para o usuário confirmar ou cancelar uma opção.

```jsx
    confirm("mensagem")
```

Os dados retornados são do tipo booleano, sendo True caso o usuário selecione Ok, e false, caso clique em Cancelar.

[https://www.youtube.com/watch?v=-ip-UXa3Aj8&index=3&list=PLucm8g_ezqNrXkDWHtgvtU9RGuauEs_xz](https://www.youtube.com/watch?v=-ip-UXa3Aj8&index=3&list=PLucm8g_ezqNrXkDWHtgvtU9RGuauEs_xz)

---

## Conversão de Tipos de Dados

A conversão do tipo de dados é necessária quando o javascript interpreta incorretamente um dado inserido.

O operador **typeof()** permite identificar qual o tipo do dado em questão.


### para String
**String()** converte um valor numérico ou boolean em string.

```jsx
    n = 20
    n = String(n)

    a = true
    a = String(a)
```

alternativamente podemos usar **.toString**:

```jsx
    n = n.toString()
```
 
Para converter um número em bínario usamos **.toString(2)**
Ex:

```jsx
let a = 22
a.toString(2)
'10110' // retorno
```


### para Number
Number() converter um valor em texto (string) em um valor numérico.

```jsx
    a = "20"
    n = "67.4"

    a = Number(a)
    b = Number(b)
```


### para nº Inteiro
**parseInt()** converte uma string em um número inteiro, descartando as casas decimais.

```jsx
    b = "23.48"
    b = parseInt(b)

    Valor de b passa a ser 23
```


### para número de ponto flutuante
**parseFloat** converte uma string em um número de ponto flutuante.

```jsx
    b = "13.46"
    b = parseFloat(b)
```

Para definir o numero de casas decimais exibidas usamos o método:
**.toFixed()**

O numero dentro do parenteses indica o numero de casas decimais a exibir.

```jsx
    document.write (a.toFixed(3))
```


Para definir o tamanho total do numero a ser exibido usamos o método 

**.toPrecision()**

O número entre parêntesis indica a quantidade total de algarismos que pretendemos exibir.

```jsx
    document.write (a.toPrecision(5))
```

Converter uma string separada por virgulas para uma Array:

usamos o metodo split e especificamos a virgula:

```jsx
    var a = ('ana,maria,pedro')

    a.split(',')
    [ 'ana', 'maria', 'pedro' ]
```

---


## Conditionals

O flow do javascript é executado linha por linha, de cima para baixo.

Contudo podemos condicionar… para tal usamos…

 - if
 - else
 - else if
 - ternary operator
 - switch

 ### If

 Variável x é igual a 3, variável y = 7

 **Se** o x for igual a 3, então o y será 5

```jsx
    var x = 3
    undefined // retorno do terminal
    var y = 7
    undefined // retorno do terminal

    if (x === 3){y = 5}

    y
    5 // retorno do terminal
```


### else

Variável x é 1, Variável y é 1

**Se** o x for igual a 2, então o y vai ser igual a 2, SENÃO, y será igual a 20.

```jsx
    x = 1
    y = 1

    if (x === 2) {y = 2;} 
    else {y = 20;}

    y
    20 // retorno do terminal
```

### else if

x = 1 e y = 10

Se** x for igual a 2, y será 2, **ou se** y for igual 3, x será 3, **ou se,** x for igual a y, x será 10 e y será 100, **SENÃO**, x será 0 e y será 0

```jsx
    x = 1
    y = 10

    if (x === 2){ y = 2;} 
    else if (y === 3){x = 3;}
    else if (x === y){x = 10; y = 100}
    else {x = 0; y = 0;}

    x
    0 // retorno do terminal
    y
    0 // retorno do terminal
```

### Operadores Ternários
São usados quando existe a verificação de uma condição com dois resultados distintos possíveis.

Sintaxe

```jsx
    Condição ? expressão1 : expressão2 ( condição ? true : false)
    // a condição é verdadeira ou falsa? se verdadeira acione a expressão1 se falsa acione a expressão2
```

Ex:

```jsx
    function isUserValid(bool) {
    return bool;
    }

    var answer = isUserValid(true) ? "You may enter" : "Acess Denied";
```

### switch
São usados quando a condição tem inúmeras possibilidades

Ex:
```jsx
    function moveCommand(direction){
    var whatHappens;

    switch (direction) {
    case "forward":
    whatHappens = "your encounter a monster";
    break;
    case "back":
    whatHappens = "you arrived home";
    break;
    case "right":
    whatHappens = "you found a river";
    break;
    case "left":
    whatHappens = "you run into a troll";
    break;
    default:whatHappens = "please enter a valid direction";
    }
    return whatHappens;
    }
 ```

O comando break; faz com que o switch pare se a condição se verificar.
Ex:

```jsx
    var state = prompt("enter state");

    switch(state) {
    case "NY":
    document.write("New York");
    break;
    case "TX":
    document.write("Texas");
    break;
    default:
    document.write("unknown");
    break;
    }
```

---

## Truthy_Falsy

Valores **Truthy** são os que são representados por **true** em contexto booleano.

Valores **Falsy** são todos os que são representados por **false** em contexto booleano.

Saber se os valores são Truthy ou Falsy é especialmente importante quando queremos testar algum valor, por exemplo, numa condicional com **if.**(o if precisa de um valor booleano para verificar se entra na condiçao ou cai no else por exemplo).

Em javascript os valores **Falsy** são:

- undefined
- null
- NaN
- 0 e -0
- " " (string vazia)
- false

Os valores **Truthy** são todos os outros que não são Falsy.

Ex: Testando se 1 e 0 são valores Truthy ou Falsy:

```jsx
    var teste
    if (1) {teste = true; } else {teste = false;}
    true // retorno do terminal

    if (0) {teste = true; } else {teste = false;}
    false // retorno do terminal
```

---

## Operadores_Lógicos

Operadores Lógicos servem para combinar ou inverter valores booleanos.

**&& (and) -** retorna o valor true se ambos os operandos forem verdadeiros

Ex: Atribuindo valores ás variáveis x e y e testando os valores de ambas em simultaneo.

```jsx
    var x = 3
    var y = 7

    x === 3 && y === 7
    true

    x === 4 && y === 7
    false
```

**|| Or** - retorna o valor true se um dos operandos forem verdadeiros.

```jsx
    var x = 3
    var y = 7

    x === 3 || y === 4
    true
```

**! - (Not / Opposit)** - Inverte o valor booleano em questão.

```jsx
    var x = 3

    x === 3
    true

    !x === 3
    false
```

---

## Loops

**for()** Loop

```jsx
    for (init; condition; final-expression) {result}
```

ex:
```jsx
    for ( let i = 0; i < 10; i++){
    document.write(i);
    }
```

**while()** Loop
```jsx
    let count = 1;

    while ( count < 5) {
    document.write(count);
    count++;
    }
```

---

## Funções

Funções servem essencialmente para executar um bloco de código num ponto especifico do programa. São especialmente uteis para lançar partes especificas de código repetidamente.

Exemplos de funções já existentes:

```jsx
    alert()
    console.log()
```

Os parêntesis indicam a execução da função e podem contem elementos dentro, chamados argumentos, são informações que são inseridas dentro da função.

Para declarar uma função usamos:

```jsx
    function myFunction() {
    document.write("in a function");
    }

    myFunction()
```

Inserindo informações dentro da função:

```jsx
    myfunction (a,b,c);
```

A segunda forma para criar uma função seria:

```jsx
    let sayBye = function() {
    console.log("Bye");
    }

    sayBye()
```

Retornado valores da função:

```jsx
    return value;
```

A função recebe um input (dentro do parêntesis), faz a sua operação e exporta os seus dados através do comando return:

![Javascript%20Guia%20abd0081575724baca2f50716e5ea77d6/file_funcoes.png](file_funcoes.png)

```jsx
    function multiply (a, b) {
    return a * b
    }

    multiply(5,10)
```

Return sempre termina a função. Qualquer código dentro da função depois da palavra return é ignorado.

Retornar múltiplos valores numa função:

Return apenas retorna um valor especifico, contudo, podemos retornar multiplos valores, retornando um Array, ou um Objeto.

Ex: função retornado um array com multimos valores:

```jsx
    function myfunction() {
    return [1, 2, 3,]
    }

    myfunction()
    [ 1, 2, 3 ] // retorno
```

Acessando elementos do array diretamente:

```jsx
    myfunction() [2]

    3 // retorno
```

Ex: função retornando um objeto:

```jsx
    function myfunction() {    
    return{ prop1: 1,        
    				prop2: 'arroz',        
    				prop3: true
    			}

    myfunction()
    {prop1: 1, prop2: 'arroz', prop3: true} // retorno
```

Acessando propriedades do objeto diretamente:

```jsx
    myfunction().prop2
    'arroz'
```

---

### Passando arrays e objectos para dentro das funções como parâmetros:

Da mesma forma que podemos retornar arrays e objetos das funções, tambem podemos passar arrays e objetos para dentro das funções.

 ### Array:

 Ex: criamos uma variável com um array,

```jsx
    var arr = [1,2,3]
    undefined
```

depois criamos uma função simples que só retorna um parâmetro:

```jsx
    function myfunction(x) {return x}
```

de seguida invocamos a função passando o array como parâmetro, a função retornará os valores do array:

```jsx
    myfunction(arr)
    [ 1, 2, 3 ]
```

Modificando a função, podemos também retornar apenas um valor do array, dando como parâmetro o array inteiro:

```jsx
    function myfunction2(x) {return x[1];}

    myfunction2(arr)
    2 //retorno
```

### Objeto:

ex: 
Criamos um objeto com 3 propriedades:

```jsx
    var obt = {
    … prop1: 1,
    … prop2: ‘arroz’,
    … prop3: true,
    … }
```

depois criamos uma função simples que só retorna um parâmetro:

```jsx
    function myfunction(x) {
    … return x}
```

de seguida invocamos a função passando o objeto como parâmetro, a função retornará os valores do objeto:

```jsx
    myfunction(obt)
    {prop1: 1, prop2: ‘arroz’, prop3: true} //retorno
```

Podemos invocar tambem uma propriedade especifica do objeto quando invocamos a função:

```jsx
    myfunction(obt).prop2
    ‘arroz’
```

Modificando a função, podemos também retornar apenas uma propriedade do objeto, dando como parâmetro o objeto inteiro:

```jsx
    function myfunction2(x) {return x.prop2}

    myfunction2(obt)
    'arroz' //retorno
```

---

### Escopo da função:
Quando criamos uma variável dentro duma função, ela não existe fora desta.

---

### Valor Padrão

Podemos colocar um valor padrão (que será usado caso nao seja passado nenhum parametro) nos atributos duma função:

Ex:

```jsx
    function soma3( **a** **=** 1, **b** **=** 1, **c** **=** 1){
    **return** a **+** b **+** c
    }

    // resultado será 3 se nao for passado nenhum atributo na função soma3
```
 ---
Em muitos casos, o valor this é determinado pela forma como a função é chamada. Ele não pode ser assinado durante a execução, e isso pode ser diferente a cada vez que a função é chamada. 

ES5 introduziu o método bind para estabelecer o valor this da função, independentemente de como ela seja chamada, e ECMAScript 2015 introduziu o arrow functions, cujo this é lexicalmente delimitado (o valor this é estabelecido segundo o escopo de execução no qual está inserido).

---

## Escopo

Existem apenas 2 tipos de escopos em javascript: **Global e Local**.

Por definição quando definimos uma variável o escopo desta é global. Caso a definamos dentro de uma função por exemplo, ela apenas existirá dentro desta (local).

Variáveis definidas globalmente (ou seja, fora de funções especificas) são acedidas normalmente por funções. (já que existem no root, global.)
	
----

## Manipulando o DOM

Adicionando Javascript a uma página HTML podemos:

- Adicionar, remover ou Modificar quaisquer elementos e atributos HTML da página.
- Modificar todos os estilos CSS da página.
- Javascript também pode reagir a todos os eventos HTML na página
- Javascript pode criar eventos novos na página.

[15%20Manipulando%20o%20DOM/untitled](https://www.notion.so/15%20Manipulando%20o%20DOM/untitled)

[https://www.w3schools.com/js/js_htmldom.asp](https://www.w3schools.com/js/js_htmldom.asp)
Para manipularmos o DOM da página usamos os chamados DOM selectors (seletores).

 Os mais comumente usados são:

```jsx
    document.getElementsByTagName("nome_da_tag")

    document.getElementsByClassName("nome_da_classe")

    document.getElementById("id_do_elemento")

    .
```

Selecionam os elementos do DOM através da Tag, Classe e Id. Note que no caso da seleção por id, a palavra Element está no singular em vez do plural, Elements, tal se deve a que ............

Alternativamente podemos usar:

```jsx
    document.querySelector("h1")
```

Quando usamos document.querySelector("") apenas o primeiro elemento é selecionado. no exemplo acima apenas o primeiro elemento h1 é selecionado. 
	
Para selecionarmos todos os elementos h1 utilizamos:

```jsx
    document.querySelectorAll("h1")
```

Os seletores queryselector são mais atuais e recomendáveis do que os getElementBy, contudo é muito comum encontrar-se os getELementBy.

```jsx
    getAtribute("") - retorna o valor de um elemento.
    setAtribute("") - atribui um valor especifico a um elemento.
 ```
Exemplo:

Html:

Primeiro selecionamos o html e depois retornamos ou atribuímos o valor ao elemento:

document.querySelector("p").getAttribute("id");

document.querySelector("p").setAttribute("id", "second");

no caso atribuimos o valor "second" ao ID, que anteriormente era "first".

**Changing Styles:**

className

classList

classList.add

classList.remove

classList.toggle

innerHTML

parentElement

children

**É fundamental colocar os seletores em variáveis**

 ---
 
 ## Objetos

Objetos servem para agrupar vários dados num só grupo.

Um objeto é uma coleção de propriedades, e uma propriedade é uma associação entre um nome (ou chave) e um valor. 
Em javascript é caracterizado pelo simbolo: {}


Ex - Criando o objeto pessoa:
```jsx
    pessoa = { }
```


Adicionando propriedades e valores ao objeto pessoa:
```jsx
    pessoa = {
    		altura: 1.75,
    		peso: 72 
			 }
```


Chamando o objeto pessoa:
```jsx
    pessoa
    { altura: 1.75, peso: 72 }
```


Acessando um valor do objeto pessoa:
```jsx
    pessoa.altura
    1.75
```

Atribuir outro valor a um parametro do objeto:

```jsx
    pessoa.altura = 1.80
    1.8
```

---

### Principais objetos Built-in:
- Math
- Date
- String
- Number
- Date

Ex:
```jsx
    let result = new Date().toDateString();
    console.log(result);
```

 ---

## DOM Events

Lista referencia de eventos:
[https://developer.mozilla.org/en-US/docs/Web/Events](https://developer.mozilla.org/en-US/docs/Web/Events)

Para chamar esperar por um evento utilizamos o método addEventListener()

Exemplo adicionando uma função ao click de um botão:
html:
```html
    <button>Click me!</button>
```

Primeiro atribuimos uma variável ao seletor, no caso button, como o seletor escolhido é por tag name, ele vai referenciar uma array, por tal, temos de definir especificamente qual valor da array, no caso o primeiro botão do código, seria o [0].

Com a variavel corretamente atribuída podemos então adicionar a função especifica ao click do botão, o método addEventListener aceita dois paramentros dentro do parenteses, o primeiro indica o evento, o segundo a ação a ser executada a quando do evento.

```jsx
    var button = document.getElementsByTagName("button")[0];

    button.addEventListener("click", function() {console.log("CLICK!!");})

    /* Traduzindo: adicione o seguinte event listener à variável button: quando o usuário clicar execute a função console.log("CLICK!!)
```

Eventos mais comuns com o mouse:
- click
- mouseenter
- mouseleave
- lista mouse events: [https://developer.mozilla.org/pt-BR/docs/Web/API/MouseEvent](https://developer.mozilla.org/pt-BR/docs/Web/API/MouseEvent)

Exemplo: Adicionando tarefas numa to-do list com um botão:
html:
```html
    <input id="userinput" type="text" placeholder="enter items">
    <button id="enter">Enter</button>

    <ul>
    <li>Notebook</li>
    <li>Jello</li>
    <li>Spinach</li>
    </ul>
```

Primeiro vamos atribuir variáveis aos 3 elementos que vamos usar: o campo de input, o botão e a lista.

Depois das variáveis atribuídas adicionamos a função especifica ao botão.

O método createElement cria um elemento, no caso li.

O método appendChild acrescenta um elemento como ultimo a outro elemento.

O método createTextNode cria um node de texto com um valor especifico, no caso o valor do input.

```jsx
    var button = document.getElementById("enter");
    var input = document.getElementById("userinput");
    var ul = document.querySelector("ul");

    button.addEventListener("click", function(){ 
    	var li = document.createElement("li");
    	li.appendChild(document.createTextNode(input.value));
    	ul.appendChild(li);
    })
```

Adicionando to-do na lista através da tecla Enter:

Utilizando o exemplo acima, mudamos a variável para o input, de seguida, mudamos o evento para keypress atribuimos o valor event(pode ser qualquer nome) à função, depois adicionamos a condicional if para se o keycode é igual 13. 13 corresponde à tecla Enter.

```jsx
    input.addEventListener("keypress", function(event){
    	if (event.keyCode === 13) {
    	var li = document.createElement("li");
    	li.appendChild(document.createTextNode(input.value));
    	ul.appendChild(li);
    }
```

No método keyPress cada tecla tem um número pré-definido (Key code).

Para ver a lista das key code:
[https://www.cambiaresearch.com/articles/15/javascript-char-codes-key-codes](https://www.cambiaresearch.com/articles/15/javascript-char-codes-key-codes)

---

## Arrow_Functions
Comparativo entre a sintaxe padrão de uma função em Javascript e sintaxe duma Arrow Function:

Padrão:
```jsx
    function myFnc() {
    .....
    }
    ​
```

Arrow Function:
```jsx
    const myFnc = () => {
    ......
    }
    ​
```

Exemplos:
```jsx
    function first() {
    	var greet = "Hi!";

    function second(){
    	alert(greet);
    }

    return second;
    }

    var newFunc = first();
    newFunc();

    const first = () => {
    const greet = "Hi!";
    const second = () => {
    alert(greet);
    }

    return second;
    }

    const newFunc = first();
    newFunc();
```

---

## Destructuring
Novo no ES6, o destructuring permite aceder com maior facilidade a dados dentro de arrays e objetos.

```jsx

/* Ex: Aqui acedemos às propriedades do objeto (obj) da forma convencional, atribuindo a cada uma delas uma variável. */

    const obj = {
    	player: "Bobby",
    	experience: 100,
    	wizardLevel: false
    }

    const player = obj.player;
    const experience = obj.experience;
    let wizardLevel = obj.wizardLevel;

    /* E aqui fazemos a mesma operação usando o recurso destructuring, código fica bastante mais simplificado: */

    const obj = {
    	player: "Bobby",
    	experience: 100,
    	wizardLevel: false
    }

    const { player, experience } = obj;
    let { wizardLevel } = obj;
```

---

## ES7
### Método includes
Determina se um determinado elemento está presente numa array (retorna true ou false).

 ```jsx
    Ex:

    const pets = ["dog" , "cat" , "bat"];

    pets.includes("dog")
    true

    pets.includes("bird")
    false
```

### Exponentiation operator
Permite usar o expoente (multiplicar o mesmo numero base sobre sim mesmo x(expoente) vezes) de forma simplificada.

```jsx
    Ex:

    const square = (*x*) => x**2;
    const cube = (*y*) => y**3;

    square(5)
    25

    cube(3)
    27
```



---

## ES8

### String padding - permite adicionar espaços em uma string:
```jsx
    .padStart()
    .padEnd()

    ex:
    "gato".padStart(20)
    " gato"

    "golfinho".padEnd(10);
    "golfinho "

    Object.values.....
    ..........

    Object.entries........
    .................
```

### Async Await



### Modules (Exports & Imports)
Permite escrever código modular, ou seja código que poderá ser divido em multiplos ficheiros. Para isso, dentro de um ficheiro JS poderemos importar código de outro ficheiro JS.

Exemplo exportando de um ficheiro nomeado person.js:

```jsx
    const person = { 
    		name: "Alexandre"
    }
    export default person
```

Exemplo Importando desse ficheiro:

```jsx
    import person from './person.js'
```

### this e bind
A palavra this em javascript referência diferentes valores em Javacript:

Quando está sozinha ela referência o Objecto Global.

 It has different values depending on where it is used:

 - In a method, this refers to the **owner object**.
 - Alone, this refers to the **global object**.
 - In a function, this refers to the **global object**.
 - In a function, in strict mode, this is undefined.
 - In an event, this refers to the **element** that received the event.
 - Methods like call(), and apply() can refer this to **any object**.

Numa função tradicional o valor do **this** pode variar de acordo com quem chamou a função.

Quando usamos uma arrow function o **this** não varia o seu valor.

Exemplo do uso do this:

```jsx
    const pessoa = {
    saudacao: 'Bom dia!',
    }

    falar() {
    	console.log(this.saudacao)
    }

    pessoa.falar()

    // o this está referenciando o objeto pessoa
```


### Callbacks
.forEach

O método forEach() executa uma dada função em cada elemento de um array.

```jsx
    const fabricantes = ['Mercedes', 'Audi', 'BMW']

    function imprimir(nome, indice) {
    	console.log(indice + 1 + "." + nome)
    }

    fabricantes.forEach(imprimir)

    /*Retorno */
    1.Mercedes
    2.Audi
    3.BMW
```

**.filter**
```jsx
    const notas = [7.7, 6.5, 5.2, 8.9, 3.6, 7.1, 9.0]
    // Sem callback

    let notasBaixas = []

    for (let i in notas) {
    	if (notas[i] < 7) {
    	notasBaixas.push(notas[i])
    }
    }

    console.log(notasBaixas)

    // Com callback

    notasBaixas = notas.filter(function(nota){
    	return nota < 7
    })

    console.log(notasBaixas)
```


### Função Factory
A função factory permite-nos criar objectos através duma função:

```jsx
    Ex:

    function criarProduto(nome,preco) {
    return {
    	nome: nome,
    	preço: preco,
    	desconto: 0.1
    }

    }

    console.log(criarProduto("Notebook", 2399.89))
    console.log(criarProduto("Celular", 1290.89))
```

### Hoisting
Hoisting pode ser traduzido como içamento ou elevamento.

Em javascript as funções e variáveis são Hoisted. Ou seja elas são movidas para o topo do escopo.

Isso permite que voce use uma função ou variável antes de ser declarada.

```jsx
    Exemplo:

    a = 2

    var a;

    //é o mesmo que:

    var a;
    a = 2
```

### IIFE -> Immediately Invoked Function Expression

Uma IIFE permite criar uma função imediatamente quando ela é invocada, fugindo do escopo global.

```jsx
    Sintaxe:

    // IIFE -> Immediately Invoked Function Expression

    // Função Auto-invocada permite fujir do escopo global

    (function() {
    	console.log("Será executado na hora!")
    	console.log("Foge do escopo mais abrangente!")
    })()
```

---