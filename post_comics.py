import requests


def upload_photo_on_server(directory, token, group_id, version='5.131'):
    url = 'https://api.vk.com/method/photos.getWallUploadServer/'

    params = {
        'access_token': token,
        'group_id': group_id,
        'v': version
    }
    response = requests.get(url, params=params)

    with open(directory, 'rb') as comics:
        url_upload = response.json()['response']['upload_url']

        files = {
            'Content-Type': 'multipart/form-data',
            'photo': comics
        }

        params = {
            'access_token': token,
            'v': version
        }

        wall_server = requests.post(url_upload, files=files, params=params).json()
    return wall_server


def saved_photo_in_album(server_upload, token, group_id, version='5.131'):
    link_save_wall = 'https://api.vk.com/method/photos.saveWallPhoto'

    payload = {
        'access_token': token,
        'group_id': group_id,
        'photo': server_upload['photo'],
        'server': server_upload['server'],
        'hash': server_upload['hash'],
        'v': version
    }

    img_wall = requests.post(link_save_wall, params=payload)
    return img_wall.json()['response'][0]


def post_comics(img_wall, token, group_id, message, version='5.131'):
    link_for_upload = 'https://api.vk.com/method/wall.post'

    owner_id = img_wall["owner_id"]
    image_id = img_wall["id"]

    payload_upload = {
        'access_token': token,
        'owner_id': f'-{group_id}',
        'from_group': 1,
        'message': message,
        'attachments': f'photo{owner_id}_{image_id}',
        'v': version,
    }

    requests.post(link_for_upload, params=payload_upload)
