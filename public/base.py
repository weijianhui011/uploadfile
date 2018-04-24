from public import Config
from public import read_excel

import hashlib




def requesturl(endpoint):
        host = Config.hosturl()
        url = ''.join([host,endpoint])
        return(url)
'''
def get_response(url,Method,**DataALL):
    if Method == 'get':
        resp = HttpService.MyHTTP(url).get(url,**DataALL)
    if Method == 'post':
        resp = HttpService.MyHTTP(url).post(url, **DataALL)
    return (resp)
'''
def getfilemd5(filename):
    f = open(filename, 'rb')
    f_md5 = hashlib.md5()
    f_md5.update(f.read())
    return(f_md5.hexdigest())

def get_data(testfile,sheetname):
    datainfo=read_excel.XLDateinof(r'F:\unitest\fileupload\test_data\%s'%testfile)
    Data = datainfo.get_sheetinfo_by_name(sheetname)
    return Data




