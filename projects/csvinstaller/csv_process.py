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


def get_index(path_of_csv):
    with open(path_of_csv, 'r', encoding='utf-8_sig') as f:
        index_of_index = csv.reader(f, delimiter=',')
        list_of_index = next(index_of_index)

    return list_of_index


def check_index(path_of_csv, index_of_hoge):
    with open(path_of_csv, 'r', encoding='utf-8_sig') as f:

        index_of_index = csv.reader(f, delimiter=',')
        list_of_index = next(index_of_index)

        if type(index_of_hoge) is str:
            index_of_hoge = index_of_hoge.replace(' ', '')
            list_of_hoge = index_of_hoge.split(',')
        elif type(index_of_hoge) is list:
            list_of_hoge = index_of_hoge

        i2 = 0

        while i2 < len(list_of_hoge):

            count_index = [i for i, x in enumerate(list_of_index) if x == list_of_hoge[i2]]

            if list_of_hoge[i2] in list_of_index:
                print('index check...OK: ' + list_of_hoge[i2])
                i2 += 1
            else:
                print('index check...NG: ' + list_of_hoge[i2])
                exit()

            if len(count_index) < 2:
                print('index count check...OK: ' + str(count_index))
            else:
                print('index count check...NG: ' + list_of_hoge + ' is ' + str(count_index) + ' duplicated')
                exit()


def check_path(path):
    if os.path.exists(path):
        print('file path check...OK: ' + path)
    else:
        print('file path check...NG: ' + path)
        exit()