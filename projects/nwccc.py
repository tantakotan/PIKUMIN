# -*- coding: utf-8 -*-

from projects.nwccc import tpl_process
from projects.nwccc import jinja2_process


class Nwccc:

    list_of_module = []
    path_of_module = ''
    dict_of_parameter = {}

    def __init__(self, list_of_module, path_of_module, dict_of_parameter):
        self.list_of_modul = list_of_module
        self.path_of_module = path_of_module
        self.dict_of_parameter = dict_of_parameter
        print('Hello World')



class exec_pykumin():

    def __init__(self):
        print('OKPK!!!')

    def starter_nwccc(self):
        tpl_process.check_file(path_of_tpl, list_of_tpl)
        otp_of_tpl = tpl_process.bond_tpl(path_of_tpl, list_of_tpl)

        str_of_nw = list(dict_of_conv.keys())[0]

        jinja2_process.create_template(otp_of_tpl, path_of_tpl, str_of_nw)

        for host_of_nw in dict_of_conv:

            dict_of_nw = dict(dict_of_conv[host_of_nw])
            otp_of_j2 = jinja2_process.j2_render(otp_of_tpl, dict_of_nw)
            jinja2_process.create_file(otp_of_j2, path_of_tpl, host_of_nw)

        exit()
