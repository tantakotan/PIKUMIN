# -*- coding: utf-8 -*-

from ppp import ppp as ppp
from ppp import ppm as ppm

# starting ppp...
pppi = ppp.PppExe(__file__)

# import ini path
pppi.import_ini()

# import project list
list_of_projects, path_of_project = pppi.import_projects()

# Start projcets
for projectname in list_of_projects:
    ppme = ppm.PpmExe(projectname, path_of_project)
    path_of_ppini = ppme.import_ini()

    pppc = ppp.PppCsv()
    list_of_module, path_of_module, dict_of_parameter = pppc.get_module(path_of_ppini)

    exit()

    # path_of_module, list_of_module, dict_of_module = ppp.exec_pppcsv(x)
    # eval(dict_of_projects[x])

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
