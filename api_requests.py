import requests
import json
from random import randint


URL = 'http://api.oboobs.ru/'
BOOBS_COUNT = 'boobs/count'
NOISE_COUNT = 'noise/count'
MEDIA = 'media.oboobs.ru/'
FILENAME = 'data.json'


def get_response(request):
    r = requests.get(URL + request)
    response_dict = r.json()
    print(response_dict)
    # print("Status code: ", r.status_code)
    # print(response_dict[0])
    try:
        return response_dict[0]
    except IndexError:
        print('Error caught... retrying...')
        get_response(request)

    
def get_boobs_url():
    """Получает URL-адрес самого свежего фото сисек с oboobs.ru"""
    boobs = get_response('boobs/')
    return MEDIA + boobs['preview']


def get_random_boobs():
    """Получает URL-адрес рандомного фото сисек"""
    rand_boobs = get_response('boobs/0//random')
    return MEDIA + rand_boobs['preview']


def boobs_content():
    boobs = get_response(BOOBS_COUNT)
    count = boobs['count']
    all_boobs = get_response(URL + 'boobs/0/{}/random'.format(count))
    with open(FILENAME, 'w', encoding='utf-8') as f:
        f.write(all_boobs[0])
    print('Data stored.')



if __name__ == "__main__":
    get_random_boobs()