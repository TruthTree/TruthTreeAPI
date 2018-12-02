# TruthTree

The TruthTree Python backend

## Requirements

1. Python 3.7
2. Django 2.x
3. Pipenv
4. PostgreSQL 9.x+

## Development

    $ pipenv --python 3.7       # creates virtual env
    $ pipenv install --dev      # install dependencies
    $ cp .env.sample .env       # configure your .env file
    $ make migrate              # run migrations for existing apps
    $ make start                # start server

## Deployment

    $ docker build -t truthtree .
    $ docker run -p 8000:8000 truthtree

## Setting Up VSCode

https://code.visualstudio.com/docs/python/environments

    $ pipenv --venv             # where your virtual env exists
    $ code .                    # start VSCode

Then select the interpreter where your virtual env exists. Looks something like this:

    /Users/elusive/.local/share/virtualenvs/django-bootstrap-trBOeQwu

## Appendix

**Starting from Scratch @ben @lantz**

    $ pipenv --python 3.7
    $ pipenv install django djangorestframework psycopg2 python-dotenv
    $ pipenv run django-admin startproject backend .
    $ pipenv run django-admin startapp api
    (create database)
    (configure database - see settings.py)
    $ pipenv run python3 manage.py migrate
    $ python manage.py createsuperuser --email admin@example.com --username admin
    $ pipenv run python3 manage.py createsuperuser --email admin@example.com --username admin
