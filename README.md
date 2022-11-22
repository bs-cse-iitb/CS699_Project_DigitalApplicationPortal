# CS699_Project
step 1. Install Required Packages
1.sudo apt update
2.sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib
3.sudo pip3 install virtualenv
4.pip install django-mailjet

step 2. setup database
1.sudo -u postgres psql
2.CREATE DATABASE databasename;
3.CREATE USER projectusername WITH PASSWORD 'password';
4.ALTER ROLE projectusername SET client_encoding TO 'utf8';
ALTER ROLE projectusername SET default_transaction_isolation TO 'read committed';
ALTER ROLE projectusername SET timezone TO 'UTC';
5.GRANT ALL PRIVILEGES ON DATABASE databasename TO projectusername;
6.quit command: \q

step 3. activate virtual environment
1.python3 -m virtualenv environentname
2.source environentname/bin/activate


step 4.Install more packages
1.pip install Django psycopg2

step 5. database config
change settings.py for required username, password, and databasename.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'databasename',
        'USER': 'projectusername',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

step 6. change allowed hosts in settings.py
ALLOWED_HOSTS = ['your_server_domain_or_IP']

step 7. make migrations and setup
1. python manage.py makemigrations
2. python manage.py migrate


step 7. ready to run
python manage.py runserver 0.0.0.0:8000

step 8. access via browser
http://server_domain_or_IP:8000
