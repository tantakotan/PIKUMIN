# -*- coding: utf-8 -*-

import os
from projects.csvinstaller import csv_process
from distutils.util import strtobool


def starter_nw(dict_of_ini):

    path_of_god = os.path.join(dict_of_ini['god']['god_folder'], dict_of_ini['god']['god_file'])
    path_of_tpl = os.path.join(dict_of_ini['tpl']['tpl_folder'], dict_of_ini['tpl']['tpl_file'])
    index_of_tpl = dict_of_ini['tpl']['tpl_index']
    index_of_nw = dict_of_ini['nw']['nw_index']
    index_of_conf = dict_of_ini['nw']['config_index']
    flag_of_nw = strtobool(dict_of_ini['nw']['nw_index_all'])

    csv_process.check_path(path_of_god)
    csv_process.check_path(path_of_tpl)

    csv_process.check_index(path_of_god, index_of_conf)
    csv_process.check_index(path_of_tpl, index_of_tpl)
    if flag_of_nw:
        index_of_nw = csv_process.get_index(path_of_god)
        index_of_nw.remove(index_of_conf)
    csv_process.check_index(path_of_god, index_of_nw)

    list_of_tpl = csv_process.get_columns(path_of_tpl, index_of_tpl)
    dict_of_nw = csv_process.get_dictionary(path_of_god, index_of_conf, index_of_nw)

    return path_of_tpl, list_of_tpl, dict_of_nw


def starter_ps(dict_of_ini):

    path_of_god = os.path.join(dict_of_ini['god']['god_folder'], dict_of_ini['god']['god_file'])
    path_of_ps = os.path.join(dict_of_ini['ps']['ps_folder'], dict_of_ini['ps']['ps_file'])
    index_of_ps = dict_of_ini['ps']['ps_index']
    index_of_sh = dict_of_ini['ps']['ps_subindex']
    index_of_nw = dict_of_ini['nw']['nw_index']
    index_of_conf = dict_of_ini['nw']['config_index']
    flag_of_ps = strtobool(dict_of_ini['ps']['ps_index_all'])
    flag_of_nw = strtobool(dict_of_ini['nw']['nw_index_all'])

    csv_process.check_path(path_of_god)
    csv_process.check_path(path_of_ps)

    list_of_pspair = []
    dict_of_ps = {}

    if flag_of_ps:
        index_of_ps = csv_process.get_index(path_of_ps)
        for x in index_of_ps:
            list_of_ppp = [[i, x] for i in index_of_ps if x + index_of_sh in i]
            list_of_pspair.extend(list_of_ppp)
    else:
        index_of_ps = [index_of_ps.strip() for index_of_ps in index_of_ps.split(',')]
        for x in index_of_ps:
            list_of_pspair.append([x + index_of_sh], x)
            print(list_of_pspair)
    csv_process.check_index(path_of_ps, index_of_ps)

    if flag_of_nw:
        index_of_nw = csv_process.get_index(path_of_god)
        index_of_nw.remove(index_of_conf)
    csv_process.check_index(path_of_god, index_of_nw)

    for i in list_of_pspair:
        dict_of_temp = csv_process.get_dictionary(path_of_ps, i[0], i[1])
        dict_of_ps.update(dict_of_temp)

    dict_of_nw = csv_process.get_dictionary(path_of_god, index_of_conf, index_of_nw)

    print(path_of_ps)
    print(dict_of_ps)
    print(dict_of_nw)

    exit()

    return path_of_ps, dict_of_ps, dict_of_nw
