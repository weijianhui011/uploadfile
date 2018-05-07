
import unittest
import os
from public import HttpService
from public import base
from public import Config
from ddt import ddt,data,unpack

testcasefile = 'get_params_headers_data.xlsx'
AllData = base.get_data(testcasefile,'AllData')
print(AllData)
TestData = base.get_data(testcasefile,'TestData')
Endpoint = AllData[1][1]
filename=TestData[1][1]
dataall=TestData[1][2]
expectresult=TestData[1][3]
print(AllData,TestData,Endpoint,filename,dataall,expectresult)


@ddt #装饰器在使用前需要将ddt给类使用，!!如果引入的ddt，需要@ddt.ddt
class PostParams(unittest.TestCase):

    def setUp(self):
        endpoint='/nbfile/upload'
        self.url = base.request_url(endpoint)
        print(self.url)
    @data(True,False)
    def test_post_params(self,result):
        #上传一个文件判断是否上传成功
         os.chdir(Config.uploadpath())
         print(os.getcwd)


         md5code = base.getfilemd5('1.pdf')
         headers = { 'nb-file-md5': md5code}
         files = {'field1': ('1.pdf', open('1.pdf', 'rb'))}
         DataAll={'headers':headers, 'files':files }

         r = HttpService.MyHTTP(self.url).post(self.url, **DataAll)
         #roo = requests.post(self.url,headers = headers,files = files)
         #r = roo.json()
         print(r)
         connect = r.get('Success')
         msg = r.get("Message")
         print(connect)
         self.assertEqual(connect,result)
         self.assertEqual(msg,"上传成功")


    def tearDown(self):
        print('Test Over')


if __name__ == '__main__':
    unittest.main()




