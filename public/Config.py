import os

def hosturl():
    host = 'http://192.168.1.101:9999/'
    return(host)

def uploadpath():
    uploadpath= os.getcwd() + '\\upload'
    return(uploadpath)

mssql_conn_dic={
    'host':"192.168.1.101",
    'user':"sa",
    'pwd':"zqnb_123",
    'db':"NbFileManagement"

}

sql_conn_dict={
    'host':'192.168.1.56',
    'port':3306,
    'user':'root',
    'passwd':'123456',
    'db':'abc',
    'charset':'utf8'

}
