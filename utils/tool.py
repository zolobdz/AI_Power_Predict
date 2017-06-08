# -*- coding: utf-8 -*-

def data_trans(data_str):
    '''将2010/01/01
    格式转换为：20100101'''
    new_str = ''
    for temp_str in data_str.split('/'):
        if len(temp_str) == 1:
            temp_str = '0%s'%temp_str
        new_str += temp_str
    return new_str