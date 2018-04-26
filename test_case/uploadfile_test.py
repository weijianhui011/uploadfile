
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
dataall=TestData[1][2]
expectresult=TestData[1][3]
filelist= base.get_data(testcasefile,'filelist')
filefortest = filelist[1:]
print('@@@@@@@@@@@@')
print(filefortest)


@ddt #装饰器在使用前需要将ddt给类使用，!!如果引入的ddt，需要@ddt.ddt
class PostParams(unittest.TestCase):

    def setUp(self):
        endpoint='/nbfile/upload'
        self.url = base.requesturl(endpoint)
        print(self.url)
    #@data(['1.doc'],['1.docx'])
    @data (['1.doc'],['1.docx'],['1.pdf'],['1.ppt'],['1.txt'],['1.wps'],['1.xlsx'],['1.aac'],['1.m4a'],['1.mp3'],['1.wav'],['1.bmp'],['1.gif'],['1.jpg'],['1.png'],['1.psd'],['1.asf'],['1.avi'],['1.flv'],['1.mkv'],['1.mov'],['1.mp4'],['1.rmvb'],['1.vob'],['1.wmv'],['1.rar'],['1.zip'])
    #['1.ppt'],['1.pdf'],['1.jpg'],['1.gif'],['1.png'],['1.bmp'],['1.psd']
    #['1.doc'],['1.docx'],['1.pdf'],['1.ppt'],['1.txt'],['1.wps'],['1.xlsx'],['1.rar'],['1.zip']
    # ['1.aac'],['1.m4a'],['1.mp3'],['1.wav']
    # ['1.bmp'],['1.gif'],['1.jpg'],['1.png'],['1.psd']
    #['1.asf'],['1.avi'],['1.flv'],['1.mkv'],['1.mov'],['1.mp4'],['1.rmvb'],['1.vob'],['1.wmv']
    @unpack
    def test_post_params(self,filefortest1):
        #上传一个文件判断是否上传成功
         os.chdir(Config.uploadpath())
         print(os.getcwd)
         filenameinfolder = filefortest1

         md5code = base.getfilemd5(filenameinfolder)
         print('!!!!!!!!!!!!')
         print(md5code)
         headers = { 'nb-file-md5': md5code}
         files = {'field1': (filenameinfolder, open(filenameinfolder, 'rb'))}
         DataAll={'headers':headers, 'files':files }

         r = HttpService.MyHTTP(self.url).post(self.url, **DataAll)
         #roo = requests.post(self.url,headers = headers,files = files)
         #r = roo.json()
         print('CCCCCCCCCCCCCCCCC')
         print(r)
         file_id=r.get('Data')
         print(file_id)
         connect = r.get('Success')
         msg = r.get("Message")
         print(connect)

         print('DDDDDDDDDDDDDDDDDDDD')
         md5Indb = base.md5fromsql(str(file_id))[0][0]
         print(md5Indb)

         self.assertEqual(connect,True)
         self.assertEqual(msg,"上传成功")
         self.assertEqual(md5code, md5Indb)


    def tearDown(self):
        print('Test Over')


if __name__ == '__main__':
    unittest.main()




