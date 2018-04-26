

import unittest

from public import HttpService
from public import base

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
        self.url1 = base.filefetch_url()
        print(base.filefetch_url())
        print(self.url1)

    @data(['1.aac'],['1.m4a'],['1.mp3'],['1.wav'])
    @unpack
    def test_video_download(self, filefortest1):
        file_id = base.getfile_id(base.fileupload_url(),filefortest1 )
        print('CCCCCCCCCCCCCCCCCCC')
        print(file_id)

        params = {'id': file_id, 'format': 'mp3'}
        DataAll2 = {'params': params}
        r1 = HttpService.MyHTTP(self.url1).nojsonget(self.url1, **DataAll2)
        date1 = r1.headers
        print(date1['Content-Disposition'])
        r1_content = date1['Content-Disposition']
        bool_endwith2 = r1_content.endswith('.mp3')
        print(bool_endwith2)


        self.assertEqual(bool_endwith2, True)

        def tearDown(self):
            print('Test Over')

    if __name__ == '__main__':
        unittest.main()












