#!/bin/bash
# prints the input
function create() {
    cd
    source .env
    python $FOLDERPATH/create.py $1
    cd $FOLDERPATH/$1
    git init
    touch README.md
    git add .
    git commit -m 'Initial Commit'
    git remote add origin https://github.com/$GITHUB_USERNAME/$1.git
    git push -u origin master
}
