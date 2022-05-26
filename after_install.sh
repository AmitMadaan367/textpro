#!/usr/bin/env bash
cd /var/www/html

source env/bin/activate

pip install -r requirements.txt
# Restart services

mv /var/www/html/apac.conf /etc/apache2/sites-available 

sudo ln -s /etc/apache2/sites-available/apac.conf /etc/apache2/sites-enabled/

sudo rm /etc/apache2/sites-enabled/000-default.conf

sudo service apache2 restart




