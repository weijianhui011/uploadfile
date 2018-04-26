from public import Config
from public import read_excel
from public import sqlserver
import os
from public import HttpService


import hashlib




def requesturl(endpoint):
        host = Config.hosturl()
        url = ''.join([host,endpoint])
        return(url)

def fileupload_url():
    host = Config.hosturl()
    url = ''.join([host,'/nbfile/upload'])
    return url

def filefetch_url():
    host = Config.hosturl()
    url = ''.join([host,'/nbfile/Fetch'])
    return url
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
    datainfo=read_excel.XLDateinof(r'..\\test_data\%s'%testfile)
    Data = datainfo.get_sheetinfo_by_name(sheetname)
    return Data

def md5fromsql(file_id):
    delquery = "SELECT [Md5] FROM [NbFileManagement].[dbo].[Nb_File] where [id] = '%s'"%file_id
    ssmd = sqlserver.SqlServer(**Config.mssql_conn_dic)
    datamd = ssmd.ExecQuery(delquery)
    return datamd

def getfile_id(url,filefortest1):
    os.chdir(Config.uploadpath())
    print(os.getcwd)
    filenameinfolder = filefortest1

    md5code = getfilemd5(filenameinfolder)
    headers = {'nb-file-md5': md5code}
    files = {'field1': (filenameinfolder, open(filenameinfolder, 'rb'))}
    DataAll = {'headers': headers, 'files': files}

    r = HttpService.MyHTTP(url).post(url, **DataAll)
    file_id = r.get('Data')
    return file_id


def filelistindir(path):
    g = os.walk(path)
    for name in g:
        return (name[-1])

path1 = r'..\test_case\upload\audio'
print(filelistindir(path1))

# if __name__=="__main__":
#     url= 'http://192.168.1.101:9999/nbfile/upload'
#     filefortest1 = '1.aac'
#     print(getfile_id(url,filefortest1))
#     print(filefetch_url())

if __name__=="__main__":
    print(path1)


