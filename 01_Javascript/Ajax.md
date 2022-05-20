
**AJAX -> Asynchronous JavaScript and [XML](XML.md)** -> Permite inserir código de uma base de dados / servidor dentro de um website sem ter que carregar todo o site novamente de cada vez.

ex: um site que possua um chat integrado (ex:facebook) precisaria de recarregar toda a página de cada vez que uma mensagem nova fosse enviada sem um recurso como AJAX.

---

### XMLHttpRequest - Propriedades

[Exemplo Completo de Requisição XMLHttpRequest](Requisição_XMLHttpRequest.md)

#### readyState
```Javascript
var ajax = new XMLHttpRequest()
console.log(ajax.readyState)
```

ReadyState -> retorna o cabeçalho da requisição. Representa o estado atual da sua requisição

Os estados podem ser os seguintes:
- **0**: UNSENT - Requisição não iniciada
- **1**:  OPENED - Requisição estabelecida com o servidor
- **2**: HEADERS_RECEIVED-  Pedido recebido
- **3**: LOADING - Processando pedido
- **4**: DONE - Solicitação concluída e resposta pronta

### status
```Javascript
var ajax = new XMLHttpRequest()
console.log(ajax.status)
```
status -> indica o status da resposta do servidor à sua requisição.
Alguns status codes HTTP mais comuns:
- 200 -> OK
- 201 -> Created
- 400 -> Bad request - The request could not be understood by the server due to malformed syntax. The client should not repeat the request without modifications.
- 401 -> Acess denied
- 403 -> Forbidden
- 404 -> Not found

Lista completa -> https://httpstatuses.com/

---
### exemplo - GET
```javascript
// estancia os objetos
var ajax = new XMLHttpRequest()
var documento;

//define o tipo de resposta
ajax.responseType = "json";

// configura o evento para quando o mudar o estado
ajax.onreadystatechange = function() {
// so exibe quando o readyState é igual a 4 e o status igual a 200 (ok)
	if(ajax.readyState == 4 && ajax.status === 200) {
		documento = ajax.response;
		console.log(documento);
	}
}

// define o verbo (get) e o url
ajax.open("GET", "http://jsonplaceholder.typicode.com/posts/1", true)

// faz a requisição ao servidor
ajax.send();
```


Links:
- https://developer.mozilla.org/pt-BR/docs/Web/API/XMLHTTPRequest