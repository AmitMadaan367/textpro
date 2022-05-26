#!/bin/bash
sudo apt update
sudo apt install python3-pip python3-dev apache2 -y
pip install virtualenv
virtualenv env2
source env2/bin/activate