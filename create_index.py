#!/usr/bin/env python
'''This script creates an Index of all md files for every directory in the current one, it all also creates a master index file for all those indexes created'''
'''
Note1: This script creates index files listing all markdown files for each sub-directory in the current one, it will ignore any sub-directory inside those main directories.
Note2: In order to keep the navigation consistent (in github, obsidian, etc) it´s important to name the files/folders without spaces.
'''

import os
from os import walk
__author__ = "Alexandre Muralha"
__version__ = '0.3'

dir_names = next(os.walk('.'))[1]

main_index = open('index.md', 'w')
main_index.write('# main index')

for dir_name in dir_names:
    current_directory_name = os.path.split(
        os.getcwd())[1]  # gets current directory name
    # gets all filenames on the current Dir, [] if no file
    filenames = next(walk('./{}'.format(dir_name)), (None, None, []))[2]
    file = open("./{}/$index_{}.md".format(dir_name, dir_name), "w")
    file.write('{} Index'.format(dir_name) + '\n')
    print('{} Index - Done'.format(dir_name))
    
    # Main index
    # ignores directories starting with . or _
    if dir_name[0] != '.' and dir_name[0] != '_':
        # adds each dir index to main index
        main_index.write('\n' + '* [' + dir_name + ']' + '(' + dir_name + '/$index_' + dir_name + '.md)')

    for filename in filenames:
        if filename.endswith(".md"):  # apenas ficheiros .md
            # descarta o proprio index da lista
            if filename != "$index_{}.md".format(dir_name):
                filename_without_extension = filename[:-3]
                file.write(
                    '\n' + '* [' + filename_without_extension + ']' + '(' + filename + ')')
                main_index.write(
                    '   \n' + '* [' + filename_without_extension + ']' + '(' + filename + ')')
    file.write('\n\n')
    file.write('[Back](./../index.md)')
    file.close()

main_index.write('\n---\n')
main_index.write('this file is generated by [create_index_all_dir.py](Link) script.')
main_index.close()

print('---------------')                      
print('index.md - Done')