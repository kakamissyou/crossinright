# -*- coding: utf-8 -*-
from ctypes import windll,create_string_buffer
import time
__author__ = 'Administrator'
params = "protocol=TCP,ipaddress=192.168.1.61,port=4370,timeout=4000,passwd=0"
commpro = windll.LoadLibrary("plcommpro.dll")
con_str = create_string_buffer(params)

def pressOkey(handle):
    time.sleep(1)
    items = ("VirtualKey=394")
    p_items = create_string_buffer(items)
    ret = handle.SetDeviceParam(hcommpro, p_items)
    print ret
    time.sleep(1)
    items = ("VirtualKey=138")
    p_items = create_string_buffer(items)
    ret = handle.SetDeviceParam(hcommpro, p_items)
    print ret

def pressNumericOne(handle):
    time.sleep(1)
    items = ("VirtualKey=305")
    p_items = create_string_buffer(items)
    ret = handle.SetDeviceParam(hcommpro, p_items)
    print ret
    time.sleep(1)
    items = ("VirtualKey=49")
    p_items = create_string_buffer(items)
    ret = handle.SetDeviceParam(hcommpro, p_items)
    print ret

hcommpro = commpro.Connect(con_str)
pressNumericOne(commpro)
pressOkey(commpro)
pressNumericOne(commpro)
pressOkey(commpro)