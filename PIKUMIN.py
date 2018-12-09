# -*- coding: utf-8 -*-


import os
import sys
sys.path.append('./module')
import csv_process

# argv check
if len(sys.argv) == 2:
    print("...引数入力OK")
    print("..." + __file__ + " " + sys.argv[1])
else:
    print("引数入力NG")
    print("example: python sample.py device_name")
    exit()

# path import
csv_folder = './tpls'
csv_file = 'sample.csv'
csv_path = os.path.abspath(os.path.join(csv_folder, csv_file))
tpl_path = os.path.abspath(csv_folder)

# strings import
tpl_csv_index = 'tpl'
config_csv_index = 'config'
# argv import
dev_csv_index = sys.argv[1]

# path check
if not os.path.exists(csv_path):
    print('not found...CSV FILE:' + csv_path)
    exit()
elif not os.path.exists(tpl_path):
    print('not found...TPL FOLDER:' + tpl_path)
    exit()

csv_process.check_of_index(csv_path, tpl_csv_index)
csv_process.check_of_index(csv_path, config_csv_index)
csv_process.check_of_index(csv_path, dev_csv_index)

tpl_list = csv_process.list_of_index(csv_path, tpl_csv_index)
cfg_dict = csv_process.dict_of_indexs(csv_path, config_csv_index, dev_csv_index)
# dev_dict = csv_process.dict_device(csv_path, dev_csv_index)



print(tpl_list)
print(cfg_dict)
