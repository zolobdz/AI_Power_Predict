# -*- coding: utf-8 -*-
import urllib.request
import pickle
import os
from setting import WEATHER_API
from utils.path import helper_path
from bs4 import BeautifulSoup

class weatherObj(object):
    attr_slots = ('date', 'high', 'low', 'weather', 'wind_blow', 'wind_stength')
    def __init__(self, tag_obj):
        for attr_name, sorce_data in zip(self.attr_slots, tag_obj.find_all('li')):
            setattr(self, attr_name, str(sorce_data.string))
            
    def dump(self):
        base_date = self.__dict__['date']
        self.__dict__['date'] = ''.join(base_date.split('-'))
        return self.__dict__

def __getWeatherMonth():
    '''取2015年1月到12月，2016年1月到8月的数据'''
    for month in range(1, 13):
        new_month = str(month)
        if len(new_month) == 1:
            new_month = '0'+new_month
        yield '2015{0}.html'.format(new_month)
    for month in range(1, 9):
        yield '20160{0}.html'.format(str(month))

def weather_download():
    date_dict = {}
    for url_month in __getWeatherMonth():
        url = WEATHER_API + url_month
        req = urllib.request.Request(url)
        conn = urllib.request.urlopen(req)
        html = conn.read().decode('gbk')
        soup = BeautifulSoup(html, 'html.parser')
        for tag in soup.find_all('div'):
            if not 'tqtongji2' in tag.get('class', []):
                continue
            for ul_tag in tag.find_all('ul')[1:]:
                obj = weatherObj(ul_tag).dump()
                date_dict[obj['date']] = obj
    my_file = open(os.path.join(helper_path, 'weather'), 'wb')
    my_file.write(pickle.dumps(date_dict))
    my_file.close()

if __name__ == '__main__':
    weather_download()
    