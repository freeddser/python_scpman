#!/bin/bash
#code by scpman

echo "Git commit tools!"
echo "https://github.com/freeddser/go_example.git"
git status
git add .
read -p "Enter the commit Desc!" Desc
git commit -a -m "$Desc"
git push -u origin master

