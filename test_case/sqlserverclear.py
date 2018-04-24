from public import sqlserver
from public import Config

delquery = '''


DELETE FROM [dbo].[Nb_File]
DELETE FROM [dbo].[Nb_FileBaseRelation]
DELETE FROM [dbo].[Nb_ImageExtension]
DELETE FROM [dbo].[Nb_ImageFile]
DELETE FROM [dbo].[Nb_AudioFile]
DELETE FROM [dbo].[Nb_DocumentFile]
DELETE FROM [dbo].[Nb_VideoFile]
DELETE FROM [dbo].[Nb_FileReference]
DELETE FROM [dbo].[Nb_FileProcessState]

'''
ss = sqlserver.SqlServer(**Config.mssql_conn_dic)
ss.ExecNonQuery(delquery)


