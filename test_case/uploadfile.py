import unittest
import os
from public import HttpService
from public import base
from public import Config
from ddt import ddt, data, unpack


@ddt  # 装饰器在使用前需要将ddt给类使用，!!如果引入的ddt，需要@ddt.ddt
class PostParams(unittest.TestCase):
    def setUp(self):
        endpoint = '/nbfile/upload'
        self.url = base.request_url(endpoint)

    @data (['1.txt'], ['1.pdf'], ['1.jpg'], ['1.xlsx'])
    @unpack
    def test_post_params(self, file_for_test):
        #  上传一个文件判断是否上传成功
        os.chdir(Config.get_upload_path())
        file_name_in_folder = file_for_test
        md5code = base.get_file_md5(file_name_in_folder)
        headers = { 'nb-file-md5': md5code}
        files = {'field1': (file_name_in_folder, open(file_name_in_folder, 'rb'))}
        data_all = {'headers': headers, 'files': files}
        r = HttpService.MyHTTP(self.url).post(self.url, **data_all)
        connect = r.get('Success')
        msg = r.get("Message")
        self.assertEqual(connect, True)
        self.assertEqual(msg, "上传成功")
        files['field1'][1].close()

    def tearDown(self):
        print('Test Over')


if __name__ == '__main__':
    unittest.main()



