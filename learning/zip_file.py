import os
from operator import itemgetter
from utils.path import data_path, bridge_path
from datetime import datetime

def zip_two_origin():
    with open(os.path.join(data_path, 'Tianchi_power.csv'), 'r') as first:
        with open(os.path.join(data_path, 'Tianchi_power(1).csv'), 'r') as second:
            base_line = first.readlines()
            base_line += second.readlines()[1:]
    new_total_line = []
    for line in base_line[1:]:
        a, b, c = line.split(',')
        new_total_line.append([datetime.strptime(a, '%Y/%m/%d'), int(b), c])
    new_total_line = [base_line[0]] + sorted(new_total_line, key=itemgetter(1, 0))
    def __gen():
        for k, i in enumerate(new_total_line):
            if k == 0:
                continue
            yield '{0},{1},{2}'.format(i[0].strftime('%Y/%m/%d'), i[1], i[2])
    with open(os.path.join(bridge_path, 'My_Bichi.csv'), 'w') as new_file:
        new_file.writelines(__gen())
        
if __name__ == '__main__':
    zip_two_origin()