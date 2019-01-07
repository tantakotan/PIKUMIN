# -*- coding: utf-8 -*-

import os


class ExecTpl:

    def __init__(self, list_of_tpl, path_of_tpl):
        self.x = ''
        self.path_of_tpl = path_of_tpl
        self.list_of_tpl = list_of_tpl

    def bond_tpl(self):

        for i in self.list_of_tpl:
            f = open(os.path.join(self.path_of_tpl, i))
            self.x += f.read() + '\n'

        return self.x

    def check_file(self):
        b = os.path.isdir(self.path_of_tpl)

        if b:
            print('directory check...OK: ' + self.path_of_tpl)
        else:
            print('directory check...NG: ' + self.path_of_tpl)
            exit()

        for i in self.list_of_tpl:
            b = os.path.isfile(os.path.join(self.path_of_tpl, i))

            if b:
                print('file check...OK: ' + i)
            else:
                print('file check...NG: ' + i)
                exit()
