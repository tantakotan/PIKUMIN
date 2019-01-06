# -*- coding: utf-8 -*-

from projects.parasheeter import pslsx_process


class ExecPykumin:

    def __init__(self, dict_of_module, path_of_module, dict_of_parameter, dict_of_option):
        execpslsx = pslsx_process.ExecPslsx(dict_of_module, path_of_module, dict_of_parameter, dict_of_option)
        execpslsx.get_keys()
        execpslsx.get_outputpath()
        execpslsx.get_spacerow()
        execpslsx.get_template()
