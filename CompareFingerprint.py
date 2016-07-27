# coding=utf-8
#import pymssql
import MySQLdb
import random
from traceback import format_exc
import win32com.client
import sys
import os
import datetime
from ctypes import windll,create_string_buffer

IPAdd="192.168.1.32"#�豸ip��ַ
Port="4370"#�豸�˿ں�
dwMachineNumber="6316155300012"#�豸���к�
dwFingerIndex=0
intervallog = 1
#============================��־�и�===================================
def old_year_and_month(year, month, timedelta_month):
    if month - timedelta_month <= 0:
        timedelta_year = timedelta_month/12 or 1
        old_year = year - timedelta_year
        old_month = timedelta_year * 12 + month - timedelta_month
    else:
        old_year = year
        old_month = month - timedelta_month
    return old_year, old_month
def logcut(log_name): #��־�и�
    #��ȡ��ǰ�����£��鿴logĿ¼���Ƿ��е�ǰ���µ��ļ���
    cur_path = os.getcwd()
    
    log=None
    currentDate=datetime.datetime.now()
    filename="CPlog/%s%s/%s"
    if not os.path.exists("%s/CPlog/%s%s"%(cur_path,currentDate.year,currentDate.month)) and intervallog > 0:
        #=========================ɾ����־==========================================
        year, month = old_year_and_month(currentDate.year, currentDate.month, intervallog)
        old_log_path = "%s/CPlog/%s%s" % (cur_path, year, month)
        if os.path.exists(old_log_path):
            import shutil
            for month in range(1, intervallog+1):
                old_year, old_month = old_year_and_month(currentDate.year, currentDate.month, month)
                old_path = "%s/CPlog/%s%s" % (cur_path, old_year, old_month)
                try:
                    shutil.rmtree(old_path)
                except Exception, e:
                    pass
        #===================================================================
        os.makedirs("%s/CPlog/%s%s"%(cur_path,currentDate.year,currentDate.month))
        log = open(filename%(currentDate.year,currentDate.month,log_name),"a")
    else:
        log = open(filename%(currentDate.year,currentDate.month,log_name),"a")
    return log

try:
    #���ӵ�sql server���ݿ�
    #con=pymssql.connect(host="192.168.1.185",user="zk",password="123",port=1433,database="zkteco185(0506)",charset="utf8")
    #����mysql���ݿ�
    con=MySQLdb.connect(host='192.168.1.133',port=3306,user='root',passwd='zksoft3',db='zkteco133(0428)',)
    #����cursor����
    cur = con.cursor()
    #ִ�в�ѯ
    cur.execute("select pin,Template,FingerID from finger_template")
    #ȡ�ò�ѯ�Ľ��
    datas= cur.fetchall()
    #��������ѡ��n������Ҷ�����Ԫ��
    rows=random.sample(datas,100)
    #print rows
    #���ö�̬��
    dd=win32com.client.Dispatch("zkemkeeper.ZKEM.1")
    #�ж��Ƿ������豸
    conn=dd.Connect_Net('192.168.1.32','4370')
    print "conn==",conn
    if conn:
        for row in rows:
            #���ݿ��д洢����Աָ��ģ��
            sql_template=row[1]
            pin=int(row[0])
            #��ȡ�豸�д洢����Աָ��ģ��       

            dwFingerIndex=row[2] 
            mathpro = windll.LoadLibrary("matchdll.dll")                   
            device_template=dd.GetUserTmpExStr(dwMachineNumber,pin,dwFingerIndex)
            print "sql_template=",sql_template
            print "device_template=",device_template
            if sql_template and device_template[2]:
                #ret=cmp(sql_template,device_template[2])
                sql_template =create_string_buffer(sql_template)
                device_template=create_string_buffer(device_template[2])
                ret=mathpro.process10(sql_template,device_template)
                if ret==1:
                    log = logcut(dwMachineNumber)
                    if log:
                        log.write('��Ա���:%s ���ݿ����豸��ָ��������Ϊ:%s ��ָ��ģ��ƥ��\n'%(pin,row[2]))                            
                else:
                    log = logcut(dwMachineNumber)
                    if log:
                        log.write('��Ա���:%s ���ݿ����豸��ָ��������Ϊ:%s ��ָ��ģ�岻һ��\n'%(pin,row[2])) 
            else:
                log = logcut(dwMachineNumber)
                if log:
                    log.write('���ݿ���豸�в�������Ա���:%s ָ��ģ��\n'%pin)
            log.flush()#�ѻ�����������д��Ӳ��
            log.close()#�ر��ļ�
    else:
        print "�豸δ����"
except:
    info=format_exc()
    print info
