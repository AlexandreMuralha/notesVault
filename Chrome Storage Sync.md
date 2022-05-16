Chrome Storage é uma API que visa salvar, acessar e controlar alterações de dados do usuário ou configuraões no contexto de uma extensão do Google Chrome. 

Semelhante ao localStorage API, porem otimizada especificamente para as extensões do Google Chrome.

## Manifest
Para usarmos a API teremos primeiro que indicar a permissão no ficheiro manifest.json da nossa extensão. 
Por exemplo:
```json
{
	"manifest_version": 3,
	"name": "A minha extensão",
	"description": "World Time Extension",
	"version": "0.1",
	"permissions": [
		"storage"
	],
	...
}
```


## Uso
To store user data for your extension, you can use either `storage.sync`:

```js
chrome.storage.sync.set({key: value}, function() { 
console.log('Value is set to ' + value);});chrome.storage.sync.get(['key'], 
	function(result) {  console.log('Value currently is ' + result.key);});
```

or `storage.local`:

```js
chrome.storage.local.set({key: value}, function() {  
console.log('Value is set to ' + value);});chrome.storage.local.get(['key'], 
	function(result) {  console.log('Value currently is ' + result.key);});
```

When using `storage.sync`, the stored data will automatically be synced to any Chrome browser that the user is logged into, provided the user has sync enabled.

When Chrome is offline, Chrome stores the data locally. The next time the browser is online, Chrome syncs the data. Even if a user disables syncing, `storage.sync` will still work. In this case, it will behave identically to `storage.local`.


-----------------
Links:
https://developer.chrome.com/docs/extensions/reference/storage/
https://sunnyzhou-1024.github.io/chrome-extension-docs/apps/storage.html