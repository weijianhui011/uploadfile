
import unittest
import os
from public import base
import requests

class PostParams(unittest.TestCase):

    def setUp(self):
        endpoint = '/nbfile/upload'
        self.url = base.request_url(endpoint)

    def test_post_params(self):
        #上传一个文件判断是否上传成功
         os.chdir('..\\test_case\\upload')
         print(os.getcwd)
         files = {'field1': ("1.txt", open('1.txt', 'rb'))}
         DataAll = {'files':files}
         Method = 'postfile'
         r = base.get_response(self.url,Method,**DataAll,)
         print(r)
         connect = r.get('Success')
         msg = r.get("Message")
         fileid = r.get('Data')



         print(connect)
         self.assertEqual(connect,True)
         self.assertEqual(msg,"上传成功")



    @unittest.skip('无条件跳过')
    def test_post_params2(self):
            os.chdir('..\\test_case\\upload')
            files = {'field1': ("1.txt", open('1.txt', 'rb'))}
            r = requests.post(self.url, files=files)
            print(r.text)
            resp = r.json()
            connect = resp.get('Success')
            msg = resp.get("Message")
            print(connect)
            self.assertTrue(connect)


    def tearDown(self):
        print('Test Over')


if __name__ == '__main__':
    unittest.main()




