import requests
import json

URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'

with open('token.txt','r') as f:
    KEY = f.read()


def get_auth_token(key: str, url_auth: str) -> str:
    headers_auth = {'Authorization': 'Basic ' + key}
    auth = requests.post(url=url_auth, headers=headers_auth)
    if auth.status_code == 200:
        cur_token = auth.text
        return cur_token
    else:
        print('Error - ' + str(auth.status_code))
        return ''


def get_a_word_translation(cur_token: str, url_tr: str, word: str) -> str:
    headers_translate = {
        'Authorization': 'Bearer ' + cur_token
    }
    params = {
        'text': word,
        'srcLang': 1033,
        'dstLang': 1049
    }
    req = requests.get(url_tr, headers=headers_translate, params=params)
    if req.status_code == 200:
        res = req.json()
        try:
            value = res['Translation']['Translation']
            return value
        except TypeError:
            if res == 'Incoming request rate exceeded for 50000 chars per day pricing tier':
                print('Error - Incoming request rate exceeded for 50000 chars per day pricing tier')
                return res
            else:
                return 'No translation available'
    else:
        print('Error!' + str(req.status_code))


if __name__ == "__main__":
    token = get_auth_token(key=KEY, url_auth=URL_AUTH)
    not_translated_words_test = ['victim', 'home', 'root']
    for en_word in not_translated_words_test:
        ru_translation = get_a_word_translation(cur_token=token, url_tr=URL_TRANSLATE, word=en_word)
        if ru_translation == 'Incoming request rate exceeded for 50000 chars per day pricing tier':
            break
        print(ru_translation)
