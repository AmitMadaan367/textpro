#!/usr/bin/env bash
cd /var/www/html
mkdir textpro

cd textpro

sudo apt update
sudo apt install python3-pip python3-dev apache2 libapache2-mod-wsgi-py3 -y
pip install virtualenv
virtualenv env
source env/bin/activate
