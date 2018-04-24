import xlsxwriter
from datetime import date,datetime

'''创建excel文件'''
workbook = xlsxwriter.Workbook('test.xlsx') #创建文件
worksheet = workbook.add_worksheet('test') #创建sheet，会清空
'''特定单元格写入'''
worksheet.write('A1','软件测试')
worksheet.write(1,0,'王慧写入xlsxwriter')
#写入不同类型的数据
worksheet.write(0,1,32)
#设置样式行属性，列属性
worksheet.set_row(0,40)#设置行属性
worksheet.set_column('A:A',20)#设置列属性
#设置自定义格式
top = workbook.add_format({'border':1,'font_size':13,'bold':True,'align':'center','bg_color':'ccccc'})
worksheet.write('A3','物理物理',top)
worksheet.set_row(3,40,top)#设置行属性
worksheet.set_column('C:C',20,top)#设置列属性

#写入数字和函数
worksheet.write(1,2,35)
worksheet.write(2,2,43)
worksheet.write(3,2,'=sum(C2:C3)')
#写入日期
worksheet.write(0,3,datetime.strptime('2018-04-12','%Y-%m-%d'))
worksheet.write(1,3,datetime.strptime('2018-04-12','%Y-%m-%d'),workbook.add_format({'num_format':'yyyy年mm月dd日'}))

#插入图片
worksheet.insert_image(0,4,'1.jpg')
worksheet.insert_image(0,15,'Chrysanthemum.jpg',{'x_scale':0.2,'y_scale':0.2})
worksheet.insert_image(0,20,'Chrysanthemum.jpg',{'x_scale':0.2,'y_scale':0.2,'url':'https://www.baidu.com'})

#批量写入单元格
worksheet.write_column('A22',[1,2,3,4])#列写入，从A22写起
worksheet.write_row('A27',[1,2,3,4])#列写入，从A22写起

#合并单元格写入
worksheet.merge_range(15,5,21,8,'快乐无界限',top)# 1.开始行，开始列，结束行，结束列

#生成图表（多种方式）
#workbook.add_chart()

#关闭单元格
workbook.close()