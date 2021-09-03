# drf-example

Django REST framework exemplos e testes.


## Este projeto foi feito com:

* [Python 3.9.6](https://www.python.org/)
* [Django 3.2.6](https://www.djangoproject.com/)
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

token d7643a4710c7e19915df7d5e3d82f70cb07998ba
```




```
curl -X POST http://127.0.0.1:8000/api/v1/users/ --data 'username=djoser&password=api127rg'

curl -X POST http://127.0.0.1:8000/api/v1/auth/token/login/ --data 'username=admin&password=d'

curl -X GET http://127.0.0.1:8000/api/v1/users/me/ -H 'Authorization: Token d7643a4710c7e19915df7d5e3d82f70cb07998ba'
```
