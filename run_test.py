import unittest
import time
import os
import sys
from public import mail
from HTMLTestRunner import HTMLTestRunner


sys.path.append('./test_case')
sys.path.append('./public')


def report(test_report):  # 查找最新的测试报告
    lists = os.listdir(test_report)  # 返回指定的文件夹包含的文件或者文件夹的名字的列表
    lists.sort(key=lambda fn: os.path.getatime(test_report + "\\" + fn))  # 通过sort()方法重新按照时间对目录下的文件进行排序
    report_name = lists[-1]
    return "\\report\\" + report_name


if __name__ == "__main__":
    # test_data.init_data()#初始化接口测试数据
    # 指定测试用例为当前文件夹下的test_case目录
    # 自动化识别需要运行的测试用例
    test_dir = './test_case'
    main_dir = os.getcwd()
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*test.py')
    now = time.strftime("%Y-%m-%d %H_%M_%S")  # 定义当前的时间戳
    filename = './report/' + now + '_result.html'  # 定义文件名
    fp = open(filename, 'wb')
    # 调用HTML报告
    runner = HTMLTestRunner(
        stream=fp,
        title='Interface Test Report',
        description='The results are following:'
    )
    runner.run(discover)
    fp.close()
    test_reports = main_dir + '\\report\\'  # 定义报告文件目录
    rep = main_dir + report(test_reports)
    mail.send_email(rep)
