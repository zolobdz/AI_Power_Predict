# -*- coding: utf-8 -*-
import setting
import os, urllib.request, pickle
from utils.path import data_path
from utils.path import helper_path
from utils.tool import data_trans

def holiday_download():
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
    with open(os.path.join(helper_path, 'weather'), 'wb') as database:
        finall_data = pickle.dumps(date_record)
        database.write(finall_data)
        
if __name__ == '__main__':
    holiday_download()