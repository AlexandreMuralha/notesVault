## PostgreSQL

https://www.postgresql.org/

### Características Gerais:
- Compatível com ACID
- Banco Transacional (uses WAL/RED)
- Suporta Particionamento
- Possui Controle de Concorrência Multiversão (MVCC)
- Busca de texto completo
- Indexação com vários tipos de algoritmos (B-Tree, GisT, etc.)
- Permite operações de manutenção em modo online
- Operações geoespaciais (PostGIS)
- Possui linguagem procedural

---

### Conectividade:
- Usa o TCP/IP padrão. Possui um protocolo de transmissão chamado libpq.
- Uma vez estabelicida a conexão, nos comunicamos com o PostgreSQL enviando comandos.
- Sua linguagem combina o padrão SQL:2008 com comandos de manutenção específicos.
- O SGBDR serve uma instância a partir de uma única porta TCP/IP.

---

### Terminologia
Termos acadêmicos, baseados em álgebra relacional, mais comuns no PostgreSQL:

| Termo Comum	 | Termo Postgres  |
| -------------  |-------------    |
|  Tabela     	 | Relação         | 
|  Linha     	 | Tupla           | 
|  Coluna     	 | Atributo        |
|  Bloco de Dados| Página (no disco)|
|  Coluna     	 | Buffer (na mémoria)|

---

## Comandos Básicos
### Criar um Banco de Dados:
```SQL
CREATE DATABASE nome_do_banco;
```

### Criar um Banco de Dados com opções:
```SQL
CREATE DATABASE nome_do_banco
WITH 
OWNER = nome_do_proprietario
ENCODING = "UTF8"
LC_COLLATE = "pt_BR.UTF-8"
LC_CTYPE = "pt_BR.UTF-8"
TABLESPACE = pg_default
CONNETCTION LIMIT -1;
```

### Apagar um Banco de Dados:
```SQL
DROP DATABASE nome_do_banco;
```

### Conceder / Retirar Privilégios a um Usúario:
```SQL
-- Concede todas as permissões:
GRANT ALL ON DATABASE nome_do_banco TO nome_do_usuario;
-- Permite que o usuário se conecte ao banco de dados:
GRANT CONNECT ON DATABASE nome_do_banco TO nome_do_usuario;
-- Retira os privilégios de um usuário:
REVOKE ALL PRIVILEGES ON DATABASE nome_do_banco FROM nome_do_usuário;
```

### Criar Tabelas
```SQL
CREATE TABLE nome_da_tabela(
nome_coluna tipo_dado constraints,
nome_coluna2 tipo_dado constraints,
)
```

```SQL
--Exemplo tabela clientes
CREATE TABLE clientes(
	cod_cliente INT PRIMARY KEY,
	nome_cliente VARCHAR(20) NOT NULL,
	sobrenome_cliente VARCHAR(40) NOT NULL
);
```

```SQL
--Exemplo tabela produtos
CREATE TABLE produtos(
	cod_produto INT PRIMARY KEY,
	nome_produto VARCHAR(30) NOT NULL,
	descricao TEXT NULL,
	preco NUMERIC CHECK(preco > 0) NOT NULL,
	qtde_estoque SMALLINT DEFAULT 0
);
```

```SQL
--Exemplo tabela pedidos com chaves estrageiras referenciando as chave primárias das tabelas anteriores:
CREATE TABLE pedidos(
	cod_pedido SERIAL PRIMARY KEY,
	cod_cliente INT NOT NULL REFERENCES clientes(cod_cliente),
	cod_produto INT NOT NULL,
	qtde SMALLINT NOT NULL,
	FOREIGN KEY (cod_produto) REFERENCES produtos(cod_produto)
);
```

### Inserir Registros em Tabelas
```SQL
INSERT INTO nome_tabela(coluna1,coluna2,coluna3)
VAlUES(dado,dado2,dado3)
```

```SQL
--Exemplo inserindo dois registros na tabela clientes
INSERT INTO clientes(cod_cliente,nome_cliente,sobrenome_cliente)
VALUES (1,'Alexandre', 'Fernandes');
INSERT INTO clientes(cod_cliente,nome_cliente,sobrenome_cliente)
VALUES (3,'Ana', 'Teixeira');
```

```SQL
--Exemplo vários registros na tabela produtos
INSERT INTO produtos(cod_produto,nome_produto,descricao,preco,qtde_estoque)
VALUES(1,'Álcool Gel','Garrafa de álcool em gel de 1 litro', 12.90, 20),
(2,'Luvas de Latex', 'Caixa de luvas de latex', 32.50, 25),
(3,'Pasta de Dentes', 'Tubo de pasta de dentes 90g', 3.60, 12),
(4,'Sabonete', 'Sabonete Antibacteriano', 3.50, 5),
(5,'Enxaguante Bocal', 'Antisséptico Bucal de 500ml', 17.00, 28);

```

```SQL
--Exemplo vários registros na tabela produtos (o cod_pedido é automático pois foi definido como SERIAL):
INSERT INTO pedidos(cod_cliente, cod_produto,qtde)
VALUES
(1,2,3),
(2,3,2),
(1,3,4);

```

---

## Consultas

### Consulta todos os registos de uma tabela
```SQL
SELECT nome_da_coluna FROM nome_da_tabela;
```

```SQL
--Consulta todos os registos da tabela clientes
SELECT * FROM clientes;
```

### Consulta de colunas especificas de uma tabela
```SQL
--Consulta apenas a coluna nome_cliente
SELECT nome_cliente FROM clientes;

--Consulta as colunas nome_cliente e sobrenome_cliente
SELECT nome_cliente, sobrenome_cliente FROM clientes;
```

### Filtrar Consultas com cláusula WHERE
```SQL
SELECT colunas FROM tabelas WHERE condição-filtragem;
```

```SQL
--Filtra a consulta apenas para mostra o cliente com cod_cliente = 1
SELECT * FROM clientes WHERE cod_cliente = 1;
```

### Ordenar Resultados com ORDER BY
```SQL
--Ordena a consulta por ondem alfabética ascendente ou descente de uma coluna especifica. ASC é o padrão.
SELECT colunas 
FROM tabelas 
WHERE condição-filtragem 
ORDER BY coluna ASC/DESC;
```

```SQL
--Consulta todos os registos da tabela produtos e ordenando-os por ordem alfabetica do nome do produto
SELECT * FROM produtos ORDER BY nome_produto;
```

```SQL
--Consulta todos os registos da tabela produtos e ordenando-os por ordem alfabetica do nome do produto
SELECT nome_produto FROM produtos ORDER BY nome_produto;
```

### Consultas limitadas por LIMIT e OFFSET
Permitem obter uma parte especifica das linhas retornadas por uma consulta.
Contagem -> quantidade de linhas a exibir.
Deslocamento -> quantas linhas serão puladas antes de iniciar a contagem.
```SQL
SELECT coluna
FROM tabela
ORDER BY coluna
LIMIT contagem/all
OFFSET deslocamento
```

```SQL
--Consulta os 4 registos com o preço mais baixo da tabela produtos.
SELECT * FROM PRODUTOS
ORDER BY PRECO
LIMIT 4;
```

```SQL
--Consulta os 3 registos mais caros, descartando os dois primeiros.
SELECT * FROM PRODUTOS
ORDER BY PRECO DESC
LIMIT 3
OFFSET 2;
```

### Consultas usando Operadores de Comparação
Permitem comparar dois valores retornando um valor booleano.

```SQL
-- Operadores de Comparação:
< menor que
> menor que
<= menor ou igual a 
>= maior ou igual a
= igual a
!= diferente de
```

```SQL
-- Retorna todos os registos da tabela produto cujo preço é maior do que 12.00
SELECT nome_produto, preco
FROM produtos
WHERE preco > 12.00;
```

```SQL
-- Retorna todos os registos cuja quantidade em stock seja menor ou igual a 20 e maior do que 10.
SELECT nome_produto, qtde_estoque
FROM produtos
WHERE qtde_estoque <= 12 AND qtde_estoque > 10;
```

```SQL
-- Retorna todos os registos cujo nome é diferente de Refrigerante.
SELECT nome_produto, qtde_estoque
FROM produtos
WHERE nome_produto != 'Refrigerante';
```

### Operador BETWEEN
Permite consultas com filtros de intervalos de dados.
```SQL
SELECT colunas
FROM tabela
WHERE coluna BETWEEN valor1 AND valor2

```

```SQL
--Retorna os produtos com preço entre 10 e 20 reais.
SELECT nome_produto, preco
FROM produtos
WHERE preco BETWEEN 10.00 AND 20.00;

```

```SQL
--Retorna os produtos com preço entre 3 e 5 reais ou entre 10 e 20 reais.
SELECT nome_produto, preco
FROM produtos
WHERE 
	preco BETWEEN 3.5 AND 5 OR
	preco BETWEEN 10.00 AND 20.00;

```

### Cláusula UPDATE
Permite alterar/atualizar registros em tabelas.
```SQL
UPDATE tabela
SET coluna = novo_valor
WHERE coluna = valor_índice; --o registo que vai ser alterado
```

```SQL
--Altera o valor da descricao no produto com o cod_produto = 4 para 'Sabonete Normal'.
UPDATE produtos
SET descricao = 'Sabonete Normal'
WHERE cod_produto = 4;
```

```SQL
--Altera o preço do produto com o cod_produto = 3, para 3.96.
UPDATE produtos
SET preco = 3.96
WHERE cod_produto = 3;
```

### Apagar Registros com DELETE FROM e TRUNCATE TABLE
Permite apagar linhas de uma tabela.
DELETE FROM: Excluir linhas específicas de uma tabela
```SQL
DELETE FROM nome_tabela
WHERE condições --condiçoes de exclusão
```

```SQL
--apaga o registro do produto cujo cod_produto é 4.
DELETE FROM produtos
WHERE cod_produto = 4;
```

```SQL
--apaga o registro do produto cujo cod_produto é 4.
DELETE FROM produtos
WHERE cod_produto = 4;
```

```SQL
--apaga o registro do produto cujo nome é 'Manteiga'.
DELETE FROM produtos
WHERE nome_produto = 'Manteiga';
```


TRUNCATE TABLE: Limpa todos os registros de uma tabela (não apaga a tabela).
```SQL
TRUNCATE TABLE nome_tabela
```

```SQL
--Apaga todas as linhas da tabela pedidos
TRUNCATE TABLE pedidos;
```

----

## Tipos de Dados

### Tipos Numéricos
| Tipo      	 | Descrição         |
| -------------  |-------------      |
|  smallint    	 | Inteiros 2 bytes  | 
|  int    	     | Inteiros 4 bytes  | 
|  bigint     	 | Inteiros 8 bytes      |
|  numeric(p,e)  | Ponto flutuante, precisão=dígitos;escala=casas decimais|
|  real    	     | 32 bits, até 6 dígitos decimais de precisão|
|  double precision| 64 bits-variável, até 15 dígitos de precisão|
|  serial   	 | 32 bits, com sinal, números sequenciais|
|  big serial    | 64 bits, com sinal, números sequenciais|
|  money     	 | 64 bits, com sinal(2^63 valores). Valores monetários|

### Tipos de String
| Tipo      	 | Descrição         |
| -------------  |-------------      |
|  text   	            | varchar tamanho ilimitado.Mais usado.| 
|  char(n), character(n)| caracteres de tamanho fixo, com padding e n caracteres| 
|  varchar(n)   	    | varchar de tamanho ilimitado até n caracteres.|

### Tipos de Data e Hora
| Tipo      	 | Descrição         |
| -------------  |-------------      |
|  date  	                | 4 bytes, datas com precisão de 1 dia  | 
|  time (sem timezone)      | 8 bytes, hora sem fuso horário, precisão de 1 microssegundo| 
|  time with time zone      | 12 bytes, hora com fuso horário, precisão de 1 microsegundo|
|  timestamp (sem timezone) | 8 bytes, data e hora sem fuso horário, precisão de 1 microssegundo|
|  timestamp with time zone | 12 bytes, armazena data e hora com fuso horário, precisão de 1 microsegundo|
|  interval                 | 16 bytes, armazena faixas de tempo com precisão de 1 microssegundo|

### Outros Tipos
| Tipo      	 | Descrição         |
| -------------  |-------------      |
|  boolean  	       | Tipo lógico; 8bits (1 byte): True (1/yes/on) ou False (0/no/off)| 
|  cidr                | 7 ou 19 bytes, endereços de rede IPv4 e IPv6| 
|  inet                | 7 ou 19 bytes, endereços de hosts IPv4 e IPv6|
|  macaddr             | 6 bytes (48 bits), Endereços MAC Adress|
|  Geometric Types     | Armazena informações relacionadas com fig. geométricas, como linhas, polígnos, pontos, etc.|
|  Tipos de Enumeração | Criádos pelo usuário, para conjuntos de valores definidos e imutáveis|
|  tsvector / tsquery  | Tipos para busca completa de texto em documentos.|

https://www.postgresql.org/docs/9.5/datatype.html

---
tags: #bancos-da-dados #sql 