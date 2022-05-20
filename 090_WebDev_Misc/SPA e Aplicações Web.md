---
id: 2111221432
title: SPA e Aplicações Web
date-created: 211122_1411T14:32
---
### Site Estático vs Site Dinâmico
**Site Estático** -> Páginas estáticas, ou seja, as páginas são sempre as mesmas e são alteráveis diretamente no código pelo programador. 
Não existe interação com um banco de dados.
O cliente faz a requisição da página ao servidor, que retorna diretamente os conteúdos na forma de páginas estáticas.
Um site estático é quase sempre mais rápido mas ao mesmo tempo mais limitado do que o dinâmico.
![](static_page_dia.jpg)

**Site Dinâmico** -> Conteúdo da página é dinâmico, ou seja, a página é gerada em tempo real acedendo a um banco de dados.
O cliente faz a requisição ao servidor, que consulta o banco de dados, sendo a página entregue gerada dinamicamente.
![](dinamic_page_dia.jpg)


### Aplicação Web
**Aplicação Web** é um aplicativo (software) que vivem no servidor web, pode ser acessado em um browser convencional, e, apesar de algumas vezes ser parecido com um website dinâmico é geralmente mais complexo e possui mais requesitos.
Exemplos: gmail, evernote, notion, figma, twitter

### Aplicação Web vs Single Page Aplication
As **Aplicações Web** tradicionais precisam recarregar toda a página para ter o conteúdo atualizado.
- Cada vez mudamos e de página o servidor processa e devolve a página completa (html+css+js) de uma só vez.
- O front-end e o back-end estão numa aplicação só.
- ex: wordpress

As **Single Page Aplication (SPA)** não precisam recarregar toda a página para serem atualizadas.
- O front e back-end são aplicações distintas.
- O front end é construido com frameworks (angular, react, vue) e comunica com o back-end usando [APIs](API.md). 
- Quando a SPA é aberta todo o código html+css+js é obtido do servidor e carregado. Posteriomente, quando navegamos pela SPA o conteudo dinamico vai sendo requesitado ao servidor e adicionado à página apenas usando o formato [JSON](JSON.md) (bastante leve) usando uma [API](API.md).

---
**ID**:  2111221432
**tags**: #WebDev #api 
**references**:
