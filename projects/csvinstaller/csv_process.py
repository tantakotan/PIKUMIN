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


def get_dictionary(path_of_csv, index_of_conf, index_of_v):
    tmp_dict = dict()
    dict_of_conv = dict()
    num = 0
    global index_of_val

    if type(index_of_v) is str:
        index_of_val = [x.strip() for x in index_of_v.split(',')]
    elif type(index_of_v) is list:
        index_of_val = index_of_v

    list_of_conv = [[0 for i in range(0)] for j in range(len(index_of_val))]

    with open(path_of_csv, 'r', encoding='utf-8_sig') as f:
        for d1 in csv.DictReader(f):
            num += 1
            for i2 in range(len(index_of_val)):
                tmp_list = [d1[index_of_conf], d1[index_of_val[i2]]]
                list_of_conv[i2].append(tmp_list)

    for i in range(len(list_of_conv)):
        dict_of_conv[index_of_val[i]] = dict((list_of_conv[i]))

    return dict_of_conv


def get_index(path_of_csv):
    with open(path_of_csv, 'r', encoding='utf-8_sig') as f:
        index_of_index = csv.reader(f, delimiter=',')
        list_of_index = next(index_of_index)

    return list_of_index


def check_index(path_of_csv, index_of_hoge):
    global list_of_hoge
    with open(path_of_csv, 'r', encoding='utf-8_sig') as f:

        index_of_index = csv.reader(f, delimiter=',')
        list_of_index = next(index_of_index)

        if type(index_of_hoge) is str:
            list_of_hoge = [x.strip() for x in index_of_hoge.split(',')]
        elif type(index_of_hoge) is list:
            list_of_hoge = index_of_hoge

        for i2 in range(len(list_of_hoge)):
            count_index = [i for i, x in enumerate(list_of_index) if x == list_of_hoge[i2]]

            if list_of_hoge[i2] in list_of_index:
                print('index check...OK: ' + list_of_hoge[i2])
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
