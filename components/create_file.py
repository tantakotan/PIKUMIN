import os
from datetime import datetime
import sys

dev = sys.argv[1]
tr = '書き込みたい内容！！！！！'
tpl_folder = './tpls' # 書き込みたいフォルダパス

tdatetime = datetime.now()
create_file: str = dev + '_' + tdatetime.strftime('%Y%m%d') + '.conf'

with open(os.path.join(tpl_folder, create_file), mode='w') as f:
    f.write(tr)
    print(tr)

