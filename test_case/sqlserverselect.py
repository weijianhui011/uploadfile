from public import sqlserver
from public import Config

delquery = '''

select * from [dbo].[Nb_File]

'''

ss = sqlserver.SqlServer(**Config.mssql_conn_dic)
data = ss.ExecQuery(delquery)
for item in data:
    print (data)




'''
    for i in len(row[0]):
        if row[0][i]==id:
            print(row[9][i])
'''
#aa = datamd[Md5]
#print(aa)
    #md5insql= datamd[Md5]
