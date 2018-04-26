import requests
import json



class MyHTTP(object):
    def __init__(self,url):
        self.url = url


    def get(self,url,**DataALL):
        params = DataALL.get('params')
        id = DataALL.get('id')
        headers = DataALL.get('headers')
        files = DataALL.get('files')
        resp = requests.get(url,headers=headers,params=params,id = id,files=files)
        text = resp.json()
        return (text)

    def nojsonget(self,url,**DataALL):
        params = DataALL.get('params')

        headers = DataALL.get('headers')
        files = DataALL.get('files')
        resp = requests.get(url,headers=headers,params=params,files=files,timeout=120)
        return (resp)


    def post(self,url,**DataALL):
        params = DataALL.get('params')
        headers = DataALL.get('headers')
        files = DataALL.get('files')
        try:
            resp = requests.post(url,headers=headers,params=params,files=files,timeout=5)
            text = resp.json()
            return (text)
        except Exception as e:
            print('POST错误：%s'%e)

