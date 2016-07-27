# -*- coding: utf-8 -*-
#两个问题，第一个是城市名称不支持中文，奇怪 ，第二个是urlopen后面竟然不支持read方法
from city import city
import urllib2
import json

cityname = raw_input(u'您想查询哪个城市的天气？\n')
citycode= city.get(cityname)


if citycode:
    url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
    content = urllib2.urlopen(url)
    print content
    print type(content)
    try:
        data = json.load(content)
        print type(data)
        result = data['weatherinfo']
        str_temp = ('%s - %s - %s - %s')%(cityname, result['weather'], result['temp1'], result['temp2'])
        print str_temp
    except:
        print u'查询失败!'
else:
    print(u'城市没找到，请确认!')


