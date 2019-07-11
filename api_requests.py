import requests
from random import randint


URL = 'http://api.oboobs.ru/'
BOOBS_COUNT = 'boobs/count'
NOISE_COUNT = 'noise/count'
MEDIA = 'media.oboobs.ru/'


def get_response(request):
    r = requests.get(URL + request)
    response_dict = r.json()
    # print(response_dict)
    # print("Status code: ", r.status_code)
    return response_dict[0]

    
def get_boobs_url():
    """Получает URL-адрес самого свежего фото сисек с oboobs.ru"""
    boobs = get_response('boobs/')
    return MEDIA + boobs['preview']


def get_random_boobs():
    """Получает URL-адрес рандомного фото сисек"""
    boobs = get_response(BOOBS_COUNT)
    count = boobs['count']
    photo_id = str(randint(1, count))
    file_info = get_response('boobs/get/' + photo_id)
    if not file_info:
        get_random_boobs()
    else:
        return MEDIA + file_info['preview']


if __name__ == "__main__":
    rb = get_random_boobs()
    print(rb)