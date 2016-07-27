# -*- coding: utf-8 -*-
from urllib2 import urlopen,URLError,HTTPError
import smtplib

demoServerList = {
    'zkeco':'http://zkeco.xmzkteco.com/',
    'bioServer':'http://biosecurity.xmzkteco.com/login/images/button1.png'
}

def sendEmailNotification(user,TO,BODY= 'Server Exception,please deal with it first！'):
    HOST = 'smtp.zkteco.com'
    TO = 'kaka.liu@zkteco.com'
    SUBJECT = 'Demo Server exception Alert!'
    BODY = 'Server Exception,please deal with it first！'
    user = 'kaka.liu@zkteco.com'
    pwd = '131015liusr'
    try:
        serverObj = smtplib.SMTP()
        serverObj.connect(HOST)
        serverObj.login(user,pwd)
        serverObj.sendmail(user, TO, BODY)
    except:
        print '发送邮件异常!'
    finally:
        serverObj.quit()

for demoServer in demoServerList:
    try:
        content = urlopen(demoServerList.get(demoServer), timeout=10)
        httpcode = content.getcode()
    except HTTPError,e:
        print u'访问服务器时发现网络异常,请联系管理员!'
    if httpcode!= 200:
        print u'服务异常，请及时处理！'
        restartAppServer('net start ZkecoControlCenterService')
        sendEmailNotification()
    else:
        print u'服务正常'

import os
def restartAppServer(command):
    os.system(command)
