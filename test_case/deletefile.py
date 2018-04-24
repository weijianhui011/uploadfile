import requests
from public import base
endpoint = 'nbfile/Delete'
url = base.requesturl(endpoint)

header = {'content-type':'application/x-www-form-urlencoded; charset=UTF-8'}
list1 = ['e2ceec6f-7d64-49c6-a005-bf646d865482', 'f47a1cb7-dd0b-4f94-bf9d-b1272574230f', '78943d43-836d-429e-915a-ecd7bc6d1ea7', '287c6878-6796-4744-9ee7-f6a4d95be08e', '6f707474-91fa-46cd-b52b-e7665368ab56', '281c6aa4-ed56-480a-bce3-2c3d1152df60', 'd3b10414-9f20-4465-947d-4c16ef4efe90', '9e8ff1a6-97d9-4c19-aca5-b788d588005e', 'b7db7914-11c0-4d84-80c9-f931b95e787a']

for each in list1:
    d={'id': each}
    r = requests.post(url, data = d,headers = header)
    print(r.content)