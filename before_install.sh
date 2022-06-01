#!/usr/bin/env bash
cd /var/www/html
apt update
apt-get install python3-pip python3-dev apache2 libapache2-mod-wsgi-py3 python3-venv  -y
python3 -m venv env
source env/bin/activate
pip install gunicorn
