### Componentes
- When using react, think of your UI as a bunch of separate components.
- Conceitualmente, componentes são como funções JavaScript. Eles aceitam entradas (chamadas “props”) e retornam elementos React que descrevem o que deve aparecer na tela.
- Components can be create as **Functions** or **Classes** .
- These days (2021) the more common way of create components is using **Functions with hooks**
- Um componente recebe parâmetros, chamados `props` (abreviação de propriedades), e retorna uma hierarquia de elementos para exibir através do método `render`


```jsx
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}
```

Essa função é um componente React válido porque aceita um único argumento de objeto “props” (que significa propriedades) com dados e retorna um elemento React. Nós chamamos esses componentes de “componentes de função” porque são literalmente funções JavaScript.


Você também pode usar uma classe ES6 para definir um componente:
```jsx
class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}
```
Os dois componentes acima são equivalentes do ponto de vista do React.


> Sempre inicie os nomes dos componentes com uma letra maiúscula.
O React trata componentes começando com letras minúsculas como tags do DOM. Por exemplo, `<div />` representa uma tag div do HTML, mas `<Welcome />` representa um componente e requer que `Welcome` esteja no escopo.

<br>

### Props (propriedades)
São informações que podemos passar para um componente para alterar o comportamento deste, assim como temos atributos no HTML.


Por exemplo, o código seguinte renderiza “Hello, Sara” na página:
```jsx
function Welcome(props) {  
  return <h1>Hello, {props.name}</h1>;
}

const element = <Welcome name="Sara" />;
ReactDOM.render(
  element,
  document.getElementById('root')
);
```

#### Compondo Componentes
Componentes podem se referir a outros componentes em sua saída. Isso nos permite usar a mesma abstração de componente para qualquer nível de detalhe. Um botão, um formulário, uma caixa de diálogo, uma tela: em aplicativos React, todos esses são normalmente expressos como componentes.

Por exemplo, nós podemos criar um componente `App` que renderiza `Welcome` muitas vezes:
```jsx
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}

function App() {
  return (
    <div>
      <Welcome name="Sara" />      
	  <Welcome name="Cahal" />      
	  <Welcome name="Edite" />    
	</div>
  );
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
);
```

> Tipicamente, novos aplicativos React tem um único componente `App` no topo.


#### Props são somente de Leitura
Em react um componente não deve nunca alterar os seus próprios props. Deve ser sempre portanto uma função Pura.

Uma função é considerada impura quando altera a sua própria entrada, por exemplo:
```jsx
function withdraw(account, amount) {
  account.total -= amount;
}
```
Já as funções puras não alteram as suas entradas e sempre retornam o mesmo resultado para as mesmas entradas, por exemplo:
```jsx
function sum(a, b) {
  return a + b;
}
```
**Todos os componentes React tem que agir como funções puras em relação ao seus props.**

### Método render
O método `render` retorna uma _descrição_ do que você deseja ver na tela. React recebe a descrição e exibe o resultado. Em particular, `render` retorna um **elemento React**, que é uma descrição simplificada do que renderizar. A maioria dos desenvolvedores do React usa uma sintaxe especial chamada “JSX”, que facilita a escrita desses elementos
Por exemplo, sintaxe `<div />` é transformada em tempo de compilação para :
```js
React.createElement ('div')
```









### Hooks
React Hooks are functions that let us hook into the React state and lifecycle features from function components.
- useState -> Returns a stateful value and a function to update it.
- useEffect -> Perform side effects in function components.


---
Links:
Pensando do jeito React: https://pt-br.reactjs.org/docs/thinking-in-react.html
