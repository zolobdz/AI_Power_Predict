# -*- coding: utf-8 -*-
import urllib.request
import pickle
import os
from utils.tool import data_trans
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

class WeatherFactory(object):
    def __init__(self):
        self.date_path = os.path.join(helper_path, 'weather')
        self.fresh_flag = False
        with open(self.date_path, 'rb') as db_file:
            self.db = pickle.load(db_file)
            
    def __downloadHtml(self, url_date):
        url = WEATHER_API + url_date + '.html'
        req = urllib.request.Request(url)
        conn = urllib.request.urlopen(req)
        soup = BeautifulSoup(conn.read().decode('gbk'), 'html.parser')
        for tag in soup.find_all('div'):
            if not 'tqtongji2' in tag.get('class', []):
                continue
            for ul_tag in tag.find_all('ul')[1:]:
                yield weatherObj(ul_tag)
                
    def __freshFlag(self, datetime_obj):
        print(datetime_obj.month)
        url_date = str(datetime_obj.year) + '%02d'%datetime_obj.month
        print('Download New Weather Data, Request Date is '+ url_date + str(datetime_obj.day))
        for wea_obj in self.__downloadHtml(url_date):
            repr_date = wea_obj.dump()
            self.db[repr_date['date']] = repr_date
    
    def getWeaByDate(self, datetime_obj):
        date_str = datetime_obj.strftime('%Y/%m/%d')
        db_key = data_trans(date_str)
        if db_key in self.db:
            return self.db.get(db_key, {})
        self.__freshFlag(datetime_obj)
        with open(self.date_path, 'wb') as db_file:
            db_file.write(pickle.dumps(self.db))
        return self.db.get(db_key, {})
    
try:
    Weather
except NameError:
    Weather = WeatherFactory() 
