import webbrowser
import requests
from contextlib import closing
import ctypes
from class1 import ProgressBar
import os
webbrowser.open("https://ys.mihoyo.com/cloud/?utm_source=default#/")
webbrowser.open("https://ys-api.mihoyo.com/event/download_porter/link/ys_cn/official/pc_default")
webbrowser.open("https://ys.mihoyo.com/")
res=requests.get("https://ts1.cn.mm.bing.net/th/id/R-C.49d26daf3f33576e668deae3e3199ca2?rik=X1I1722ccGZEOg&riu=http%3a%2f%2fi1.hdslb.com%2fbfs%2farchive%2f806cecdf0a76b99a816433e307f158dcd0ef227e.png&ehk=PyNIJ42xrBRsehMT1wpajBeQuALJ1tZCbRJYKHNc1fo%3d&risl=&pid=ImgRaw&r=0")
with open("原神.jpg", "wb") as file:
    for datas in res.iter_content(100000):
        file.write(datas)
    file.close()
    
rel_path=os.path.abspath("原神.jpg")
ctypes.windll.user32.SystemParametersInfoW(20, 0,rel_path, 0)

with closing(requests.get("https://autopatchcn.yuanshen.com/client_app/download/launcher/20231026165011_31JrRLv7IPd4QbTX/mihoyo/yuanshen_setup_20231018115430.exe", stream=True)) as response:
    chunk_size = 1024 # 单次请求最大值
    content_size = int(response.headers['content-length']) # 内容体总大小
    progress = ProgressBar("原神.exe", total=content_size,
                                     unit="KB", chunk_size=chunk_size, run_status="正在下载", fin_status="下载完成")
    with open("原神.exe", "wb") as file:
       for data in response.iter_content(chunk_size=chunk_size):
           file.write(data)
           progress.refresh(count=len(data))