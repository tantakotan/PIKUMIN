# -*- coding: utf-8 -*-

import os
import openpyxl
import re

def get_template(path_of_ps, dict_of_ps):
    path_of_pslsx = os.path.dirname(path_of_ps)

    list_of_sheet = list(dict_of_ps.keys())
    list_of_wbnsh = []

    # common と common_sheet の関連性の識別に前方一致 + '_' を暫定的に用いているが…
    for i in range(len(list_of_sheet)):
        exc = list_of_sheet[i] + '[^0-9A-Za-z]+|' + list_of_sheet[i] + '$'
        i2 = [i2 for i2, x in enumerate(list_of_sheet) if re.match(exc, x)]

        if len(i2) == 2:
            list_of_wbnsh.append(i2)
            print(list_of_wbnsh)


    print(list_of_wbnsh)
    print(list_of_wbnsh[0])
    print(list_of_wbnsh[1])

    unko = []
    unko2 = []

    for i in range(len(list_of_wbnsh)):
        print('28: ' + str(list_of_wbnsh[i]))
        for i2 in range(len(list_of_wbnsh[i])):
            print('30: ' + str(list_of_wbnsh[i][i2]))
            print('31: ' + str(list_of_sheet[list_of_wbnsh[i][i2]]))
            print('32: ' + str(dict_of_ps[list_of_sheet[list_of_wbnsh[i][i2]]]))
            for i3 in dict_of_ps[list_of_sheet[list_of_wbnsh[i][i2]]]:
                print('35: ' + str(dict_of_ps[list_of_sheet[list_of_wbnsh[i][i2]]][i3]))
                unko.extend(dict_of_ps[list_of_sheet[list_of_wbnsh[i][i2]]][i3])

    for i in dict_of_ps:
        print(i)
        

    exit()

    print(list_of_wbnsh)
    print(list_of_wbnsh[0][0])
    print(list_of_wbnsh[0][1])
    print(list_of_wbnsh[1][0])
    print(list_of_wbnsh[1][1])

    print(list_of_sheet[list_of_wbnsh[0][0]])
    print(list_of_sheet[list_of_wbnsh[0][1]])
    print(list_of_sheet[list_of_wbnsh[1][0]])
    print(list_of_sheet[list_of_wbnsh[1][1]])

    print(dict_of_ps[list_of_sheet[list_of_wbnsh[0][0]]])
    print(dict_of_ps[list_of_sheet[list_of_wbnsh[0][1]]])
    print(dict_of_ps[list_of_sheet[list_of_wbnsh[1][0]]])
    print(dict_of_ps[list_of_sheet[list_of_wbnsh[1][1]]])

    print(dict_of_ps[list_of_sheet[list_of_wbnsh[0][0]]]['1'])
    print(dict_of_ps[list_of_sheet[list_of_wbnsh[0][1]]]['1'])
    print(dict_of_ps[list_of_sheet[list_of_wbnsh[0][0]]]['2'])
    print(dict_of_ps[list_of_sheet[list_of_wbnsh[0][1]]]['2'])
    print(dict_of_ps[list_of_sheet[list_of_wbnsh[0][0]]]['3'])
    print(dict_of_ps[list_of_sheet[list_of_wbnsh[0][1]]]['3'])
    print(dict_of_ps[list_of_sheet[list_of_wbnsh[0][0]]]['4'])
    print(dict_of_ps[list_of_sheet[list_of_wbnsh[0][1]]]['4'])


    print(dict_of_ps[list_of_sheet[list_of_wbnsh[1][0]]]['1'])
    print(dict_of_ps[list_of_sheet[list_of_wbnsh[1][1]]]['1'])
    print(dict_of_ps[list_of_sheet[list_of_wbnsh[1][0]]]['2'])
    print(dict_of_ps[list_of_sheet[list_of_wbnsh[1][1]]]['2'])
    print(dict_of_ps[list_of_sheet[list_of_wbnsh[1][0]]]['3'])
    print(dict_of_ps[list_of_sheet[list_of_wbnsh[1][1]]]['3'])
    print(dict_of_ps[list_of_sheet[list_of_wbnsh[1][0]]]['4'])
    print(dict_of_ps[list_of_sheet[list_of_wbnsh[1][1]]]['4'])



    exit()

# def bond_tpl(path_of_tpl, list_of_tpl):
#     x = ''
#     path_of_tpl = os.path.dirname(path_of_tpl)
#
#     for i in list_of_tpl:
#         f = open(os.path.join(path_of_tpl, i))
#         x += f.read() + '\n'
#
#     return x
#
#

def check_pslsx(path_of_ps, dict_of_ps):
    path_of_pslsx = os.path.dirname((path_of_ps))


    # try:
    #     print('directory check...OK: ' + path_of_pslsx)
    #     exit()
    # except UnicodeError:
    #     exit

    # else:
    #     print('directory check...NG: ' + path_of_tpl)
    #     exit()
    #
    # for i in tpl_list:
    #     b = os.path.isfile(os.path.join(path_of_tpl, i))
    #     if b:
    #         print('file check...OK: ' + i)
    #     else:
    #         print('file check...NG: ' + i)
    #         exit()