# -*- coding: utf-8 -*-

from projects.nwccc import tpl_process
from projects.nwccc import jinja2_process


class Nwccc:

    list_of_module = []
    path_of_module = ''
    dict_of_parameter = {}

    def __init__(self, list_of_module, path_of_module, dict_of_parameter):
        self.list_of_module = list_of_module
        self.path_of_module = path_of_module
        self.dict_of_parameter = dict_of_parameter


class ExecPykumin:

    def __init__(self, list_of_module, path_of_module, dict_of_parameter, dict_of_option):

        exectpl = tpl_process.ExecTpl(list_of_module, path_of_module)
        exectpl.check_file()
        text_of_tpl = exectpl.bond_tpl()

        j2render = jinja2_process.J2Render(dict_of_parameter)
        j2render.create_template_key()
        j2render.create_outputdir(path_of_module)
        j2render.create_template(text_of_tpl)

        for key_of_parameter in dict_of_parameter:
            j2render.create_parameter_host(key_of_parameter)
            j2render.j2_render(text_of_tpl)
            j2render.create_file(key_of_parameter)

        self.dict_of_option = dict_of_option
