# -*- coding: utf-8 -*-
import os, urllib.request
import setting, pickle

'''当前路径'''
current_path = os.getcwd()
'''项目的根目录'''
father_path = os.path.abspath(os.path.dirname(current_path)+os.path.sep+".")
'''项目数据目录'''
data_path = os.path.join(father_path, 'datas')
'''辅助数据库'''
helper_path = os.path.join(father_path, 'helper_data')

def data_trans(data_str):
    new_str = ''
    for temp_str in data_str.split('/'):
        if len(temp_str) == 1:
            temp_str = '0%s'%temp_str
        new_str += temp_str
    return new_str

def parse_data(): 
    with open(os.path.join(data_path, 'Tianchi_power.csv')) as base_data:
        return_dict = {}
        date_record = pickle.load(open(os.path.join(helper_path, 'holiday'), 'rb'))
        for lines in base_data.readlines()[1:]:
            date_str, user_id, el_cost = lines.split(',')
            req_date = data_trans(date_str)
            if req_date in date_record:
                holiday_type = date_record[req_date]
            else: 
                req = urllib.request.Request(setting.HOLIDAY_API+'?d='+req_date)
                conn = urllib.request.urlopen(req)
                holiday_type = conn.read()
                date_record[req_date] = holiday_type
            return_dict[user_id] = None

parse_data()
