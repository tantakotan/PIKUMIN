# -*- coding: utf-8 -*-

import sys
from projects.iniinstaller import iniinst

def starter(arg1):
    print(arg1)

    check_ini = iniinst.IniInstall(arg1)
    dict_of_ini = check_ini.read_ini()

    return dict_of_ini