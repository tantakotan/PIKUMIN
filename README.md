# PYKUMIN
Code name "PYKUMIN"

![PYKUMIN](https://user-images.githubusercontent.com/26395852/50912580-d348bf00-1475-11e9-90b1-28410120384d.png)

- PPP が .ini のキーワードから CSV を処理し、そのパラメータやら何やらをPPMが各モジュールに渡すの図。

# 概要
- ネットワークエンジニアが作成する様々なドキュメントの自動化ツール(コンフィグ…パラメータシート…ラック搭載図…etc)
- オペレータが運用する部分と、デベロッパーの開発する部分とを明確に定義したアーキテクチャを採用
- モジュールはText形式とXlsx形式に対応

# Dependency
- python 3.7
- openpyxl  2.5.12
- jinja2 2.10

# Usage
- PYKUMIN.py を実行したら、PYKUMIN.ini に記載されたモジュールが自動実行されます。
- PPP は、.ini から各種PATHや、CSV用のIndex Key等を読み取りつつ前処理を担当します。
- PPM は、各種PYKUMIN モジュールを順番に実行するとともに、PPPで処理された情報をPYKUMINモジュールに渡します。
- PYKUMIN モジュールは、最終的に以下の情報を受け取ります。

```
dict_of_module : Template Files のDict
  text形式の場合 {1.text, 2.text, 3.text} or XLSX形式の場合 {Common : {1.xlsx : Sheet1, 1.xlsx : Sheet2}} 
path_of_module : Template Files のPATH
  ./projects/nwccc/tpls
dict_of_parameters : パラメータ用CSV のDict
  {l2SwitchA : {hostname : l2SwitchA, Vlan : 90, IP Address : 192.168.0.1, MASK : 255.255.255.0}, l2Switch B : {hostname : l2SwitchB ...}}
dict_of_option : .ini に記載したオプション
  {rowspase : 2}
```

こんな感じ？
明日、朝早いので寝ます…ZZZ

# Author...
色々いらっしゃるんで整理して書きます...zzz
