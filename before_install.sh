#!/usr/bin/env bash
cd /var/www/html
mkdir textpro

sudo apt update
sudo apt-get install python3-pip python3-dev apache2 libapache2-mod-wsgi-py3  -y

sudo pip install virtualenv
sudo virtualenv env
source env/bin/activate
