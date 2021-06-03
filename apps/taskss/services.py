from django.db import connection


import os, sys,time,datetime

from doggo.settings import MEDIA_ROOT,STATIC_ROOT
 
# 打开文件
path = MEDIA_ROOT+"/reg/"
dirs = os.listdir(path)
 
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


