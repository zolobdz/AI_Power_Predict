# -*- coding: utf-8 -*-

'''获取节假日API
请求方式：地址+?d=20110501
返回:0:工作日，1:休息日 2:假日'''
HOLIDAY_API = 'http://tool.bitefu.net/jiari/'

'''获取天气页面，爬虫方法见download_weather.py
说明: yangzhong表示扬中市
请求对应月份: http://lishi.tianqi.com/yangzhong/201001
'''
WEATHER_API = 'http://lishi.tianqi.com/yangzhong/'