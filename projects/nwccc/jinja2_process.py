# -*- coding: utf-8 -*-

from datetime import datetime
from jinja2 import Environment
import os


def j2_render(text_of_template, dict_of_config):
    env = Environment()
    env.trim_blocks = True
    env.lstrip_blocks = True

    s = env.from_string(text_of_template)
    s2 = s.render(dict_of_config)
    return s2


def create_file(j2_temp, directory_path, file_name):
    s = datetime.now()
    s2 = file_name + '_' + s.strftime('%Y%m%d') + '.conf'
    s3 = os.path.join(directory_path, s2)

    with open(s3, mode='w') as f:
        f.write(j2_temp)

    print('create file successfuly...: ' + s3)


def create_template(template_string, directory_path, file_name):
    s = datetime.now()
    s2 = file_name + '_template_' + s.strftime('%Y%m%d') + '.conf'
    s3 = os.path.join(directory_path, s2)

    with open(s3, mode='w') as f:
        f.write(template_string)

    print('create template successfuly...: ' + s3)
