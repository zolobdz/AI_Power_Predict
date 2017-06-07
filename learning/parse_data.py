# -*- coding: utf-8 -*-
import os

'''当前路径'''
current_path = os.getcwd()
'''项目的根目录'''
father_path = os.path.abspath(os.path.dirname(current_path)+os.path.sep+".")
'''项目数据目录'''
data_path = os.path.join(father_path, 'datas')

with open(os.path.join(data_path, 'Tianchi_power.csv')) as base_data:
    return_dict = {}
    for lines in base_data.readlines()[1:]:
        date_str, user_id, el_cost = lines.split(',')
        return_dict[user_id] = None
    print(len(return_dict))