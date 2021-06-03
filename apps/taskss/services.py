from django.db import connection


import os, sys,time

from doggo.settings import MEDIA_ROOT,STATIC_ROOT
 
# 打开文件
path = MEDIA_ROOT+"/reg/"
dirs = os.listdir(path)
 
# 输出所有文件和文件夹
aDayTicks = 60*60*24*1000

def delRegImage():
    for file in dirs:
        f=path+file
        mtime = os.path.getmtime(f)
        ticks = time.time()
        subTime = ticks-mtime
        print(ticks,subTime,subTime>aDayTicks,"-------")

