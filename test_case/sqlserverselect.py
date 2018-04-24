from public import sqlserver
from public import Config

delquery = '''

select * from [dbo].[Nb_File]

'''

ss = sqlserver.SqlServer(**Config.mssql_conn_dic)
data = ss.ExecQuery(delquery)
for item in data:
    print (data)

