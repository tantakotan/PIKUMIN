# -*- coding: utf-8 -*-

import os
from projects.csvinstaller import csv_process
from distutils.util import strtobool


def starter_nw(dict_of_ini):

    path_of_csv = os.path.join(dict_of_ini['csv']['csv_folder'], dict_of_ini['csv']['csv_file'])
    path_of_tpl = os.path.join(dict_of_ini['tpl']['tpl_folder'])
    index_of_tpl = dict_of_ini['tpl']['tpl_index']
    index_of_nw = dict_of_ini['nw']['nw_index']
    index_of_conf = dict_of_ini['nw']['config_index']
    flag_of_nw = strtobool(dict_of_ini['nw']['nw_index_all'])

    csv_process.check_path(path_of_csv)
    csv_process.check_path(path_of_tpl)

    csv_process.check_index(path_of_csv, index_of_tpl)
    csv_process.check_index(path_of_csv, index_of_conf)

    if flag_of_nw:
        index_of_nw = csv_process.get_index(path_of_csv)
        index_of_nw.remove(index_of_tpl)
        index_of_nw.remove(index_of_conf)

        csv_process.check_index(path_of_csv, index_of_nw)

    else:
        csv_process.check_index(path_of_csv, index_of_nw)

    list_of_tpl = csv_process.get_columns(path_of_csv, index_of_tpl)
    dict_of_nw = csv_process.get_dictionary(path_of_csv, index_of_conf, index_of_nw)

    return path_of_tpl, list_of_tpl, dict_of_nw


def starter_pa(dict_of_ini):

    path_of_csv = os.path.join(dict_of_ini['csv']['csv_folder'], dict_of_ini['csv']['csv_file'])
    path_of_par = os.path.join(dict_of_ini['par']['par_folder'], dict_of_ini['par']['par_file'])
    index_of_nw = os.path.join(dict_of_ini['nw']['nw_index1'])
    index_of_conf = os.path.join(dict_of_ini['nw']['config_index'])

    csv_process.check_path(path_of_csv)
    csv_process.check_path(path_of_tpl)
    csv_process.check_path(path_of_par)

    csv_process.check_index(path_of_csv, index_of_tpl)
    csv_process.check_index(path_of_csv, index_of_conf)
    csv_process.check_index(path_of_csv, index_of_nw)

    list_of_tpl = csv_process.get_columns(path_of_csv, index_of_tpl)
    dict_of_nw = csv_process.get_dictionary(path_of_csv, index_of_conf, index_of_nw)

    return path_of_tpl, list_of_tpl, dict_of_nw

