# -*- coding: utf-8 -*-

from projects.nwccc import tpl_process
from projects.nwccc import jinja2_process


def starter_nwccc(path_of_tpl, list_of_tpl, dict_of_nw):

    tpl_process.check_file(path_of_tpl, list_of_tpl)
    tpl_of_tpl = tpl_process.bond_tpl(path_of_tpl, list_of_tpl)
    str_of_host = dict_of_nw['hostname']

    jinja2_process.create_template(tpl_of_tpl, path_of_tpl, str_of_host)
    tpl_of_j2 = jinja2_process.j2_render(tpl_of_tpl, dict_of_nw)
    jinja2_process.create_file(tpl_of_j2, path_of_tpl, str_of_host)

    exit()
