# Git cheatsheet

## Desfaz todas as alterações:
```shell
git checkout * 
removes all changes made to unstaged files in git status eg
```

## Adicionar Repositório remoto
1. In the command line, navigate to the root directory of your project.
2. Initialize the local directory as a Git repository.
    ```shell
    git init -b main
    ```
    
3. Stage and commit all the files in your project
    ```shell
    git add . 
	git commit -m "initial commit"
    ```

4. Create a new repository on GitHub.com. To avoid errors, do not initialize the new repository with _README_, license, or `gitignore` files. You can add these files after your project has been pushed to GitHub. At the top of your repository on GitHub.com's Quick Setup page, click  to copy the remote repository URL.

5.  In the Command prompt, add the URL for the remote repositorywhere your local repository will be pushed.
    ```shell
    $ git remote add origin  <REMOTE_URL> 
    # Sets the new remote
    $ git remote -v
    # Verifies the new remote URL
    ```
    
6.  Push the changes in your local repository to GitHub.com.
    ```shell
    $ git push origin main
    # Pushes the changes in your local repository up to the
	remote repository you specified as the origin
    ```
