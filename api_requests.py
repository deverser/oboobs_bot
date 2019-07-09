import requests


URL = 'http://api.oboobs.ru/'
BOOBS_COUNT = 'boobs/count'
NOISE_COUNT = 'noise/count'
MEDIA = 'media.oboobs.ru/'

def get_response(request):
    r = requests.get(URL + request)
    # print("Status code: ", r.status_code)
    return r


def get_boobs_dict(response):
    response_dict = response.json()
    return response_dict[0]
    

def get_boobs_url():
    """Получает URL-адрес самого свежего фото сисек с oboobs.ru"""
    boobs = get_response('boobs/')
    boobs_data = get_boobs_dict(boobs)
    return MEDIA + boobs_data['preview']


if __name__ == "__main__":
    bc = get_response('boobs/')
    boobs_data = get_boobs_dict(bc)
    print(get_boobs_url())