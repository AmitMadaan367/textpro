#!/usr/bin/env bash
pip install -r requirements.txt
# Restart services

mv /home/ubuntu/apac.conf /etc/nginx/sites-available 

sudo ln -s /etc/apache2/sites-available/apac.conf /etc/apache2/sites-enabled/

sudo rm /etc/apache2/sites-enabled/000-default.conf

sudo service apache2 restart




