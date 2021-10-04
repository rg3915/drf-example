# drf-example

Django REST framework exemplos e testes.


## Este projeto foi feito com:

* [Python 3.9.6](https://www.python.org/)
* [Django 3.2.7](https://www.djangoproject.com/)
* [Django Rest Framework 3.12.4](https://www.django-rest-framework.org/)

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/rg3915/drf-example.git
cd drf-example
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser --username="admin" --email=""
```

## Sumário

* [dr-scaffold](#dr-scaffold)
* [drf-yasg - Yet another Swagger generator](#drf-yasg---yet-another-swagger-generator)
* [djoser](#djoser)
* [Reset de Senha com djoser](#reset-de-senha-com-djoser)
* [Autenticação via JWT com djoser](#autenticação-via-jwt-com-djoser)
* [Django CORS headers](#django-cors-headers)

## dr-scaffold

https://github.com/Abdenasser/dr_scaffold

https://www.abdenasser.com/scaffold-django-apis


dr-scaffold é uma lib para criar models e uma API simples em Django REST framework.


### Experimentando e criando um projeto do zero

```
python -m venv .venv
source .venv/bin/activate
pip install dr-scaffold djangorestframework django-extensions python-decouple
```

Crie um arquivo `.env`

```
cat << EOF > .env
SECRET_KEY=my-super-secret-key-dev-only
EOF
```


Crie um novo projeto.

```
django-admin startproject backend .
```

Edite `settings.py`

```python
# settings.py

from decouple import config

SECRET_KEY = config('SECRET_KEY')

INSTALLED_APPS = [
    ...
    'rest_framework',
    'dr_scaffold',
]
```


#### Exemplo 1

Rodando o comando `dr_scaffold`

```
python manage.py dr_scaffold blog Author name:charfield

python manage.py dr_scaffold blog Post body:textfield author:foreignkey:Author
```

Edite `settings.py`

```python
# settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',
    'dr_scaffold',
    'blog',  # <--
]
```

Edite `urls.py`

```python
# urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]
```

```
python manage.py makemigrations
python manage.py migrate
```


#### Exemplo 2


```
python manage.py dr_scaffold product Product title:charfield price:decimalfield

python manage.py dr_scaffold ecommerce Order nf:charfield

python manage.py dr_scaffold ecommerce OrderItems \
order:foreignkey:Order \
product:foreignkey:Product \
quantity:integerfield \
price:decimalfield
```

Edite `settings.py`

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'dr_scaffold',
    'blog',  # <--
    'product',  # <--
    'ecommerce',  # <--
]

```

Edite `urls.py`

```python
...
path('product/', include('product.urls')),
path('ecommerce/', include('ecommerce.urls')),
...
```

Não se esqueça de editar `ecommerce/models.py`

```python
from product.models import Product

```

```
python manage.py makemigrations
python manage.py migrate
```


## drf-yasg - Yet another Swagger generator

https://github.com/axnsan12/drf-yasg/

[drf-yasg](https://github.com/axnsan12/drf-yasg/) é uma outra biblioteca para gerar a documentação com Swagger e reDoc.

```
pip install -U drf-yasg

pip freeze | grep drf-yasg >> requirements.txt
```

Edite `settings.py`

```python
INSTALLED_APPS = [
   ...
   'django.contrib.staticfiles',  # required for serving swagger ui's css/js files
   'drf_yasg',
   ...
]
```

Edite `urls.py`

```python
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('product/', include('product.urls')),
    path('ecommerce/', include('ecommerce.urls')),
    path('admin/', admin.site.urls),
]

# swagger
urlpatterns += [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),  # noqa E501
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # noqa E501
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # noqa E501
]
```

## djoser

https://djoser.readthedocs.io/en/latest/

```
pip install -U djoser
pip freeze | grep djoser >> requirements.txt
```



Configure `INSTALLED_APPS`

```python
INSTALLED_APPS = (
    'django.contrib.auth',
    (...),
    'rest_framework',
    'rest_framework.authtoken',  # <-- rode ./manage.py migrate
    'djoser',  # <--
    (...),
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

```

Configure `urls.py`

```python
# djoser
urlpatterns += [
    path('api/v1/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),
]
```


```
python manage.py migrate
python manage.py drf_create_token admin

token d7643a4710c7e19915df7d5e3d82f70cb07998ba  # o seu será um novo
```

Veja no video como rodar no **Postman** e no **Swagger**.

Exemplos com curl

```
# Cria novo usuário
curl -X POST http://127.0.0.1:8000/api/v1/users/ --data 'username=djoser&password=api127rg'

# Login
curl -X POST http://127.0.0.1:8000/api/v1/auth/token/login/ --data 'username=djoser&password=api127rg'

# Informações do usuário
curl -X GET http://127.0.0.1:8000/api/v1/users/me/ -H 'Authorization: Token d7643a4710c7e19915df7d5e3d82f70cb07998ba'  # o seu será um novo

# Logout
curl -X GET http://127.0.0.1:8000/api/v1/auth/token/logout/ -H 'Authorization: Token d7643a4710c7e19915df7d5e3d82f70cb07998ba'  # o seu será um novo
```

Quando faz o logout ele apaga o token, e só gera um novo quando você fizer login novamente.


## Reset de Senha com djoser

### MailHog

Rode o [MailHog](https://github.com/mailhog/MailHog) usando Docker.

`docker run -d -p 1025:1025 -p 8025:8025 mailhog/mailhog`


Endpoints

```
/api/v1/auth/token/login/
/api/v1/users/reset_password/
/api/v1/users/reset_password_confirm/
```

![reset_password](reset_password.png)


Edite `settings.py`

```python
DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', 'webmaster@localhost')
EMAIL_HOST = config('EMAIL_HOST', '0.0.0.0')  # localhost
EMAIL_PORT = config('EMAIL_PORT', 1025, cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, cast=bool)
```

### Página em pt-br

Edite `settings.py`

```python
LANGUAGE_CODE = 'pt-br'
```


### Página com template personalizado

Edite `settings.py`

```python
DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'EMAIL': {
        'password_reset': 'accounts.email.PasswordResetEmail'
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR,
            BASE_DIR.joinpath('templates')
        ],
        ...
    }
]
```

Crie uma nova app

```
python manage.py startapp accounts
rm -f accounts/{admin,models,tests,views}.py
```

Crie um arquivo `email.py`

```python
cat << EOF > accounts/email.py
from djoser import email


class PasswordResetEmail(email.PasswordResetEmail):
    template_name = 'accounts/email/password_reset.html'

EOF
```


Crie o template de e-mail

```
mkdir -p accounts/templates/accounts/email
touch accounts/templates/accounts/email/password_reset.html
```

https://github.com/sunscrapers/djoser/blob/master/djoser/templates/email/password_reset.html

Edite `password_reset.html`

```html
{% block text_body %}
Olá {{ user.first_name }},
...

{% block html_body %}
Olá {{ user.first_name }},
...
```


### Postman

#### Login

POST: http://localhost:8000/api/v1/auth/token/login/

```
{
    "username": "huguinho",
    "password": "d"
}
```

#### Reset

POST: http://localhost:8000/api/v1/users/reset_password/

```
{
    "email": "huguinho@email.com"
}
```

* Não precisa de Token Authorization.


#### Reset Password Confirm

POST: http://localhost:8000/api/v1/users/reset_password_confirm/

```
{
    "uid": "MQ",
    "token": "at61wx-d98ea2d93ae43ba571252177750c4de8",
    "new_password": "my_super_new_password123"
}
```

* Não precisa de Token Authorization.

Se em settings você definir `PASSWORD_RESET_CONFIRM_RETYPE=True` então você precisa passar `re_new_password`.

```
{
    "uid": "MQ",
    "token": "at61wx-d98ea2d93ae43ba571252177750c4de8",
    "new_password": "my_super_new_password123"
    "re_new_password": "my_super_new_password123"
}
```

## Autenticação via JWT com djoser

https://djoser.readthedocs.io/en/latest/jwt_endpoints.html


`pip install djoser djangorestframework-simplejwt`

![jwt.png](jwt.png)


```python
# settings.py
from datetime import timedelta

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # <--
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}


SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("Bearer",),  # na doc está JWT mas pode mudar pra Bearer.
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    # "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}
```

```python
# urls.py
urlpatterns += [
    path('api/v1/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),
    path('api/v1/auth/', include('djoser.urls.jwt')),  # <--
]
```

```python
# views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from product.models import Product
from product.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)  # <--
```

```
curl -X POST http://127.0.0.1:8000/api/v1/auth/token/login/ --data 'username=admin&password=d'

curl -X POST http://127.0.0.1:8000/api/v1/auth/jwt/create/ --data 'username=admin&password=d'
```


Pegar access

```
# atualizar
curl -X POST \
http://127.0.0.1:8000/api/v1/auth/jwt/refresh/ \
-H 'Content-Type: application/json' \
--data '{"refresh": ""}'

curl -X GET \
http://127.0.0.1:8000/product/products/ \
-H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLC...'
```

### Consumindo a API com Python

```python
'''
Usage:

python consumer.py -u usuario -p senha
'''
from pprint import pprint
from typing import Dict

import click
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = 'http://localhost:8000/api/v1/'


def fetch_token(session, endpoint, username, password):
    '''
    Faz autenticação do usuário.
    '''
    # headers = {'Content-type': 'application/json'}  # Não precisou
    data = {
        'username': username,
        'password': password,
    }
    with session.post(
        endpoint,
        auth=HTTPBasicAuth(username, password),
        # headers=headers,  # Não precisou
        data=data
    ) as response:
        return response.json()


def get_token(username: str, password: str) -> Dict[str, str]:
    '''
    Pega o access_token do usuário logado.
    '''
    with requests.Session() as session:
        endpoint = f'{BASE_URL}auth/jwt/create/'
        response = fetch_token(session, endpoint, username, password)
        data = {
            'access_token': response['access'],
        }
        return data


def fetch(session, endpoint, access_token):
    '''
    Faz a autenticação usando JWT.
    '''
    headers = {'Authorization': f'Bearer {access_token}'}
    with session.get(endpoint, headers=headers) as response:
        return response.json()


def post_product(session, endpoint, access_token, title, price):
    '''
    Salva o produto.
    '''
    headers = {'Authorization': f'Bearer {access_token}'}
    data = {
        'title': title,
        'price': price,
    }
    with session.post(endpoint, headers=headers, data=data) as response:
        print(response)
        pprint(response.json())


@click.command()
@click.option('--username', '-u', prompt='username', help='Type the username.')
@click.option('--password', '-p', prompt='password', help='Type the password.')
@click.option('--title', '-t', help='Type the title.')
@click.option('--price', '-pr', help='Type the price.')
def main(username, password, title=None, price=None):
    '''
    Consumindo a lista de produtos.
    '''
    token = get_token(username, password)
    access_token = token['access_token']
    with requests.Session() as session:
        endpoint = 'http://127.0.0.1:8000/product/products/'
        response = fetch(session, endpoint, access_token)
        pprint(response)

        if title and price:
            print(f'Salvando produto: {title}')
            post_product(session, endpoint, access_token, title, price)


if __name__ == '__main__':
    print('Produtos')
    main()

```

## Django CORS headers

https://pt.wikipedia.org/wiki/Cross-origin_resource_sharing

https://github.com/adamchainz/django-cors-headers


```
python -m pip install django-cors-headers
pip freeze | grep django-cors-headers >> requirements.txt
```


Edite `settings.py`

```python
CORS_ALLOWED_ORIGINS = [
    'http://localhost:8080',
]

INSTALLED_APPS = [
    ...,
    'corsheaders',
    ...,
]

MIDDLEWARE = [
    ...,
    # corsheaders
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...,
]

```

```
# Se necessário
python manage.py drf_create_token huguinho
```
