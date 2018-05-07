import requests


class MyHTTP(object):
    def __init__(self, url):
        self.url = url

    def get(self, url, **data_all):
        params = data_all.get('params')
        id = data_all.get('id')
        headers = data_all.get('headers')
        files = data_all.get('files')
        resp = requests.get(url, headers=headers, params=params, id=id, files=files)
        text = resp.json()
        return text

    def nojsonget(self, url, **data_all):
        params = data_all.get('params')
        headers = data_all.get('headers')
        files = data_all.get('files')
        resp = requests.get(url, headers=headers, params=params, files=files, timeout=1200)
        return resp

    def post(self, url, **data_all):
        params = data_all.get('params')
        headers = data_all.get('headers')
        files = data_all.get('files')
        try:
            resp = requests.post(url, headers=headers, params=params, files=files, timeout=5)
            text = resp.json()
            return text
        except Exception as e:
            print('POST错误：%s' % e)

