# -*- coding: utf-8 -*-

from projects.parasheeter import pslsx_process
# from projects.parasheeter import jinja2_process


def starter_parasheeter(path_of_ps, dict_of_ps, dict_of_conv):

    pslsx_process.check_pslsx(path_of_ps, dict_of_ps)
    pslsx_process.get_template(path_of_ps, dict_of_ps)









    # tpl_process.check_file(path_of_pslsx, list_of_pslsx)
    # otp_of_tpl = tpl_process.bond_tpl(path_of_pslsx, list_of_pslsx)
    #
    # str_of_nw = list(dict_of_conv.keys())[0]
    #
    # jinja2_process.create_template(otp_of_tpl, path_of_pslsx, str_of_nw)
    #
    # for host_of_nw in dict_of_conv:
    #
    #     dict_of_nw = dict(dict_of_conv[host_of_nw])
    #     otp_of_j2 = jinja2_process.j2_render(otp_of_tpl, dict_of_nw)
    #     jinja2_process.create_file(otp_of_j2, path_of_pslsx, host_of_nw)
    #
    exit()
