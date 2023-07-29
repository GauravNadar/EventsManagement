# EventsManagement

### make sure ***python version 3.9*** and ***postgres 15*** is installed in system

1. git clone https://github.com/GauravNadar/EventsManagement.git

2. EventsManagement  ---> root folder

3. cd EventsManagement

4. python -m venv {env_name} 

5. {env_name}\Scripts\activate -- to activate in windows

6. {env_name}/Scripts/activate.bat //In CMD
 
7. {env_name}/Scripts/Activate.ps1 //In Powershel

8. source {env_name}/bin/activate //in Linux

9. cd events_mgmt

10. pip install -r requirements.txt

---

### for creating database and user open SQL shell and type below commands

`CREATE DATABASE {yourdbname};`

`CREATE USER {youruser} WITH ENCRYPTED PASSWORD '{yourpassword}';`

`GRANT ALL PRIVILEGES ON DATABASE {yourdbname} TO {youruser};`

`ALTER DATABASE {yourdbname} OWNER TO {youruser};`

---

### change setting.py to point to your local db

```
DATABASE_NAME = os.environ.get("DB_NAME", 'yourdbname')
DATABASE_USERNAME = os.environ.get("DB_USERNAME", 'youruser')
DATABASE_PASSWORD = os.environ.get("DB_PASSWORD", 'yourpassword')
DATABASE_HOST = os.environ.get("DB_HOST", 'localhost')
DATABASE_PORT = os.environ.get("DB_PORT", '5432')
```
---

## run below migrate command to migrate initial django tables

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

go to --> [Events Home Page](http://127.0.0.1:8000/home/)
