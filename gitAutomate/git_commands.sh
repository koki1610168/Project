#!/bin/zsh

function create() {
  python github.py $1
  cd /Users/hachimannoboruju/Documents/Python/Project/$1
  git init
  git remote add origin https://github.com/koki1610168/$1.git
  touch README.md
  touch main.py
  git add .
  git commit -m "Initial Commit"
  git push -u origin master
  charm main.py
}