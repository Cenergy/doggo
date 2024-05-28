from django.db import connection
from django.test.client import Client


import os, sys,time,datetime,requests

from doggo.settings import MEDIA_ROOT,STATIC_ROOT
 
# 打开文件
path = MEDIA_ROOT+"/recognition/images/"
dirs = os.listdir(path)
# 创建一个测试客户端实例
client = Client()
 
# 输出所有文件和文件夹
aDayTicks = 60*60*24*1000

def delRegImage():
    for file in dirs:
        f=path+file
        mtime = time.ctime(os.path.getmtime(f))
        a=datetime.datetime.strptime(mtime, "%a %b %d %H:%M:%S %Y")
        b=datetime.datetime.now()
        subDays=(b-a).days
        
        if subDays>1:
            os.remove(f)

def getGalleryCache():
    response = client.get('/resources/galleryCache/', {'key': 'value'})

def getGithub():
    response = client.get('/api/github/cenergy', {'key': 'value'})