# -*- coding: utf-8 -*-
#
# import os
# from distutils.util import strtobool
# # from projects import main_nwccc as pjpr
# from projects import starter_csv as pjcs
# from projects import starter_ini as pjin
# from projects import starter_nwccc as pjnw
# from projects import starter_parasheeter as pjps
#

from projects import *
import glob
import os

# import ini path
path_of_ini, trashbox = os.path.splitext(__file__)
path_of_ini = path_of_ini + '.ini'

# import project list
list_of_allprojects = glob.glob('./projects/*.py')

# install INI
ppp = ppp.PppExe(path_of_ini)
list_of_projects, dict_of_ini = ppp.get_projects()

print(list_of_projects)
print(dict_of_ini)

# Start projcets
for x in list_of_projects:
    path_of_module, list_of_module, dict_of_module = ppp.exec_pppcsv(x)
    eval(dict_of_projects[x])


# ppp.exec_pppini()
# ppp.check_nwflag()

#
# # check PROJECTS
# if ppp.check_nwflag():
#     path_of_tpl, list_of_tpl, dict_of_nw = ppp.exec_pppcsvnw()
#
#
#     pjnw.starter_nwccc(path_of_tpl, list_of_tpl, dict_of_nw)
#
# if strtobool(dict_of_ini['projects']['parasheeter']):
#     path_of_ps, dict_of_ps, dict_of_nw = pjcs.starter_ps(dict_of_ini)
#     ppp = pjps.starter_parasheeter(path_of_ps, dict_of_ps, dict_of_nw)
#     ppp.get_template()
#
#
#     # if str.title(dict_of_ini['projects']['processer']) == 'True':
#     #     pjpr.starter(dict_of_ini)
#     #
