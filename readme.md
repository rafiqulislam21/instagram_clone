# How to setup project

## Steps

### Creating virtual environment (using cmd)

` python -m venv .venv `

### Activate virtual environment

` .venv\Scripts\activate `

### Check installed packages

` pip freeze `

### Install packages from requirements.txt

` pip install -r requirements.txt `

### export packages into requirements.txt

` pip freeze > requirements.txt `
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

____

### Api documentation

Here root is `http://127.0.0.1:8000/`

- `http://127.0.0.1:8000/api/schema/swagger-ui/#/`
- `http://127.0.0.1:8000/api/schema/redoc`