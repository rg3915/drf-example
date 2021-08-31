# drf-example

Django REST framework exemplos e testes.


## Este projeto foi feito com:

* [Python 3.9.6](https://www.python.org/)
* [Django 3.2.6](https://www.djangoproject.com/)
* [Django Rest Framework 3.11.1](https://www.django-rest-framework.org/)

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
python manage.py migrate
python manage.py createsuperuser --username="admin" --email=""
```

## dr-scaffold

https://github.com/Abdenasser/dr_scaffold

https://www.abdenasser.com/scaffold-django-apis


dr-scaffold é uma lib para criar models e uma API simples em Django REST framework.


### Experimentando e criando um projeto do zero

```
python -m venv .venv
source .venv/bin/activate
pip install dr-scaffold djangorestframework
```

Crie um novo projeto.

```
django-admin startproject backend .
```

Edite `settings.py`

```python
# settings.py
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

```
python manage.py makemigrations
python manage.py migrate
```


