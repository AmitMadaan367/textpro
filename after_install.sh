# Install libaries
cd /var/www/backend
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
sudo fuser -k 8000/tcp

sudo chown -R www-data:www-data /var/www/

# Restart services
sudo service apache2 restart




