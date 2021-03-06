### JSX

JSX ->  **JavaScript XML**  é uma extensão de sintaxe para JavaScript.

Por príncipio o React opta por separar conceitos (em componentes) ao invés de separar tecnologias (js, css, html em ficheiros separados não são usado) seguindo o [Princípio da Responsabilidade Única](Princípio%20da%20Responsabilidade%20Única.md). O JSX constituí-se como a sintaxe ideal para este tipo de abordagem.

O uso do JSX não é obrigatório, é porém, altamente recomendado, a maioria das pessoas acha prático como uma ajuda visual quando se está trabalhando com uma UI dentro do código em JavaScript. Ele permite ao React mostrar mensagens mais úteis de erro e aviso.

> O React Dom usa o `camelCase` como convenção para nomes de propriedades ao invés dos atributos do HTML, por exemplo, `class` se transforma em `className` em JSX e `tabindex` se transforma em `tabIndex`.

### Exemplos
No exemplo abaixo, declaramos uma variável chamada `name` e então a usamos dentro do JSX ao envolvê-la com chaves:
```jsx
const name = 'Maria Pereira';
const element = <h1>Hello, {name}</h1>;

ReactDOM.render(
  element,
  document.getElementById('root')
);
```

Podemos usar qualquer expressão Javascript válida dentro das chaves
em JSX. Por exemplo, `2 + 2`, `user.firstName`, ou `formatName(user)` são todas expressões JavaScript válidas.

No exemplo abaixo, incorporamos o resultado da chamada de uma função JavaScript, `formatName(user)`, dentro de um elemento `<h1>`.

```jsx
function formatName(user) {
  return user.firstName + ' ' + user.lastName;
}

const user = {
  firstName: 'Maria',
  lastName: 'Pereira'
};

const element = (
  <h1>
    Hello, {formatName(user)}!  
  </h1>
);

ReactDOM.render(
  element,
  document.getElementById('root')
);
```


### Especificando Atributos com JSX

Para especificar strings literais como atributos usamos aspas:

```jsx
const element = <div tabIndex="0"></div>;
```

Para incorporar uma expressão JavaScript em um atributo usamos chaves:

```jsx
const element = <img src={user.avatarUrl}></img>;
```

Não envolva chaves com aspas quando estiver incorporando uma expressão JavaScript em um atributo. Você deveria ou usar aspas (para valores em string) ou chaves (para expressões), mas não ambos no mesmo atributo.

Tags JSX podem conter elementos filhos:

```jsx
const element = (
  <div>
    <h1>Hello!</h1>
    <h2>Good to see you here.</h2>
  </div>
);
```

---
**ID**:  2112161433
**tags**: #
**references**:
https://pt-br.reactjs.org/docs/introducing-jsx.html