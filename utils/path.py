import os

'''当前路径'''
current_path = __file__
'''项目的根目录'''
father_path = os.path.abspath(os.path.dirname(current_path)+os.path.sep+"..")
'''项目数据目录'''
data_path = os.path.join(father_path, 'datas')
'''辅助数据库'''
helper_path = os.path.join(father_path, 'helper_data')

