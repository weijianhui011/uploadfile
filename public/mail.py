import sys
import smtplib
from email.mime.multipart import MIMEMultipart  # 定义附件
from email.mime.text import MIMEText  # 定义文件正文
from email.header import Header  # 定义正文
from public import Config
sys.path.append('./test_case')
sys.path.append('./public')


# 设置smtplib所需的参数
# 下面的发件人，收件人是用于邮件传输的。
def send_email(filename):
    mail_host = 'smtp.mxhichina.com'
    mail_user = 'nbservice@zqnb.com.cn'
    mail_pass = 'Zqnb12345'
    sender = 'nbservice@zqnb.com.cn'  # 发送邮箱名
    receivers = Config.email_address
    message = MIMEMultipart('related')
    f = open(filename, 'rb')
    mail_body = f.read()
    att = MIMEText(mail_body, 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment;filename="report.html"'
    message.attach(att)
    f.close()
    msg = MIMEText(mail_body, 'html', 'utf-8')
    message.attach(msg)
    message['From'] = sender
    message['To'] = ','.join(receivers)
    message['Subject'] = Header('接口自动化测试报告', 'utf-8')
    smtp = smtplib.SMTP()
    smtp.connect(mail_host)
    smtp.login(mail_user, mail_pass)
    smtp.sendmail(message['From'], message['To'], message.as_string())
    smtp.quit()
    print('test report has send out!')

