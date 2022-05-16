### Indentation

By default, VSCode will try to guess your indentation options depending on the file you open.

You can turn off indentation guessing via:

```
 "editor.detectIndentation": false
```

You can customize this easily via these 3 settings in File > Preferences > Settings:

```shell
The number of spaces a tab is equal to. This setting is overriden based on the file contents when `editor.detectIndentation` is true."editor.tabSize": 4,

Insert spaces when pressing Tab. This setting is overriden based on the file contents when `editor.detectIndentation` is true."editor.insertSpaces": true,

When opening a file, `editor.tabSize` and `editor.insertSpaces` will be detected based on the file contents. Set to false to keep the values you ve explicitly set, above."editor.detectIndentation": false,
```

-----

**tags:** #vscode  
**links:** 
