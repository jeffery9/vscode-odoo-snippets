# odoo-snippets README

ported from [sublime-odoo-snippets](https://github.com/jeffery9/sublime-odoo-snippets)

use [convert-snippets-to-vscode](https://www.npmjs.com/package/convert-snippets-to-vscode) convert sublime-snippet to json file, eg data.json, and then run  `python convert.py`, this commamnd shoudl create snippets for vscode.

## install from vscode market

~~for the moment, still not published to vscode market.~~

just find this from market

## local installation

download the source code from  https://github.com/jeffery9/vscode-odoo-snippets.git

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
