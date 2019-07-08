import requests


URL = 'http://api.oboobs.ru/'
BOOBS_COUNT = 'boobs/count'
NOISE_COUNT = 'noise/count'

def get_response(request):
    r = requests.get(URL + request)
    print("Status code: ", r.status_code)
    return r


def get_boobs_dict(response):
    response_dict = response.json()
    return response_dict[0]


if __name__ == "__main__":
    bc = get_response('boobs/')
    print(get_boobs_dict(bc))


