# -*- coding: utf-8 -*-

import os
from distutils.util import strtobool
# from projects import main_nwccc as pjpr
from projects import starter_csv as pjcs
from projects import starter_ini as pjin
from projects import starter_nwccc as pjnw
from projects import starter_parasheeter as pjps

# path import
path_of_ini, trashbox = os.path.splitext(__file__)
path_of_ini = path_of_ini + '.ini'

# install INI
dict_of_ini = pjin.starterIni(path_of_ini)
print(dict_of_ini)

# check PROJECTS
if strtobool(dict_of_ini['projects']['nwccc']):
    path_of_tpl, list_of_tpl, dict_of_nw = pjcs.starter_nw(dict_of_ini)
    pjnw.starter_nwccc(path_of_tpl, list_of_tpl, dict_of_nw)

if strtobool(dict_of_ini['projects']['parasheeter']):
    path_of_ps, dict_of_ps, dict_of_nw = pjcs.starter_ps(dict_of_ini)
    pjps.starter_parasheeter(path_of_ps, dict_of_ps, dict_of_nw)

    # if str.title(dict_of_ini['projects']['processer']) == 'True':
    #     pjpr.starter(dict_of_ini)
    #
