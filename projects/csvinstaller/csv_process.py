# -*- coding: utf-8 -*-

import csv
import os


def get_columns(arg1, arg2):

    with open(arg1, 'r', encoding='utf-8_sig') as f:
        tpl = csv.reader(f, delimiter=',')
        tpl_list = []
        index_list = next(tpl)
        index_num = [i for i, x in enumerate(index_list) if x == arg2]

        if len(index_num) >= 2:
            print(arg2 + ' is ' + str(index_num) + ' count from ' + arg1)
            exit()

        for x in tpl:
            if x[index_num[0]]:
                tpl_list.append(x[index_num[0]])

    return tpl_list


def get_dictionary(arg1, arg2, arg3):
    with open(arg1, 'r', encoding='utf-8_sig') as f:
        dev_dict = dict()
        for i in csv.DictReader(f):
            dev_dict[i[arg2]] = i[arg3]

    return dev_dict


def check_index(arg1, arg2):
    with open(arg1, 'r', encoding='utf-8_sig') as f:
        index_of_index = csv.reader(f, delimiter=',')
        list_of_index = next(index_of_index)
        count_index = [i for i, x in enumerate(list_of_index) if x == arg2]
        print(count_index)

        if arg2 in list_of_index:
            print('index check...OK: ' + arg2)
        else:
            print('index check...NG: ' + arg2)
            exit()

        if len(count_index) < 2:
            print('index count check...OK: ' + str(count_index))
        else:
            print('index count check...NG: ' + arg2 + ' is ' + str(count_index) + ' duplicated')
            exit()


def check_path(path):
    if os.path.exists(path):
        print('file path check...OK: ' + path)
    else:
        print('file path check...NG: ' + path)
        exit()
