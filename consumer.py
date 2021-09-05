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


def get_token(username, password) -> Dict[str, str]:
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


@click.command()
@click.option('--username', '-u', prompt='username', help='Type the username.')
@click.option('--password', '-p', prompt='password', help='Type the password.')
def main(username, password):
    '''
    Consumindo a lista de produtos.
    '''
    token = get_token(username, password)
    access_token = token['access_token']
    with requests.Session() as session:
        endpoint = f'http://127.0.0.1:8000/product/products/'
        response = fetch(session, endpoint, access_token)
        pprint(response)
        return response


if __name__ == '__main__':
    print('Produtos')
    pprint(main())
