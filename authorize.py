import requests
import os


def main():
    link = 'https://oauth.vk.com/authorize'

    params = {
        'client_id': os.getenv('ID_CLIENT'),
        'redirect_uri': 'https://oauth.vk.com/blank.html',
        'display': 'page',
        'scope': 'photos,wall,offline,groups',
        'response_type': 'token',
    }

    response = requests.get(link, params=params)
    return response.url


if __name__ == '__main__':
    print(main())
