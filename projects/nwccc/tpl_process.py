# -*- coding: utf-8 -*-

import os


def bond_tpl(path_of_tpl, list_of_tpl):
    x = ''
    path_of_tpl = os.path.dirname(path_of_tpl)

    for i in list_of_tpl:
        f = open(os.path.join(path_of_tpl, i))
        x += f.read() + '\n'

    return x


def check_file(path_of_tpl, tpl_list):
    path_of_tpl = os.path.dirname(path_of_tpl)
    b = os.path.isdir(path_of_tpl)

    if b:
        print('directory check...OK: ' + path_of_tpl)
    else:
        print('directory check...NG: ' + path_of_tpl)
        exit()

    for i in tpl_list:
        b = os.path.isfile(os.path.join(path_of_tpl, i))
        if b:
            print('file check...OK: ' + i)
        else:
            print('file check...NG: ' + i)
            exit()
