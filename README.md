## Criar pasta venv

### macos

`python3 -m venv venv`

### ativar
`source venv/bin/activate`

## Rodar projeto
`python manage.py runserver`

## Criar app
`python3 manage.py startapp core`


## Adicionar pasta core ao settings 

`INSTALLED_APPS`

#### EX:

`
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'core',
]
` 
