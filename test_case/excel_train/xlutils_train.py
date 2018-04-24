import xlrd
import xlutils.copy

x1 = xlrd.open_workbook('test.xlsx')
workbook = xlutils.copy.copy(x1)
worksheet = workbook.get_sheet(0) # 复制第一个页签
worksheet.write(0,0,'changed')
workbook.save(r'xlutils_save.xls')#没有支持格式，只支持xls