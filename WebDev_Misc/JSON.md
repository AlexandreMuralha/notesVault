---
id: 2108061412
title: JSON
date-created: 210806_1412
---
**JSON** -> acrônimo para Javascript Object Notation, é uma sintaxe para armazenamento e troca de dados. 

- Formato Padrão de dados na web atual.
- Mais leve e simples do que XML e YAML.
- Independente da linguagem de programação.

Principais aplicações:
- Troca de dados usando APIs.
- Arquivos de configuração.
- Persistência (gravação) de dados em navegadores ou servidores.

---

### Sintaxe
O JSON trabalha em cima de objetos (Documentos), que são conjuntos não-ordenados de dados armazenados em um par **"nome":valor** (campos).

- Os objetos (documentos) são englodos em chaves - {}
- Os nomes-chave são englobados em aspas-duplas - ""
- Os nomes são separados dos valores por dois-pontos - :
- Os pares (campos) são separados por virgulas -,

```json
{
	"nome": "Maria",
	"idade": 34,
	"número": "0000-323",
	"chave2": [
		"string", 
		345, 
		true
	],
	"chave3": {
		"sub-chave": "valor"
	}
}
```

---

### Tipos de Dados

JSON suporta quatro tipos de dados primitivos e dois estruturados:
- String (qualquer caractere Unicode)
- Number
- Boolean
- null
- Array (lista ordenada de valores)
- Object (lista não ordenada de pares nome:valor)

---

### Exemplos

#### Enviando Dados
Criamos um objeto Javascript, que depois é convertido em texto JSON para ser enviado para um servidor remoto, onde poderá ser processado por uma linguagem server side, como Java, PHP etc.
```json
//Cria um objeto Javacript 
var objtoJS = {agencia: "5678-9", tipo: "física", nome: "Maria José", 
numero: "222.222-22"}; 

//Converte o objeto Javascript em texto JSON 
var textoJson = JSON.stringify(objetoJS); 

//Redireciona a página para o endereço especificado, passando, 
// via GET, o texto JSON 
window.location = "processa/json/?conta=" + textoJson;
```

#### Recebendo Dados
Criado um texto JSON, que será convertido em um objeto Javascript e então atribuído a um elemento HTML. Esse exemplo simula, entre outros, a situação em que, através de uma requisição AJAX, ou outro tipo de requisição, recebemos como retorno um texto JSON e precisamos manipulá-lo para acessar e utilizar seus dados.
```json
//Representa um texto JSON (que poderia ter sido recebido de uma requisição, por ex) 
var textoJson = '{"agencia": "5678-9", "tipo": "física", "nome": "Maria José", "numero": "222.222-22"}'; 

//Converte o texto JSON em um objeto Javascript 
var objetoJS = JSON.parse(textoJson); 

//Exibe na tag html com id=resultado os dados da conta 
document.getElementById("resultado").innerHTML = 'Agência: ' + objtoJS.agencia + ' Tipo: ' + objtoJS.tipo + ' Nome: ' + objtoJS.nome + ' Número: ' + objtoJS.numero;
```

#### Armazenando Dados
O exemplo, a seguir, demonstra como armazenar dados no formato JSON. Para isso, será utilizado um objeto Javascript que será convertido em texto JSON e, a seguir, armazenado. Além disso, também será demonstrado como recuperar os dados armazenados.
```json
//Cria um objeto Javacript
var objetoJS = {agencia: "5678-9", tipo: "física", nome: "Maria José", numero: "222.222-22"}; 

//Converte o objeto Javascript em texto JSON 
var textoJson = JSON.stringify(objtoJS); 

//Armazenando os dados no navegador 
localStorage.setItem("stringJSON", textoJson);

```


---
**tags**: #json
**links**:
https://www.json.org/json-pt.html
