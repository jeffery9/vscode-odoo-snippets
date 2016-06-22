# odoo-snippets README

ported from sublime-odoo-snippets

## install from vscode market

for the moment, still not published to vscode market.  

## local installation

## installation manually

copy the folder into `.vscode/extensions` directory, for windows this folder is  `%homepath%/.vscode/extensions`, and for linux is `~/.vscode/extensions`

after copied the extension, vscode should found and load it.


## install using packaged extension

## download pre-build package

download the file  `odoo-snippets-xxxx.vsix` from this repo.

**should release pre-build package when the extension been updated**

### build package by youself

#### install build tool

run `npm install -g vsce ` to install vsce tools

#### build vscode pakcage 

goto odoo-snippets folder, then run `vsce package`, vcse should create a packaged extension.

### install extension

open the package from vs code, it shoudl been installed.




**Enjoy!**