import requests


def get_response_xkcd(num):
    url = f'https://xkcd.com/{num}/info.0.json'
    response = requests.get(url).json()
    return response


def download_image(response, directory):
    url_img = requests.get(response['img'])
    with open(directory, 'wb') as file:
        file.write(url_img.content)


