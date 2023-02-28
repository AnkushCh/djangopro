# Django Project 

## Instructions to install and run this project

Requirements:

python version= 3.8.x

Open project folder in any IDE ex: vscode

download all the requirements 
```bash
pip install -r requirements.txt
```

create the supper user:
```bash
python manage.py createsuperuser
```
create user for Employee, Manager, Client

create migrations before running project
```bash
python manage.py makemigrations
```
apply the migrations to DB;
```bash
python manage.py migrate
```

run the django server: 
```bash
python manage.py runserver
```

