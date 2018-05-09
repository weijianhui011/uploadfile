import unittest
import os
from public import HttpService
from public import base
from public import Config
from ddt import ddt, data, unpack

'''读取测试Excel数据'''
testcasefile = 'file_upload_data.xlsx'
AllData = base.get_data(testcasefile,'AllData')
TestData=base.get_data(testcasefile,'TestData')[1:]
print(TestData)

@ddt  # 装饰器在使用前需要将ddt给类使用，!!如果引入的ddt，需要@ddt.ddt
class PostParams(unittest.TestCase):
    def setUp(self):
        self.endpoint = AllData[1][1]
        self.RequestMethod = AllData[1][2]
        self.RequestData = AllData[1][3]
        self.url = base.request_url(self.endpoint)

    @data (*TestData)
    @unpack
    def test_post_params(self, *TestData):
        #  上传一个文件判断是否上传成功
        os.chdir(Config.upload_path)
        file_name_in_folder = TestData[0]
        md5code = base.get_file_md5(file_name_in_folder)
        headers = { 'nb-file-md5': md5code}
        files = {'field1': (file_name_in_folder, open(file_name_in_folder, 'rb'))}
        data_all = {'headers': headers, 'files': files}
        # Method = self.RequestMethod
        # if self.RequestData !='':
        #     DataAll = eval(self.RequestData)
        #     r = base.get_response(self.url,Method,**DataAll)
        # else:
        #     r = base.get_response(self.url,Method)
        #print('BBBBBBBBBBBBBBBB')
        Method = self.RequestMethod
        r = base.get_response(self.url, Method,**data_all)
        print(r)
        connect = r.get(TestData[1])
        msg = r.get(TestData[3])
        self.assertEqual(connect, TestData[2])
        self.assertEqual(msg, TestData[4])
        files['field1'][1].close()

    def tearDown(self):
        print('Test Over')


if __name__ == '__main__':
    unittest.main()



