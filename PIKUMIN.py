# -*- coding: utf-8 -*-

import os
import sys
import configparser
from module import csv_process
from module import tpl_process
from module import jinja2_process

# from projects import main_parasheeter as pjpa
# from projects import main_nwccc as pjnw
# from projects import main_nwccc as pjpr

from projects import main_iniinstaller as pjin


# path import
path_of_ini, trashbox = os.path.splitext(__file__)
path_of_ini = path_of_ini + '.ini'

# install INI
dict_of_ini = pjin.starter(path_of_ini)
print(dict_of_ini['projects'])

# check PROJECTS
if dict_of_ini:
    if str.title(dict_of_ini['projects']['nwccc']) == 'True':
        pjnw.starter(dict_of_ini)

    if str.title(dict_of_ini['projects']['parasheeter']) == 'True':
        pjpa.starter(dict_of_ini)

    if str.title(dict_of_ini['projects']['processer']) == 'True':
        pjpr.starter(dict_of_ini)

    else:
        exit()

# path import
tpl_path = os.path.abspath(tpl_folder)
csv_path = os.path.abspath(os.path.join(csv_folder, csv_file))
ps_path = os.path.abspath(os.path.join(ps_folder, ps_file))


# strings import
tpl_csv_index = 'tpl'
config_csv_index = 'config'
# argv import
dev_csv_index = sys.argv[1]


class CreateConfig:
    # ini import
    ini = configparser.ConfigParser()
    inifile.read('./PIKUMIN.ini', 'UTF-8')

    print(inifile.get('csv_folder', 'csv_file'))


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

    #create configuration files for jinja2
    jinja2_process.create_template(text_of_tpl, tpl_path, dev_csv_index)
    j2_temp = jinja2_process.j2_render(text_of_tpl, cfg_dict)
    jinja2_process.create_file(j2_temp, tpl_path, dev_csv_index)

CreateConfig()



