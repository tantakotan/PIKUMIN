# -*- coding: utf-8 -*-

import os
import sys
from module import csv_process
from module import tpl_process
from module import jinja2_process

# argv check
if len(sys.argv) == 2:
    print('argv count check...OK: ' + str(len(sys.argv)))
    print('starting...: ' + __file__ + ' ' + sys.argv[1])
else:
    print('argv count check...NG: ')
    print("example: python PIKUMIN.py device_name")
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
csv_process.check_path(csv_path)
csv_process.check_path(tpl_path)

# csv file check
csv_process.check_index(csv_path, tpl_csv_index)
csv_process.check_index(csv_path, config_csv_index)
csv_process.check_index(csv_path, dev_csv_index)

# create template dictionary
tpl_list = csv_process.get_columns(csv_path, tpl_csv_index)
cfg_dict = csv_process.get_dictionary(csv_path, config_csv_index, dev_csv_index)

# create tpl file
tpl_process.check_file(tpl_path, tpl_list)
text_of_tpl = tpl_process.bond_tpl(tpl_path, tpl_list)

# create configuration files for jinja2
jinja2_process.create_template(text_of_tpl, tpl_path, dev_csv_index)
j2_temp = jinja2_process.j2_render(text_of_tpl, cfg_dict)
jinja2_process.create_file(j2_temp, tpl_path, dev_csv_index)
