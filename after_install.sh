#!/usr/bin/env bash
cd /var/www/html

source env/bin/activate

cd textpro

pip install -r requirements.txt


#deleting old conf file
sudo rm /etc/apache2/sites-available/000-default.conf


mv /var/www/html/textpro/000-default.conf /etc/apache2/sites-available 

# Restart services
sudo service apache2 restart




