import time,random

def timeStampRandom(str):
    randomString = time.strftime('%Y%m%d%H%M%S')
    randomString = str+randomString + '%d' %(random.randint(10,100))
    return randomString