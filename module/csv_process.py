# -*- coding: utf-8 -*-

import csv

def list_of_index(arg1, arg2):
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

def dict_of_indexs(arg1, arg2, arg3):
    with open(arg1, 'r', encoding='utf-8_sig') as f:
        dev_dict = dict()
        for i in csv.DictReader(f):
            dev_dict[i[arg2]] = i[arg3]

        return dev_dict

def check_of_index(arg1, arg2):
    with open(arg1, 'r', encoding='utf-8_sig') as f:
        tpl = csv.reader(f, delimiter=',')
        index_list = next(tpl)
        index_num = [i for i, x in enumerate(index_list) if x == arg2]

        if arg2 in index_list:
            print('index check...OK: ' + arg2)
        else:
            print('index check...NG: ' + arg2)
            exit()

        if len(index_num) < 2:
            print('index count check...OK: ' + str(index_num))
        else:
            print('index count check...NG: ' + arg2 + ' is ' + str(index_num) + ' duplicated')
            exit()












