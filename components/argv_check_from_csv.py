# -*- coding: utf-8 -*-

import sys
import csv

## 辞書オブジェクト
parashi = dict()

# 第一引数がちゃんと入力されているかの確認
if len(sys.argv) == 2:
    print("引数入力OK")
else:
    print("引数入力NG")
    print("example: python sample.py device_name")
    exit()

# --------------対象となるCSVを色々と指定するところ--------------------
csvfile = 'sample.csv'
dev = sys.argv[1]

# CSVからデバイス名の抽出 row = CSVファイルの index に書いてあるデバイス名
with open(csvfile, "r", encoding="utf-8_sig") as f:
    row = f.readline().replace('\n', '').split(",")
    config = row.pop(0)     # csv の index 名をここで取得してしまう

# デバイス名が正常なものかどうか確認する
if(dev in row):
    print("引数デバイス名OK: ", dev, )
else:
    print(
    "引数デバイス名NG\n"
    " CSVファイル名:",csvfile,"\n"
    " 入力可能デバイス名:",row
    )
    exit()

# 神様データの読み込み
with open(csvfile, "r", encoding="utf-8_sig") as f:
    for i in csv.DictReader(f):
        parashi[i[config]] = i[dev]

