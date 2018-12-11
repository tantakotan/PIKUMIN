# -*- coding: utf-8 -*-

from datetime import datetime
import os
import sys
import csv
from jinja2 import Template, Environment, FileSystemLoader
import openpyxl

# 第一引数がちゃんと入力されているかの確認
if len(sys.argv) == 2:
    print("引数入力OK")
else:
    print("引数入力NG")
    print("example: python sample.py device_name")
    exit()

## オブジェクトの生成まとめ
parashi = dict()
csv_folder = './tpls'
csvfile = 'sample.csv'
tpl_list = []
tpl_folder = './tpls'
tpl_appends_complete = ''
dev = sys.argv[1]
config_column = 1

# path
csv_path = os.path.join(csv_folder, csvfile)

# テンプレートファイルの読み込み
env = Environment(loader = FileSystemLoader('.'))
env.trim_blocks = True
env.lstrip_blocks = True

#----------argv_check_from_csv.py-----------#
# CSVからデバイス名の抽出 row = CSVファイルの index に書いてあるデバイス名
with open(csv_path, "r", encoding="utf-8_sig") as f:
    row = f.readline().replace('\n', '').split(",")
    config = row.pop(config_column)     # csv の index 名をここで取得してしまう

# デバイス名が正常なものかどうか確認する
if(dev in row):
    print("引数デバイス名OK: ", dev, )
else:
    print(
    "引数デバイス名NG\n"
    " CSVパス:",csv_path,"\n"
    " 入力可能デバイス名:",row
    )
    exit()

#----------argv_check_from_csv.py-----------#

#------csv_read_tpl.py--------#
with open(csv_path, "r", encoding="utf-8_sig") as f:
    tpl = csv.reader(f, delimiter=',')
    trash = next(tpl)

    for x in tpl:
        if x[0]:
            tpl_list.append(x[0])

    for i in tpl_list:
        f = open(os.path.join(tpl_folder, i))
        tpl_appends_complete += f.read() + "\n"

tdatetime = datetime.now()
template_file = dev + '_template' + '_' + tdatetime.strftime('%Y%m%d') + '.conf'

with open(os.path.join(tpl_folder, template_file), mode='w') as f:
    f.write(tpl_appends_complete)


#------csv_read_tpl.py--------#

#------jinja2_render-------#
with open(csv_path, "r", encoding="utf-8_sig") as f:
    for i in csv.DictReader(f):
        parashi[i[config]] = i[dev]


tem = env.from_string(tpl_appends_complete)

tr = tem.render(parashi)
#------jinja2_render-------#

#------create_file.py--------#
tdatetime = datetime.now()
create_file = dev + '_' + tdatetime.strftime('%Y%m%d') + '.conf'

print(os.path.join(tpl_folder, create_file))

with open(os.path.join(tpl_folder, create_file), mode='w') as f:
    f.write(tr)
    print(tr)

#------create_file.py--------#

