import os
import random
from dotenv import load_dotenv
from download_comics import *
from post_vk import *


def main():
    load_dotenv('sensitive_information.env')
    token = os.getenv('access_token')
    id_group = os.getenv('id_group')

    count_comics = requests.get('https://xkcd.com/info.0.json').json()['num']
    xkcd_response = get_response_xkcd(random.randrange(count_comics))

    message = xkcd_response['alt']
    os.makedirs('img', exist_ok=True)
    directory = 'img/comics.jpg'

    download_image(xkcd_response, directory)
    server_upload = upload_photo_on_server(directory, token, id_group)
    img_wall = saved_photo_in_album(server_upload, token, id_group)
    post_comics(img_wall, token, id_group, message)
    os.remove(directory)


if __name__ == '__main__':
    main()
