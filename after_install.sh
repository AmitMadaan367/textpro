#!/bin/bash
cd /var/www/html/textpro
sudo rm -r env
python3 -m venv env

source env/bin/activate


pip install -r requirements.txt


#deleting old conf file
sudo rm /etc/apache2/sites-available/000-default.conf


mv /var/www/html/textpro/000-default.conf /etc/apache2/sites-available 

# Restart services
sudo service apache2 restart




