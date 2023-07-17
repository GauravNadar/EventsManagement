# EventsManagement

make sure python version 3.9 is installed in system

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

python manage.py runserver

go to --> http://127.0.0.1:8000/home/
