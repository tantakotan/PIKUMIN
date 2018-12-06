from jinja2 import Template, Environment, FileSystemLoader
import csv
import sys

# テンプレートファイルの読み込み
env = Environment(loader = FileSystemLoader('.'))
env.trim_blocks = True
env.lstrip_blocks = True

## オブジェクトの生成まとめ
parashi = dict()
csvfile = 'sample.csv'
tplfile = 'sample.tpl'
config_column = 1
dev = sys.argv[1]

with open(csvfile, "r", encoding="utf-8_sig") as f:
    row = f.readline().replace('\n', '').split(",")
    config = row.pop(config_column)

with open(csvfile, "r", encoding="utf-8_sig") as f:
    for i in csv.DictReader(f):
        parashi[i[config]] = i[dev]

tem = env.get_template(tplfile)
tr = tem.render(parashi)
