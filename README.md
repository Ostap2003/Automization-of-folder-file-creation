# Automization-of-folder-file-creation

### Module that automizes directories and folders creation on your PC

***
#### SYNTAX
To create folders just type their names using ```/``` like so: ```dir1/dir2...```
To create files in the folders type their names using ```;``` separator.

* if you want several files to be created in a specific folder, then
  use the following syntax: ```[folder1.txt,folder2.txt]```
  use comma as a separator inside square brackets

**Example of command:**<br>
The input needs to look like this:<br>
```dir1/dir2/dir3 file1;file2;file3```<br>
```dir1/dir2 ;[file1.txt,file2.txt,file3.txt]```

***! USE EMPTY SPACE AS A SEPARATOR BETWEEN DIRS NAMES AND FILE NAMES, otherwise an exception will occur.***
</br>
***                            
**IF** you don't want to create any files in a specific folder, then
the input needs to look like this:
```dir1/dir2 ;file_in_folder2.txt```  <- here we created file only in the second directory

**IF** you don't want to create any files in a directory, then type ```;``` separators instead of the file names.
  the number of the separators needs to be **(number of created folders - 1)**, otherwise
  an exception will occur.<br>
  **EXAMPLE:** ```dir1/dir2 ;```
  
