from public import base
from urllib.error import URLError
import threading
from public import HttpService
import socket
import time
import random



timeout =20
socket.setdefaulttimeout(timeout)#这里对整个socket层设置超时时间。后续文件中如果再使用到socket，不必再设置
sleep_download_time = 0.4
def test_video_download():
    num= random.randint(1,10000)
    headers= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.08 (KHTML, like Gecko) Chrome/%d.0.3359.117 Safari/537.36'%num}
   # headers = {'nb-file-md5': md5code}
    #print(headers)
    file_id ='efef4642-160b-4404-aa94-6f2930773814'
    url1 = 'http://192.168.1.101:9999/nbfile/Fetch'
    params = {'id': file_id, 'format': 'mp4'}
    DataAll1 = {'headers':headers,'params': params}
    r1 = HttpService.MyHTTP(url1).nojsonget(url1, **DataAll1)



    #date1 = r1.headers
    #print(date1['Content-Disposition'])
    #r1_content = date1['Content-Disposition']
    #bool_endwith1 = r1_content.endswith('.mp4')
    #print(bool_endwith1)
    r1.close()

try:
    i = 0
    tasks = []  # 任务列表
    task_number = 1
    while i < task_number:
        time.sleep(sleep_download_time)
        t = threading.Thread(target=test_video_download)
        tasks.append(t)  # 加入线程池，按需使用
        t.start()  # 多线程并发
        i+=1
        #print(i)
except Exception as e:
    print(e)
