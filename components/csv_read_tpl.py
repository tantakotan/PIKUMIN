# -*- coding: utf-8 -*-

import os
import csv

#------csv_read_tpl.py--------#
csvfile = 'sample.csv'
tpl_list = []
tpl_folder = './tpls'
tpl_appends_complete = ''

with open(csvfile, "r", encoding="utf-8_sig") as f:
    tpl = csv.reader(f, delimiter=',')
    trash = next(tpl)

    for x in tpl:
        if x[0]:
            tpl_list.append(x[0])

    for i in tpl_list:
        f = open(os.path.join(tpl_folder, i))
        tpl_appends_complete += f.read() + "\n"

print()
print(tpl_appends_complete)
print()

#------csv_read_tpl.py--------#


