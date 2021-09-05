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
