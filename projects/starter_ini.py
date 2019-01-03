# -*- coding: utf-8 -*-

import sys
from projects.iniinstaller import iniinst

def starterIni(arg1):
    print(arg1)

    check_ini = iniinst.IniInstall(arg1)
    dict_of_ini = check_ini.read_ini()

    return dict_of_ini