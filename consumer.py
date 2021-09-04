from typing import Dict
from pprint import pprint

import requests
from requests.auth import HTTPBasicAuth

BASE_URL = 'http://localhost:8000/api/v1/'


def fetch_token(session, endpoint):
    '''
    Faz autenticação do usuário.
    '''
    username = 'admin'  # TODO
    password = 'd'  # TODO
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


def get_token() -> Dict[str, str]:
    '''
    Pega o access_token do usuário logado.
    '''
    with requests.Session() as session:
        endpoint = f'{BASE_URL}auth/jwt/create/'
        response = fetch_token(session, endpoint)
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


def main(token):
    '''
    Consumindo a lista de produtos.
    '''
    access_token = token['access_token']
    with requests.Session() as session:
        endpoint = f'http://127.0.0.1:8000/product/products/'
        response = fetch(session, endpoint, access_token)
        return response


if __name__ == '__main__':
    token = get_token()
    result = main(token)
    print('Produtos')
    pprint(result)
