import os
from utils.path import data_path, bridge_path

def zip_two_origin():
    with open(os.path.join(data_path, 'Tianchi_power.csv'), 'r') as first:
        with open(os.path.join(data_path, 'Tianchi_power(1).csv'), 'r') as second:
            base_line = first.readlines()
            base_line += second.readlines()[1:]
    with open(os.path.join(bridge_path, 'My_Bichi.csv'), 'w') as new_file:
        new_file.writelines(base_line)
        
if __name__ == '__main__':
    zip_two_origin()