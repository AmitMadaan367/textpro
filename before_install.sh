#!/bin/bash

sudo apt update
sudo apt install python3-pip python3-dev ffmpeg supervisor apache2 -y
pip install virtualenv
virtualenv env
source env/bin/activate
pip install -r requirements.txt

sudo rm -rf /var/www/backend
