sudo apt update
sudo apt install python3-pip python3-dev apache2 -y
pip install virtualenv
virtualenv env
source env/bin/activate
pip install django gunicorn
