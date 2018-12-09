# -*- coding: utf-8 -*-

import csv

def columns_of_index(arg1, arg2):
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

