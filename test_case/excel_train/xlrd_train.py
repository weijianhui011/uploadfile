import os
import xlrd
from datetime import date,datetime

newpath = os.chdir('F:\\unitest\\fileupload\\test_case\\excel')
filename = '1.xlsx'
file = os.path.join(os.getcwd(),filename)

'''1打开文件'''
xl = xlrd.open_workbook(file)

'''2获取sheet'''
print(xl.sheet_names())
print(xl.sheets())
print(xl.nsheets)
print(xl.sheet_by_name('目录'))
print(xl.sheet_by_index(1))


'''3获取sheet内的汇总数据'''
table1 = xl.sheet_by_name('目录')
table2 = xl.sheet_by_index(2)
print(table1.name)
print(table2.name)
print(table1.nrows)
print(table1.ncols)

'''4单元格的批量读取'''
print(table2.row_values(0))  #合并单元格，首行显示值，其他为空
print(table2.row(0))
print(table2.row_types(0))

print(table2.col_values(0))
print(table2.col_types(0))

print(table2.row_slice(0))  #type  和 name 都展现出来

'''5特定单元格读取'''
#三种相同结果的表现形式
#值
print(table2.cell(1,2).value)
print(table2.cell_value(1,2))
print(table2.row(1)[2].value)
#类型
print(table2.cell(1,2).ctype)
print(table2.cell_type(1,2))
print(table2.row(1)[2].ctype)

'''6常用技巧'''
#简单定位
print(xlrd.cellname(0,0))
print(xlrd.cellnameabs(0,0))
print(xlrd.colname(30))
#封装成一些常用的方法获取从XX到XX列的取值


def read_excel(table,row,col):
    name = table.cell_value(row,col)
    type = table.cell_type(row,col)
    if type==0:
        name = ''
    elif type ==1:
        name = name
    elif type ==2 and name%1 ==0:
        name = int(name)
    elif type ==3:
        '''
        #转换为日期时间
        date_value = xlrd.xldate.xldate_as_datetime(name,0)
        name=date.value
        '''
        #转换为元祖
        date_value= xlrd.xldate_as_tuple(name,0)
        name = datetime(*date_value).strftime('%Y/%m/%d %H:%M:%S')
    elif type ==4:
        name = True if name ==1 else False
    return (name)



'''#7获取表中不同类型的name'''
print(table1.cell_value(0,0))
print(table1.cell_type(0,0))
print(table1.cell_value(1,0))
print(table1.cell_type(1,0))
print("&&&&&&&&")
print(table2.cell_type(11,1))
print(read_excel(table2,11,1))











