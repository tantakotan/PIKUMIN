# -*- coding: utf-8 -*-

import os


def bond(arg1, arg2):
    x = ''

    for i in arg2:
        f = open(os.path.join(arg1, i))
        x += f.read() + '\n'

    return x


def check_of_file(tpl_path, tpl_list):
    b = os.path.isdir(tpl_path)

    if b:
        print('directory check...OK: ' + tpl_path)
    else:
        print('directory check...NG: ' + tpl_path)
        exit()

    for i in tpl_list:
        b = os.path.isfile(os.path.join(tpl_path, i))
        if b:
            print('file check...OK: ' + i)
        else:
            print('file check...NG: ' + i)
            exit()
