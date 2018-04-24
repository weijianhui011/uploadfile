from public import base
import requests
import json


endpoint = 'nbfile/GetOriginalFileAll'
url = base.requesturl(endpoint)
list = []

r = requests.get(url)
json_response = r.content.decode()  # 获取r的文本 就是一个json字符串

    # 将json字符串转换成dic字典对象
dict_json = json.loads(json_response)
for each in dict_json:
    md5_list = each['Md5']
    id_list = each['Id']
    list.append(id_list)

print(list)


