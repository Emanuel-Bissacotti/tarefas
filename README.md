# Projeto de estudo python com o framework django
## O que é o projeto
Um CRUD de tarefas e categorias, utilizando banco de dados SQLite, com 2 tabelas relacionais.

Também utiliza templates com HTML para visualização.
<img width="690" alt="image" src="https://github.com/user-attachments/assets/c46ccd93-03a1-4447-97b2-37dffe535f70">

# Lembretes

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
