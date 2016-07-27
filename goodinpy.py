# coding:utf-8

#RechargeDate=2016/6/20|RechargeAmout=100|RechargeUser=admin example string.

s = 'RechargeDate=2016/6/20|RechargeAmout=100|RechargeUser=admin'
scores = {}

items = s.split('|')

for item in items:
    it = item.split('=')
    scores[it[0]] = it[1]

def getvaluebykey(searchKey):

    for key in scores:
        if searchKey == key:
            return scores[key]

print getvaluebykey('RechargeDate')
