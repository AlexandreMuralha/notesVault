
### Git - fundamentos 

Git é um sistema de controle de versões (versionamento).

* Any Sequence of bytes = SHA1 Hash
* Every object in git has its own SHA1
* SHA1 are Unique

---

Fundamental Git Rules:
1. The current branch tracks new commits.
2. When you move to another commit, git updates your working directory.
3. Unreacheble objects are garbage collected.

------

 Estágios dentro do Git:
- Working Directory
- Staging Area
- .git Directory (repositório)

**Working Directory** -> Git add -> **Staging Area** -> git commit -> **.git Directory**

---

### Configuração
```bash
$ git config --global user.name "nome" #seta o username
$ git config --global user.name #mostra o nome setado
$ git config --global user.mail "email" #seta o email do user
$ git config --global core.editor editor #configura o editor padrão nos commits sem -m, ex: vim, vscode)
$ git config --list #mostra as configurações
```

---

### Comandos Básicos
```bash
$ git init #Inicia o versionamento dentro da pasta atual
```

```bash
$ git add [nome-do-arquivo.extensão] #Adiciona o arquivo ao estágio de controle
$ git add . #Adiciona todos os arquivos do diretório ao estágio de controle
```

```bash
$ git status #Indica o status do projeto - quais arquivos estão fora do controle, etc.
```

```bash
$ git commit #Comita os arquivos que estão no estágio de controle e abre o editor para escrever mensagem
$ git commit -m "mensagem do commit" #Comita os arquivos que estão no estágio de controle)
$ git commit -a -m "mensagem" #Comita os arquivos pulando a etapa de add
$ git commit -ammend -m "mensagem" #Edita/adiciona ao ultimo commit realizado
```

```bash
$ git log #Mostra um log de todos os commits já efectuados no projeto
$ git log -p #Mostra todos os commits do projeto mais o de diff de cada um deles)
$ git log -p -1 / -2 / etc #Mostra o log e o diff do ultimo ou ultimos commits
$ git log --pretty=oneline #Mostra o log, um commit por linha
```

```bash
$ git diff #Mostra todas as alterações efetuadas nos arquivos
$ git diff [ash-do-comit] #Mostra todas as alterações efetuadas entre o commit atual e especificado no comando
$ git diff [ash-do-comit] [ash-do-comit] #Mostra todas as alterações efetuadas entre os dois commits especificados no comando
$ git --staged #Mostra todas as alterações nos arquivos que estão na stagging area
$ gitk #Abre o visualizador de relatórios
$ git reset head [nome-do-arquivo] #Remove da stagging area um arquivo adicionado por engano
*$ git checkout --[nome do arquivo] #descarta as mudanças efectuadas no arquivo, retomando o arquivo para o ultimo commit
$ git rm [nome-do-arquivo] #Remove do registro do repo os arquivos nomeados
```

---

### Tags
Tags servem como pontos de atalho para o um determinado status do sistema.(são geralmente utilizadas com as versões).

```bash
$ git tag #lista as tags existentes no sistema
$ git tag -a [tag] -m "mensagem" #adiciona uma tag ao ultimo commit
$ git tag -a [tag] [sha1] -m "mensagem" #Adiciona uma tag a um commit especifico)
$ git show [tag] #Mostra detalhes sobre o commit associado à tag em questão
$ git checkout [tag] #Volta os ficheiros ao estado do commit associado a tag
$ git checkout master #volta os ficheiros ao branch master
$ git tag -d [tag] #apaga a tag indicada
```

Dois tipos de tags:

* lightweight
* annotated

---

### Branches
Branches permitem criar ambientes de desenvolvimento diferentes para o mesmo projeto, podendo fazer commits sem alterar o master. Ideal para testes.

```bash
$ git branch [nome-do-branch] #criar um branch novo
$ git checkout [nome-do-branch] #muda o ambiente para o branch definido)
$ git checkout -b [nome-do-branch] #cria e muda o ambiente para o branch novo
$ git merge [nome-do-branch] #faz o merge entre o branch novo e o master ou destino. Nota: comando tem que ser dado no branch de destino.
```

----

### Outros Comandos
```bash
$ git clone [url] #Clona um projeto do url para o repositorio local (dar git init antes)
$ git push origin master #envia os arquivos do branch master atual para o servidor(origem)
$ git pull origin master #copia os dados novos origin para o master local(faz merge automático)
$ fetch origin [nome-do-branch] #copia os dados novos do origin para um branch novo local
#origin = Nome do original clonado
```

----

### Git Rebase
```bash
$ git rebase master #faz o rebase entre o branch atual e o master
```

* The point of merging is that it preservs all history exacty has it happened.
* Rebasing helps you refactoring the project history so it looks cleaner and easier to read.
* **When in doubt, it´s recomended to Merge.**

Diference between **Merge** and **Rebase:**

* Git Merge apply all unique commits from branch A to branch B in one commit with the final result.

* Git Merge doesn´t rewrite commit history, just adds one more.

* Git Rebase gets all unique commits from both branches and applies them one by one.

* Git Rebase rewrites commit history but doesn´t create extra commits

---

## GitHub
```bash
$ git remote -v #verifica se há alguma ligação remota configurada
$ git remote add origin [url] #adiciona o repositório remoto ao local
$ git push -u origin master ##envia os dados e cria o vinculo entre o repositório local e o remoto
$ git push #envia os dados do repositório local para o remoto)
**
```

Github special files:
* readme.md
* license.md
* contributing and contributors
* changelog
* support
* code_of_conduct

```bash
$ git fetch #baixa os heads/tags/objetos sem fazer o merge
$ git pull #Incorpora as mudanças de rep para o branch local. Equivale a git fetch seguido de git merge fetch_head
```

----

### GitHub Workflow

![img_20181217_140458.236](img_20181217_140458.236.jpg)

**Workflow Colaboração GitHub:**

* Encontrar o projeto para trabalhar.
* Fazer um fork do projeto.
* Clonar o fork para a máquina local.
* Fazer localmente as alterações ao projeto.
* Comitar ARquivos e fazer o push.
* Fazer o Pull Request e enviar o fork para a analise do autor do projeto.

**Releases / Tags**

```bash
$ git push --tags #envia as tags criadas localmente para o repo no github
```

Releases are Based on Tags.
Releases can have release notas in md format.
Releases can have binary files attached.

----

### Forks

Forks are diferent from branchs
Forks are only in Github
Forks - Remove Clone
Pull Request - Pedido para o autor do projeto aceitar as alteraçoes efectuadas.
Branches all work in the same repo while forks work in different repositories

Typical Conflitcts on Merging:

* Editing on the same line
* Editing an already deleted file

Merge conflicts needs to be solved before merge will happen.

Local tools to solve merge conflitcts:
Local diff Tools: 

* kdiff 3
* p4merge
* vimdiff3
* Beyond compare

----

### Gists

Gists are a simples way to share snippets and notes with others (side github project)

* Don´t support directories
* Repository-based
* Public or Secret
* Downloadable

Can be used to embed code in a site.

**Github Pages**
Static site Hosting without server-side code
Site is effectively a repo
Can Be Created online or Offline

**Github Issues**
Can be: 

* Bugs
* Work tasks
* Enhancements
* Ideias

Can be assigned to someonelse
Can be associated with Pull Requests
Combined towards a milestone

Labels can be applyed on issues (github specific)

Default Build-in Labels:

* Bug
* Duplicate
* Enhancement
* Help Wanted
* Question
* Wont Fix
* Good First Issue
* Invalid

Milestones:

* Group Issues
* Trck Progress

Can Have:

* Due Date
* Completion Percentagem
* Open/Closed Issues

----

### Github Organizations

**Organization on Github:**

* Shared account to work on projects (group of people working on projects)
* Fine grained acess to manage access
* Free or Paid

**Teams**

* Struture of the group
* Can be Nested (with hierarchy)
* Acess to Repositories
* Notifications
* Team Page

-----

**tags:** #git #github 
**links:** 
