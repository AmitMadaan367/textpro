# Install libaries
cd /var/www/backend
virtualenv -p python3 venv
#!/bin/bash
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
# Restart services
sudo service apache2 restart




