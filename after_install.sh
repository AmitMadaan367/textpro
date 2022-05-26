#!/usr/bin/env bash
cd /var/www/html

source env/bin/activate

pip install -r requirements.txt


# Restart services
sudo rm /etc/apache2/sites-available/000-default.conf


mv /var/www/html/textpro/000-default.conf /etc/apache2/sites-available 


sudo service apache2 restart




