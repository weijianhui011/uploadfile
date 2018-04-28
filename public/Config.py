import sys

email_address = [
    'wh_2002_cn@163.com', '1069942031@qq.com', '3533437133@qq.com', '527159802@qq.com'
]


def host_url():
    host = 'http://192.168.1.101:9999/'
    return host


def get_upload_path():
    upload_path = sys.path[0] + '\\test_case\\upload'
    return upload_path


mssql_conn_dic = {
    'host': "192.168.1.101",
    'user': "sa",
    'pwd': "zqnb_123",
    'db': "NbFileManagement"
}


sql_conn_dict = {
    'host': '192.168.1.56',
    'port': 3306,
    'user': 'root',
    'passwd': '123456',
    'db': 'abc',
    'charset': 'utf8'
}
