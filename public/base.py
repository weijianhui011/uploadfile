import os
import hashlib
from public import Config
from public import read_excel
from public import sqlserver
from public import HttpService


def request_url(endpoint):
        host = Config.host_url()
        url = ''.join([host, endpoint])
        return url


def file_upload_url():
    host = Config.host_url()
    url = ''.join([host, '/nbfile/upload'])
    return url


def file_fetch_url():
    host = Config.host_url()
    url = ''.join([host, '/nbfile/Fetch'])
    return url


def get_file_md5(filename):
    f = open(filename, 'rb')
    f_md5 = hashlib.md5()
    f_md5.update(f.read())
    f.close()
    return f_md5.hexdigest()


def get_data(testfile, sheet_name):
    data_info = read_excel.XLDateInfo(r'..\test_data\%s' % testfile)
    data = data_info.get_sheet_info_by_name(sheet_name)
    return data


def md5_from_sql(file_id):
    del_query = "SELECT [Md5] FROM [NbFileManagement].[dbo].[Nb_File] where [id] = '%s'" % file_id
    ssmd = sqlserver.SqlServer(**Config.mssql_conn_dic)
    datamd = ssmd.ExecQuery(del_query)
    return datamd


def get_file_id(url, file):
    os.chdir(Config.get_upload_path())
    print(os.getcwd)
    file_name_in_folder = file
    md5code = get_file_md5(file_name_in_folder)
    headers = {'nb-file-md5': md5code}
    files = {'field1': (file_name_in_folder, open(file_name_in_folder, 'rb'))}
    data_all = {'headers': headers, 'files': files}
    r = HttpService.MyHTTP(url).post(url, **data_all)
    file_id = r.get('Data')
    files['field1'][1].close()
    return file_id


def file_list_in_dir(path):
    g = os.walk(path)
    for name in g:
        return name[-1]


if __name__ == "__main__":
    path1 = r'..\test_case\upload\audio'
    print(file_list_in_dir(path1))
    test_url = 'http://192.168.1.101:9999/nbfile/upload'
    file_for_test = '1.aac'
    print(get_file_id(test_url, file_for_test))
    print(file_fetch_url())




