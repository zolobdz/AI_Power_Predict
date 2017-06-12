# -*- coding: utf-8 -*-
import os
import setting
import urllib.request
from datetime import datetime, timedelta
from download_holiday import Holiday
from download_weather import Weather
from utils.path import data_path
from utils.path import bridge_path
from utils.tool import data_trans
            
def __getWeatherType(weather_str):
    if '雪' in weather_str:
        return 0
    if '雨' in weather_str:
        return 1
    return 2

def org_data_to_csv():
    all_lines = ['date_offset,week_day,holiday_type,high_temp,low_temp,weather_type,user_id,cost_el\n']
    user_lines = ['date_offset,week_day,holiday_type,high_temp,low_temp,weather_type,user_id,cost_el\n']
    with open(os.path.join(data_path, 'Tianchi_power.csv'), 'r') as base_file:
        for lines in base_file.readlines()[1:]:
            date_str, user_id, cost_el = lines.split(',')
            db_key, date_obj = data_trans(date_str), datetime.strptime(date_str, '%Y/%m/%d') 
            holiday_type = Holiday.getHolByDate(date_obj)
            weather_detial = Weather.getWeaByDate(date_obj)
            if (holiday_type is None) or (weather_detial is None):
                raise Exception('辅助数据库数据缺失，请补全数据后再重新生成文件，缺失日期:', db_key)
            base_date = datetime(year=date_obj.year, month=1, day=1)
            date_offset = int((date_obj - base_date).days)
            week_day = int(date_obj.weekday()) + 1
            high_temp = float(weather_detial['high'])
            low_temp = float(weather_detial['low'])
            weather_type = __getWeatherType(weather_detial['weather'])
            full_line = [date_offset, week_day, int(holiday_type), high_temp,low_temp,weather_type,user_id, cost_el]
            if int(user_id) == 1:
                user_lines.append(','.join(map(lambda x: str(x), full_line)))
            all_lines.append(','.join(map(lambda x: str(x), full_line)))
    with open(os.path.join(bridge_path, 'all.csv'), 'w') as f_one:
        f_one.writelines(all_lines)
    with open(os.path.join(bridge_path, 'user_one.csv'), 'w') as f_two:
        f_two.writelines(user_lines)


def ninth_month_csv():
    finish_date = datetime(year=2016, month=10, day=1)
    start_date = datetime(year=2016, month=9, day=1)
    base_date = datetime(year=2016, month=1, day=1)
    all_lines = ['date_offset,week_day,holiday_type,user_id\n']
    for time_delta in range((finish_date - start_date).days):
        current_day = start_date + timedelta(days=time_delta)
        req_day = current_day.strftime('%Y%m%d')
        req = urllib.request.Request(setting.HOLIDAY_API + '?d=' + req_day)
        conn = urllib.request.urlopen(req)
        holiday_type = int(conn.read())

        date_offset = int((current_day - base_date).days)
        week_day = int(current_day.weekday()) + 1

        current_line = [date_offset, week_day, holiday_type, '1\n']

        all_lines.append(','.join(map(lambda x: str(x), current_line)))
    with open(os.path.join(bridge_path, 'future.csv'), 'w') as new_f:
        new_f.writelines(all_lines)


def tenth_month_csv():
    finish_date = datetime(year=2016, month=11, day=1)
    start_date = datetime(year=2016, month=10, day=1)
    base_date = datetime(year=2016, month=1, day=1)
    all_lines = ['date_offset,week_day,holiday_type,user_id\n']
    for time_delta in range((finish_date - start_date).days):
        current_day = start_date + timedelta(days=time_delta)
        req_day = current_day.strftime('%Y%m%d')
        req = urllib.request.Request(setting.HOLIDAY_API + '?d=' + req_day)
        conn = urllib.request.urlopen(req)
        holiday_type = int(conn.read())

        date_offset = int((current_day - base_date).days)
        week_day = int(current_day.weekday()) + 1

        current_line = [date_offset, week_day, holiday_type, '1\n']

        all_lines.append(','.join(map(lambda x: str(x), current_line)))
    with open(os.path.join(bridge_path, 'future1.csv'), 'w') as new_f:
        new_f.writelines(all_lines)

if __name__ == '__main__':
    org_data_to_csv()
