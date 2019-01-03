# -*- coding: utf-8 -*-

import sys
from projects.iniinstaller import iniinst
import configparser
from distutils.util import strtobool
import os
import csv

S_ = 'section: '
S_PROJECTS = 'projects'
S_GOD = 'god'
S_TPL = 'tpl'
S_NW = 'nw'
S_PS = 'ps'

I_ = 'item: '
I_PROJECTS_NWCCC = 'nwccc'
I_PROJECTS_PSHEETER = 'parasheeter'

I_GOD_FOLDER = 'god_folder'
I_GOD_FILE = 'god_file'

I_TPL_FOLDER = 'tpl_folder'
I_TPL_FILE = 'tpl_file'
I_TPL_INDEX = 'tpl_index'

I_NW_INDEX = 'nw_index'
I_NW_CONFIGINDEX = 'config_index'
I_NW_INDEX_ALL = 'nw_index_all'

I_PS_FOLDER = 'ps_folder'
I_PS_FILE = 'ps_file'
I_PS_INDEX = 'ps_index'
I_PS_SUBINDEX = 'ps_subindex'
I_PS_INDEX_ALL = 'ps_index_all'

K_ = 'key: '


path_of_god = ''
path_of_tpl = ''
index_of_tpl = ''
index_of_nw = ''
index_of_conf = ''
flag_of_nw = False
path_of_ps = ''
index_of_ps = ''
index_of_sh = ''
flag_of_ps = False

class PppExe:

    dict_of_ini = {}
    path_of_ini = ''

    def __init__(self, path_of_ini):
        print('Starting... PPP')

        self.path_of_ini = path_of_ini

    def get_projects(self):
        pppini = PppIni(self.path_of_ini)
        self.dict_of_ini = pppini.install_ini()
        tuple_of_projects = pppini.install_projects(S_PROJECTS)
        list_of_projects = [x for x, b in tuple_of_projects if strtobool(b)]

        return list_of_projects, self.dict_of_ini

    def exec_pppini(self):
        pppini = PppIni()
        dict_of_ini = pppini.install_ini(self.path_of_ini)

        self.dict_of_ini = dict_of_ini

    def exec_pppcsv(self, project):
        pppcsv = PppCsv()
        pppcsv.install_csv(self.dict_of_ini)
        tpl_list = pppcsv.get_columns(path_of_tpl, index_of_tpl)
        dict_of_conv = pppcsv.get_dictionary(path_of_god, index_of_conf, index_of_nw)

        return path_of_tpl, tpl_list, dict_of_conv,

    def check_nwflag(self):

        try:
            return strtobool(self.dict_of_ini[S_PROJECTS][I_PROJECTS_NWCCC])

        except ValueError as er:
            print('ValueError: {}{}, {}{}, {}{}'.format \
                 (S_ , S_PROJECTS, I_, I_PROJECTS_NWCCC, K_, er))
            exit()

class PppIni():

    path_of_ini = ''
    dict_of_ini = {}
    tuple_of_projects = ()

    class_of_ini = configparser.ConfigParser()

    def __init__(self, path_of_ini):
        self.path_of_ini = path_of_ini
        self.class_of_ini.read(self.path_of_ini, 'UTF-8')

    def install_ini(self):
        list_of_inisections = self.class_of_ini.sections()

        for x in list_of_inisections:
            self.dict_of_ini[x] = dict(self.class_of_ini.items(x))

        return self.dict_of_ini

    def install_projects(self, S_SECTIONS):
        tuple_of_projects = self.class_of_ini.items(S_SECTIONS)
        print(tuple_of_projects)

        return tuple_of_projects

class PppCsv:

    def __init__(self):
        self.dict_of_ini = {}

    def install_csv(self, dict_of_ini):
        global path_of_god, path_of_tpl, index_of_tpl, index_of_nw, index_of_conf, flag_of_nw, \
               path_of_ps, index_of_ps, index_of_sh, flag_of_ps

        try:
            path_of_god = os.path.join(dict_of_ini[S_GOD][I_GOD_FOLDER], dict_of_ini[S_GOD][I_GOD_FILE])
            path_of_tpl = os.path.join(dict_of_ini[S_TPL][I_TPL_FOLDER], dict_of_ini[S_TPL][I_TPL_FILE])
            index_of_tpl = dict_of_ini[S_TPL][I_TPL_INDEX]

            index_of_nw = dict_of_ini[S_NW][I_NW_INDEX]
            index_of_conf = dict_of_ini[S_NW][I_NW_CONFIGINDEX]
            flag_of_nw = strtobool(dict_of_ini[S_NW][I_NW_INDEX_ALL])

            path_of_ps = os.path.join(dict_of_ini[S_PS][I_PS_FOLDER], dict_of_ini[S_PS][I_PS_FILE])
            index_of_ps = dict_of_ini[S_PS][I_PS_INDEX]
            index_of_sh = dict_of_ini[S_PS][I_PS_SUBINDEX]
            flag_of_ps = strtobool(dict_of_ini[S_PS][I_PS_INDEX_ALL])

        except KeyError as er:
            print('KeyNotFound: ', er)
            pass
        except ValueError as er:
            print('ValueError: ', 'check your .ini parameter: ', '"*_index_all" can be used "True,yes,y,1 or None,no,n,0"')
            exit()

        if flag_of_nw:
            try:
                pppcsv = PppCsv()
                index_of_nw = pppcsv.get_index(path_of_god)
            except FileNotFoundError as er:
                print('FileNotFoundError: ', er)
                exit()

            try:
                index_of_nw.remove(index_of_conf)
            except ValueError as er:
                print('ValueError: ', 'check your ini parameter: "config_index"=', index_of_conf)
                exit()
        
        return 

    def get_index(self, path_of_god):
        with open(path_of_god, 'r', encoding='utf-8_sig') as f:
            index_of_index = csv.reader(f, delimiter=',')
            list_of_index = next(index_of_index)

        return list_of_index

    def get_columns(self, path_of_tpl, index_of_tpl):
        with open(path_of_tpl, 'r', encoding='utf-8_sig') as f:
            tpl = csv.reader(f, delimiter=',')
            tpl_list = []
            index_list = next(tpl)
            index_num = [i for i, x in enumerate(index_list) if x == index_of_tpl]

            if len(index_num) >= 2:
                print(index_of_tpl + ' is ' + str(index_num) + ' count from ' + path_of_tpl)
                exit()

            for x in tpl:
                if x[index_num[0]]:
                    tpl_list.append(x[index_num[0]])

        return tpl_list

    def get_dictionary(self, path_of_csv, index_of_conf, index_of_value):
        dict_of_conv = dict()
        num = 0
        global index_of_val

        if type(index_of_value) is str:
            index_of_val = [x.strip() for x in index_of_value.split(',')]
        elif type(index_of_value) is list:
            index_of_val = index_of_value

        list_of_conv = [[0 for i in range(0)] for j in range(len(index_of_val))]

        with open(path_of_csv, 'r', encoding='utf-8_sig') as f:
            for d1 in csv.DictReader(f):
                num += 1
                for i2 in range(len(index_of_val)):
                    tmp_list = [d1[index_of_conf], d1[index_of_val[i2]]]
                    list_of_conv[i2].append(tmp_list)

        for i in range(len(list_of_conv)):
            dict_of_conv[index_of_val[i]] = dict((list_of_conv[i]))

        return dict_of_conv