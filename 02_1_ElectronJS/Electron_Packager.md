# Electron Packager
“Electron Packager is a command line tool and [Node.js](Node.md) library that bundles [[Electron]]-based application source code with a renamed Electron executable and supporting files into folders ready for distribution.”

----

## 1. Instalar Electron packager
Para instalar o Electron packager. Executamos os seguintes comandos na pasta do projeto:

```bash
# for use in npm scripts
npm install electron-packager --save-dev
```

Se for necessário criar o package.json > usar npm init

---

## 2. productname e electron version
Para instalar e adicionar a versão do Electron usamos o comando:

```bash
npm install --save-dev electron
```

Depois definimos o productname,, para isso adicionamos o campo productname no arquivo package.json

```json
{ 
	"name": "electron-tutorial-app", 
	"productName": "Electron tutorial app", 
	"version": "0.1.0", 
	"main": "main.js", 
	"devDependencies": { 
	"electron": "^1.4.3", 
	"electron-packager": "^8.1.0" }
}
```

---

## 3. Gerando os executáveis.
Finalmente para gerar o executável usamos no terminal:

### Windows

```bash
electron-packager . electron-tutorial-app --overwrite --asar=true --platform=win32 --arch=ia32 --icon=assets/icons/win/icon.ico --prune=true --out=release-builds --version-string.CompanyName=CE --version-string.FileDescription=CE --version-string.ProductName="Electron Tutorial App"
```

### Linux

```bash
electron-packager . electron-tutorial-app --overwrite --asar=true --platform=linux --arch=x64 --icon=assets/icons/png/1024x1024.png --prune=true --out=release-builds
```

### MacOS

```bash
electron-packager . --overwrite --platform=darwin --arch=x64 --icon=assets/icons/mac/icon.icns --prune=true --out=release-builds
```

### Flags

```bash
--overwrite: Substitui todos os ficheiros no diretório de destino.

--plataform: plataforma para a qual fazemos o build

--arch: a arquitectura para qual fazemos o build

--icon: caminho do icone do app

--prune: executa o **npm prune -production.**  Remove packages desnecessários.

--out: nome do diretório de destino.
```

No Windows, mudar: **string.ProductName=“Electron Tutorial App”**

Os arquivos serão gerados na pasta **release-builds**.

---

## 4. Scripts

Podemos criar scripts de forma a não termos que digitar sempre os mesmos comandos. Para tal adicionamos as seguintes linhas em scripts do package.json:

```json
{ 
	"name": "electron-tutorial-app", 
	"productName": "Electron tutorial app", 
	"version": "0.1.0", 
	"main": "main.js", 
	"devDependencies": { 
	"electron": "^1.4.3", 
	"electron-packager": "^8.1.0" 
	}, "scripts": { 
	"package-mac": "electron-packager . --overwrite --platform=darwin --arch=x64 --icon=assets/icons/mac/icon.icns --prune=true --out=release-builds",
	"package-win": "electron-packager . electron-tutorial-app --overwrite --asar=true --platform=win32 --arch=ia32 --icon=assets/icons/win/icon.ico --prune=true --out=release-builds --version-string.CompanyName=CE --version-string.FileDescription=CE --version-string.ProductName=\"Electron Tutorial App\"",    
	"package-linux": "electron-packager . electron-tutorial-app --overwrite --asar=true --platform=linux --arch=x64 --icon=assets/icons/png/1024x1024.png --prune=true --out=release-builds" 
	}
}
```

Agora podemos fazer o build digitando apenas o seguinte comando para cada uma das plataformas:

```bash
npm run package-win
npm run package-linux
npm run package-mac
```

[Documentação do Package Manager](https://electron.github.io/electron-packager/master/)

---
**id:** 20200519_105844
**tags:** #electron #electron-packager #javascript 
**links:**
https://www.christianengvall.se/electron-packager-tutorial/
https://electron.github.io/electron-packager/master/