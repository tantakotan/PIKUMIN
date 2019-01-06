# -*- coding: utf-8 -*-

from ppp import ppp as ppp
from ppp import ppm as ppm

# starting ppp...
pppi = ppp.PppExe(__file__)

# import ini path
pppi.import_pini()

# import project list
path_of_project = pppi.import_projects()
list_of_projects = pppi.check_projects()
print('''--------------------''')

# Start projcets
for projectname in list_of_projects:
    ppme = ppm.PpmExe(projectname, path_of_project)
    path_of_ppini = ppme.import_ppini()

    pppc = ppp.PppCsv()
    list_of_module, path_of_module, dict_of_parameter, dict_of_option = pppc.get_module(path_of_ppini)

    pppc.eof()

    ppme.start_project(list_of_module, path_of_module, dict_of_parameter, dict_of_option)
