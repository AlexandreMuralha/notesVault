
# XML

O XML — acrônimo para eXtensible Markup Language - é um padrão para a formatação e transmissão de dados de fácil entendimento tanto para humanos quanto para máquinas.

> A principal função e utilização da XML é transmitir dados através da web.

No padrão xml, podemos guardar informações em:
- **Elementos** -> é a forma padrão e mais comum no mercado.
- **Atributos** -> usada geralmente em duas situações: reduzir o tamanho do arquivo (menos tags) ou para separar os dados gerais(ex: telefone e nome) das informaçoes de identificação única(ex. id ou cpf).



Exemplo da estrutura de um ficheiro xml usando elementos:
```xml
<?xml version="1.0" encoding="UTF-8" ?> 
<correntistas> 
<!-- Dados de duas 'pessoas' --> 
	<pessoa> 
		<tipo>física</tipo> 
		<nome>Alexandre Fernandes</nome> 
		<numero>000.000-00</numero> 
	</pessoa> 
	<pessoa> 
		<tipo>jurídica</tipo> 
		<nome>Alexandre Fernandes SA</nome> 
		<numero>111.111-11</numero> 
	</pessoa> 
</correntistas>
```


O mesmo exemplo, desta vez acrescentando o atributo conta:
```xml
<?xml version="1.0" encoding="UTF-8" ?> 
<correntistas> 
	<conta agencia="0456-2"> 
		<tipo>física</tipo> 
		<nome>Alexandre Fernandes</nome> 
		<numero>000.000-00</numero> 
	</conta> 
	<conta agencia="5678-9"> 
		<tipo>jurídica</tipo> 
		<nome>Alexandre Fernandes SA</nome> 
		<numero>111.111-11</numero> 
	</conta> 
</correntistas>
```

Usando só atributos em de vez dos elementos:
```xml
<?xml version="1.0" encoding="UTF-8" ?> 
<correntistas> 
	<conta agencia="0123-4" tipo="fisica" nome="José Maria" numero="000.000-00" /> 
	<conta agencia="5678-9" tipo="jurídica" nome="José Maria SA" numero="111.111-11" /> 
</correntistas>
```

---

Regras para boa formação de um arquivo XML

- Todo documento XML, além da tag introdutória, deve ter um único elemento (tag) que sirva como raiz para todos os demais elementos do documento;
- XML é case sensitive, portanto difere letras maiúsculas e minúsculas, devendo tomar cuidado com o uso de CamelCases.
- Todo elemento XML deve ser iniciado e fechado, exceto o que define a versão do XML usada e outras definições de tag única.
- Comentários em XML são iguais ao HTML (<!--comentário-->) .
---
**tags**: #xml
**links**:
https://www.youtube.com/watch?v=9408HdOYhAA