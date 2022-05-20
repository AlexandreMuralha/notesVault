from os import walk
import os

filenames = next(walk('.'), (None, None, []))[2]  # [] if no file



arquivo = open("index.md", "w")

arquivo.write("# Index of " + os.getcwd()  + "\n")

for name in filenames:
    if name.endswith(".md"): # lista apenas ficheiros .md
      if name != 'index.md': # descarta o proprio index da lista
        filenamewithoutmd = name[:-3]
        arquivo.write('\n' + '* ['+ filenamewithoutmd + ']' + '(' + name + ')')

arquivo.close()

print('index of files created')
print(os.getcwd())