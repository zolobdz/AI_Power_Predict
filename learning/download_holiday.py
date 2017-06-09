# -*- coding: utf-8 -*-
import setting
import os, urllib.request, pickle
from utils.path import data_path
from utils.path import helper_path
from utils.tool import data_trans

class HolidayFactory(object):
    def __init__(self):
        self.date_path = os.path.join(helper_path, 'holiday')
        with open(self.date_path, 'rb') as db_file:
            self.db = pickle.load(db_file)
            
    def __freshFlag(self, datetime_obj):
        url_date = str(datetime_obj.year) + '%02d'%datetime_obj.month + \
                   '%02d'%datetime_obj.day
        print('Download New Holiday Data, Request Date is '+ url_date)
        req = urllib.request.Request(setting.HOLIDAY_API+'?d='+url_date)
        conn = urllib.request.urlopen(req)
        holiday_type = conn.read()
        self.db[url_date] = holiday_type

    def getHolByDate(self, datetime_obj):
        date_str = datetime_obj.strftime('%Y/%m/%d')
        db_key = data_trans(date_str)
        if db_key in self.db:
            return int(self.db.get(db_key, 0))
        self.__freshFlag(datetime_obj)
        with open(self.date_path, 'wb') as db_file:
            db_file.write(pickle.dumps(self.db))
        return int(self.db.get(db_key, 0))

def first_holiday_download():
    '''根据源数据下载日期是否为节假日'''
    date_record = {}
    with open(os.path.join(data_path, 'Tianchi_power.csv'), 'r') as base_data:
        for lines in base_data.readlines()[1:]:
            date_str, _, _ = lines.split(',')
            req_date = data_trans(date_str)
            req = urllib.request.Request(setting.HOLIDAY_API+'?d='+req_date)
            conn = urllib.request.urlopen(req)
            holiday_type = conn.read()
            date_record[req_date] = holiday_type
    with open(os.path.join(helper_path, 'holiday'), 'wb') as database:
        finall_data = pickle.dumps(date_record)
        database.write(finall_data)
        
try:
    Holiday
except NameError:
    Holiday = HolidayFactory()

if __name__ == '__main__':
    first_holiday_download()
