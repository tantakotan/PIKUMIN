# -*- coding: utf-8 -*-

import os
import openpyxl

class starter_parasheeter:
    dict_of_ps = {}
    dict_of_nw = {}
    path_of_ps = ''

    def __init__(self, path_of_ps, dict_of_ps, dict_of_nw):
        self.path_of_ps = path_of_ps
        self.dict_of_ps = dict_of_ps
        self.dict_of_nw = dict_of_nw

    def get_template(self):
        path_of_pslsx = os.path.dirname(self.path_of_ps)

        dict_of_swap = self.dict_of_ps
        dict_of_pslsx = {}
        for i in dict_of_swap:
            list_of_pslsx = [[v, k] for k, v in dict_of_swap[i].items()]
            dict_of_pslsx[i] = list_of_pslsx

        list_of_key = list(dict_of_pslsx.keys())

        for i in list_of_key:
            print(dict_of_pslsx[i])

            for i2 in dict_of_pslsx[i]:
                path_of_wb = os.path.join(path_of_pslsx, i2[0])
                wb = openpyxl.load_workbook(path_of_wb)
                sheet = wb[i2[1]]

                print(sheet.min_row, sheet.max_row)







