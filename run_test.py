import unittest
import time
import os
import sys
import smtplib
sys.path.append('./test_case')
sys.path.append('./public')
from HTMLTestRunner import HTMLTestRunner
from email.mime.multipart import MIMEMultipart#定义附件
from email.mime.text import MIMEText #定义文件正文
from email.header import Header #定义正文


#设置smtplib所需的参数
#下面的发件人，收件人是用于邮件传输的。
def send_email(file_name):
    mail_host='smtp.mxhichina.com'
    mail_user= 'nbservice@zqnb.com.cn'
    mail_pass = 'Zqnb12345'

    sender= 'nbservice@zqnb.com.cn'   #发送邮箱名
    receivers = ['wh_2002_cn@163.com','1069942031@qq.com','3533437133@qq.com'] #收件人

    message = MIMEMultipart('related')

    f = open(filename,'rb')
    mail_body=f.read()
    att= MIMEText(mail_body,'base64','utf-8')
    att['Content-Type']='applicatioin/octet-stream'
    att["Content-Disposition"]='attachment;filename="report.html"'
    message.attach(att)
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    #msg = MIMEText(mail_body,"html",'utf-8')
    message.attach(msg)
    message['From']=sender
    message['To']=','.join(receivers)
    message['Subject']=Header('接口自动化测试报告','utf-8')
    smtp = smtplib.SMTP()
    smtp.connect(mail_host)
    smtp.login(mail_user,mail_pass)
    smtp.sendmail(message['From'],message['To'],message.as_string())
    smtp.quit()
    print('test report has send out!')


def report(testreport):#查找最新的测试报告
    lists = os.listdir(testreport)#返回指定的文件夹包含的文件或者文件夹的名字的列表
    lists.sort(key = lambda fn: os.path.getatime(testreport + "\\" + fn))#通过sort()方法重新按照时间对目录下的文件进行排序
    #filename= os.path.join(testreport,lists[-1]) #list[-1]取最新生成的文件或者文件夹
    filename =  lists[-1]
    print(filename)
    return filename





if __name__=="__main__":
    #test_data.init_data()#初始化接口测试数据
    #指定测试用例为当前文件夹下的test_case目录
    #自动化识别需要运行的测试用例
    test_dir = './test_case'
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='*performancedownload_test.py')

    now = time.strftime("%Y-%m-%d %H_%M_%S")#定义当前的时间戳
    filename = './report/'+now+'_result.html'#定义文件名
    fp = open(filename,'wb')
    #调用HTML报告
    runner = HTMLTestRunner(
                            stream = fp,
                            title = 'Interface Test Report',
                            description = 'The results are following:'
                            )
    runner.run(discover)
    fp.close()

    os.chdir('F:\\unitest\\fileupload')
    print(os.getcwd)
    test_report= './report'#定义报告文件目录
    rep = report(test_report)
    print('########')
    print(rep)
    send_email(rep)
