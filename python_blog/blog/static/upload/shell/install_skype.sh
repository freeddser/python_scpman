#!/bin/sh
#code by Gavin
#2015-03-07
####install func####
install_skype(){
echo "start to install skype"
sudo apt-get install python-software-properties
sudo add-apt-repository "deb http://archive.canonical.com $(lsb_release -sc) partner"
sudo apt-get update
sudo apt-get install skype
}
install_skype
