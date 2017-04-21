#!/usr/bin/env bash

apt-get update
apt-get install -y python python-pip python-virtualenv nginx memcached #gunicorn nmap
pip install --upgrade pip
pip install virtualenv Flask

mkdir /home/www/ && cd /home/www/
virtualenv env
source env/bin/activate
pip install Flask
mkdir flask_project && cd flask_project
cp -f /vagrant/flask_app.py app.py 

mkdir static
cat > static/index.html <<EOF
<h1>Test!</h1>
EOF

rm /etc/nginx/sites-enabled/default
touch /etc/nginx/sites-available/flask_project
ln -s /etc/nginx/sites-available/flask_project /etc/nginx/sites-enabled/flask_project
cp -f /vagrant/nginx_flask /etc/nginx/sites-enabled/flask_project

/etc/init.d/nginx restart
cd /home/www/flask_project/
python app.py &
#gunicorn app:app -b localhost:8000 &