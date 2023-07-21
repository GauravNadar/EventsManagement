# EventsManagement

make sure python version 3.9 and postgres 15 is installed in system

git clone https://github.com/GauravNadar/EventsManagement.git

EventsManagement  ---> root folder

cd EventsManagement

python -m venv {env_name} 

{env_name}\Scripts\activate -- to activate in windows

{env_name}/Scripts/activate.bat //In CMD
 
{env_name}/Scripts/Activate.ps1 //In Powershel

source {env_name}/bin/activate //in Linux

cd events_mgmt

pip install -r requirements.txt

for creating database and user open SQL shell and type below commands

CREATE DATABASE {yourdbname};
CREATE USER {youruser} WITH ENCRYPTED PASSWORD '{yourpassword}';
GRANT ALL PRIVILEGES ON DATABASE {yourdbname} TO {youruser};
ALTER DATABASE {yourdbname} OWNER TO {youruser};

change setting.py to point to your local db

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '{yourdbname}', 
        'USER': '{youruser}',
        'PASSWORD': '{yourpassword}',
        'HOST': '127.0.0.1', 
        'PORT': '5432',
    }
}

run below migrate command to migrate initial django tables

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

go to --> http://127.0.0.1:8000/home/
