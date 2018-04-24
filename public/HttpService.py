import requests
import json
from public import base


class MyHTTP(object):
    def __init__(self,url):
        self.url = url


    def get(self,url,**DataALL):
        params = DataALL.get('params')
        headers = DataALL.get('headers')
        files = DataALL.get('files')
        resp = requests.get(url,headers=headers,params=params,files=files)
        text = resp.json()
        return (text)


    def post(self,url,**DataALL):
        params = DataALL.get('params')
        headers = DataALL.get('headers')
        files = DataALL.get('files')
        try:
            resp = requests.post(url,headers=headers,params=params,files=files,timeout=3)
            text = resp.json()
            return (text)
        except Exception as e:
            print('POST错误：%s'%e)

