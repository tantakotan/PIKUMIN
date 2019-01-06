# -*- coding: utf-8 -*-

from projects.parasheeter import pslsx_process
from projects.nwccc import jinja2_process


class ExecPykumin:

    def __init__(self, dict_of_module, path_of_module, dict_of_parameter, dict_of_option):
        num_of_space = int(dict_of_option['option_rowspace'])

        execpslsx = pslsx_process.ExecPslsx(dict_of_module, path_of_module, dict_of_parameter, dict_of_option)
        execpslsx.get_keys()
        execpslsx.get_outputpath()
        execpslsx.get_spacerow(num_of_space)
        execpslsx.get_template()
        path_of_tplxlsx = execpslsx.return_tplpath()

        j2render = jinja2_process.J2Render(dict_of_parameter)
        j2render.create_template_key()
        j2render.create_outputdir(path_of_module)

        for key_of_parameter in dict_of_parameter:
            j2render.create_parameter_host(key_of_parameter)
            j2render.j2_render_xlsx(path_of_tplxlsx)
            j2render.create_file_xlsx(key_of_parameter)
