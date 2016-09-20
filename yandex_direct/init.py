import requests
from flask import request

API_URL = 'https://api.direct.yandex.com/json/v5/'


def call_api(service, method, params, login=None, token=None, locale='ru'):
    login = login or request.args.get('login', 'sidor-qw')
    token = token or request.args['token']

    url = API_URL + service
    headers = {
        'Accept-Language': locale,
        'Client-Login': login,
        'Authorization': 'Bearer %s' % token,
    }
    data = {
        'method': method,
        'params': params,
    }
    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    if response.ok and 'result' in result:
        if method == 'get':
            return result['result'][service[0].upper() + service[1:]]
        elif method == 'add':
            return result['result']['AddResults']
        elif method == 'set':
            return result['result']['SetResults']
    elif 'error' in result:
        raise Exception(result['error'])
    elif 'warning' in result:
        raise Exception(result['warning'])
    return response


