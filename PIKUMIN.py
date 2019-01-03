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
from ppp import ppp as ppp
from ppp import ppm as ppm

# starting ppp...
ppp = ppp.PppExe(__file__)

# import ini path
ppp.import_ini()

# import project list
list_of_projects, path_of_project = ppp.import_projects()
print(list_of_projects, path_of_project)

# Start projcets
for projectname in list_of_projects:
    ppme = ppm.PpmExe(projectname, path_of_project)
    path_of_ppini = ppme.import_ini()
    dict_of_ini = ppp.exec_pppini(path_of_ppini)




    # path_of_module, list_of_module, dict_of_module = ppp.exec_pppcsv(x)
    # eval(dict_of_projects[x])

# install INI
dict_of_ini = ppp.get_projects()



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
