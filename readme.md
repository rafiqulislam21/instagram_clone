# How to setup project

## Steps

### Creating virtual environment (using cmd)

` python -m venv ienv `

### Activate virtual environment

` .venv\Scripts\activate `

### Check installed packages

` pip freeze `

### Install packages from requirements.txt

` pip install -r requirements.txt `
____

## Initial commands used in create project

### Create django project

` django-admin startproject projectName `

### Create django app

` python manage.py startapp watchlist_app `
____

### Migrations

- ` python manage.py makemigrations `
- ` python manage.py migrate `

### Create super user

` python manage.py createsuperuser `

____

### Admin panel info

- username: ` user `
- passowrd: ` user `
