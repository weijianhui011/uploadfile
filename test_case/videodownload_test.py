

import unittest
from public import HttpService
from public import base
from public import Config
from ddt import ddt,data,unpack

'''
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
'''

@ddt #装饰器在使用前需要将ddt给类使用，!!如果引入的ddt，需要@ddt.ddt
class PostParams(unittest.TestCase):

    def setUp(self):
        #endpoint = '/nbfile/Fetch'
        #self.url = base.requesturl(endpoint)
        #print(self.url)
        self.url1 = base.file_fetch_url()
        print(base.file_fetch_url())
        print(self.url1)

    @data(['1.asf'], ['1.avi'], ['1.flv'], ['1.mkv'], ['1.mov'], ['1.mp4'], ['1.rmvb'], ['1.vob'], ['1.wmv'])
    @unpack
    def test_video_download(self, filefortest1):
        file_id = base.get_file_id(base.file_upload_url(),filefortest1 )
        print('CCCCCCCCCCCCCCCCCCC')
        print(file_id)

        params = { 'id': file_id,'format':'mp4'}
        DataAll1 = {'params': params}
        r1 = HttpService.MyHTTP(self.url1).nojsonget(self.url1, **DataAll1)
        date1 =r1.headers
        print(date1['Content-Disposition'])
        r1_content=date1['Content-Disposition']
        bool_endwith1 = r1_content.endswith('.mp4')
        print(bool_endwith1)


        params = { 'id': file_id,'format':'thumbnail'}
        DataAll2 = {'params': params}
        r1 = HttpService.MyHTTP(self.url1).nojsonget(self.url1, **DataAll2)
        date1 =r1.headers
        print(date1['Content-Disposition'])
        r1_content=date1['Content-Disposition']
        bool_endwith2=r1_content.endswith('.jpg')
        print(bool_endwith2)

        self.assertEqual(bool_endwith1, True)
        self.assertEqual(bool_endwith2, True)

        def tearDown(self):
            print('Test Over')

    if __name__ == '__main__':
        unittest.main()



'''
url = ''.join([host,endpoint])
url1= 'http://192.168.1.101:9999/nbfile/Fetch?id=5fbadac4-3d4a-43fc-a7b2-05deccf9afcd&width=150&height=150&format=thumbnail&ResizeMode=Max'
response = requests.get(url1, stream=True)
print(response.content)
dir(response)
'''
'''
  def test_post_params(self,filefortest1):



         self.assertEqual(connect,True)
         self.assertEqual(msg,"上传成功")
         self.assertEqual(md5code, md5Indb)
'''






