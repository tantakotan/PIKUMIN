# -*- coding: utf-8 -*-

import configparser
from distutils.util import strtobool
import os
import csv


class PppExe:

    path_of_exe = ''
    path_of_exedir = ''
    path_of_ini = ''
    path_of_projects = ''
    dict_of_ini = {}
    list_of_projects = []

    def __init__(self, path_of_exe):
        print('Starting... PPP:', path_of_exe)
        self.path_of_exe = path_of_exe
        self.path_of_exedir = os.path.dirname(path_of_exe)
        self.path_of_project = ''
        self.dict_of_project = {}

    def import_pini(self):
        path_of_ini, trashbox = os.path.splitext(self.path_of_exe)
        self.path_of_ini = path_of_ini + '.ini'

    def import_projects(self):
        self.path_of_project = self.path_of_exedir + '/projects/'

        return self.path_of_project

    def check_projects(self):
        cp = configparser.ConfigParser()
        cp.read(self.path_of_ini, 'UTF-8')

        for i in cp.sections():
            self.dict_of_project = dict(cp.items(i))

        for i in self.dict_of_project:
            if strtobool(self.dict_of_project[i]):
                self.list_of_projects.append(i)

        return self.list_of_projects

class PppCsv:

    MODULE = 'module'
    MODULE_TYPE = 'module_type'
    MODULE_TEXT = 'module_text'
    MODULE_XLSX = 'module_xlsx'
    MODULE_DIRECTORY = 'module_directory'
    MODULE_LIST = 'module_list'
    MODULE_INDEX = 'module_index'
    MODULE_INDEX_ALL = 'module_index_all'
    MODULE_SUFFIX = 'module_suffix'
    PARAMETER = 'parameter'
    CSV_DIRECTORY = 'csv_directory'
    CSV_FILE = 'csv_file'
    KEY = 'key'
    KEY_INDEX = 'key_index'
    ITEM_INDEX_ALL = 'item_index_all'
    ITEM_INDEX = 'item_index'

    OPTION = 'option'

    path_of_moduledir = ''
    index_of_module = ''
    path_of_modulelist = ''

    def __init__(self):
        self.path_of_ppini = ''
        self.dict_of_ppini = {}
        self.dict_of_module = {}
        self.dict_of_key = {}
        self.dict_of_csv = {}
        self.list_of_module = []
        self.dict_of_parameter = {}
        self.path_of_csvdir = ''
        self.path_of_csvfile = ''
        self.index_of_key = ''
        self.flag_of_itemsall = False
        self.path_of_csv = ''
        self.index_of_item = ''
        self.index_of_items = []
        self.type_of_module = ''
        self.index_of_suffix = ''
        self.flag_of_module = False
        self.dict_of_option = {}

    def import_module_type(self):
        self.type_of_module = self.dict_of_ppini[self.MODULE_TYPE][self.MODULE_TYPE]

    def import_module_text(self):
        self.dict_of_module = self.dict_of_ppini[self.MODULE_TEXT]
        self.path_of_moduledir = self.dict_of_module[self.MODULE_DIRECTORY]
        self.path_of_modulelist = self.dict_of_module[self.MODULE_LIST]
        self.index_of_module = self.dict_of_module[self.MODULE_INDEX]

        self.path_of_modulelist = os.path.join(self.path_of_moduledir, self.path_of_modulelist)

        self.dict_of_option = self.dict_of_ppini[self.OPTION]

    def import_module_xlsx(self):
        self.dict_of_module = self.dict_of_ppini[self.MODULE_XLSX]
        self.path_of_moduledir = self.dict_of_module[self.MODULE_DIRECTORY]
        self.path_of_modulelist = self.dict_of_module[self.MODULE_LIST]
        self.index_of_module = self.dict_of_module[self.MODULE_INDEX]
        self.index_of_suffix = self.dict_of_module[self.MODULE_SUFFIX]

        self.path_of_modulelist = os.path.join(self.path_of_moduledir, self.path_of_modulelist)
        self.flag_of_module = strtobool(self.dict_of_module[self.MODULE_INDEX_ALL])

        self.dict_of_option = self.dict_of_ppini[self.OPTION]

    def import_module_list(self):

        with open(self.path_of_modulelist, 'r', encoding='utf-8_sig') as f:
            module = csv.reader(f, delimiter=',')
            list_of_index = next(module)
            count_of_index = [i for i, x in enumerate(list_of_index) if x == self.index_of_module]

            if len(count_of_index) >= 2:
                print(self.index_of_key + ' is ' + str(count_of_index) + ' count from ' + self.path_of_modulelist)
                exit()

            self.list_of_module = [x[0] for x in module if x[count_of_index[0]]]

        # TYPE:TPL = ['1.tpl', '2.tpl', '3.tpl']
        # TYPE:XLSX = {'common2': {'sample3_1': '3.xlsx', 'sample3_2': '3.xlsx'}}

    def import_module_dict(self):

        list_of_xlsxpair = []
        dict_of_ps = {}

        # seirisimasyo....
        if self.flag_of_module:
            list_of_index = get_index(self.path_of_modulelist)

            for x in list_of_index:
                list_of_ppp = [[i, x] for i in list_of_index if x + self.index_of_suffix in i]
                list_of_xlsxpair.extend(list_of_ppp)

        else:
            list_of_index = [self.index_of_module.strip() for self.index_of_module in self.index_of_module.split(',')]

            for x in list_of_index:
                list_of_xlsxpair.append([x + self.index_of_suffix, x])

        for i in list_of_xlsxpair:
            dict_of_temp = get_dictionary(self.path_of_modulelist, i[0], i[1])
            dict_of_ps.update(dict_of_temp)

        self.list_of_module = {}

        for i in dict_of_ps:
            list_of_pslsx = [[v, k] for k, v in dict_of_ps[i].items()]
            self.list_of_module[i] = list_of_pslsx

    def import_csv(self):
        self.dict_of_csv = self.dict_of_ppini[self.PARAMETER]
        self.path_of_csvdir = self.dict_of_csv[self.CSV_DIRECTORY]
        self.path_of_csvfile = self.dict_of_csv[self.CSV_FILE]
        self.index_of_key = self.dict_of_csv[self.KEY_INDEX]
        self.index_of_item = self.dict_of_csv[self.ITEM_INDEX]
        self.flag_of_itemsall = strtobool(self.dict_of_csv[self.ITEM_INDEX_ALL])

        self.path_of_csv = os.path.join(self.path_of_csvdir, self.path_of_csvfile)

        if self.flag_of_itemsall:
            try:
                self.index_of_items = get_index(self.path_of_csv)

            except FileNotFoundError as er:
                print('FileNotFoundError: ', er)
                exit()

            try:
                self.index_of_items.remove(self.index_of_key)
            except ValueError as er:
                print('ValueError: ', 'check your ini parameter: ', self.ITEM_INDEX, er)
                exit()

        else:
            self.index_of_items = [x.strip() for x in self.index_of_item.split(',')]

    def import_csvdictionary(self):
        num = 0
        list_of_conv = [[] for i in range(len(self.index_of_items)) if i is i]

        with open(self.path_of_csv, 'r', encoding='utf-8_sig') as f:
            for data_of_csv in csv.DictReader(f):
                num += 1
                for i in range(len(self.index_of_items)):
                    list_of_temp = [data_of_csv[self.index_of_key], data_of_csv[self.index_of_items[i]]]
                    list_of_conv[i].append(list_of_temp)

        for i in range(len(list_of_conv)):
            self.dict_of_parameter[self.index_of_items[i]] = dict((list_of_conv[i]))

    def get_module(self, path_of_ppini):
        self.path_of_ppini = path_of_ppini
        self.get_ppini()
        self.import_module_type()

        if self.type_of_module in 'text':
            self.import_module_text()
            self.import_module_list()
        elif self.type_of_module in 'xlsx':
            self.import_module_xlsx()
            self.import_module_dict()

        self.import_csv()
        self.import_csvdictionary()

        return self.list_of_module, self.path_of_moduledir, self.dict_of_parameter, self.dict_of_option

    def get_ppini(self):
        cp = configparser.ConfigParser()
        cp.read(self.path_of_ppini, 'UTF-8')
        list_of_inisections = cp.sections()

        for i in list_of_inisections:
            self.dict_of_ppini[i] = dict(cp.items(i))

    def eof(self):
        print('Successfuly... PPP', self.path_of_csv)


def get_index(path_of_god):
    with open(path_of_god, 'r', encoding='utf-8_sig') as f:
        index_of_index = csv.reader(f, delimiter=',')
        index_of_items = next(index_of_index)

    return index_of_items


def get_dictionary(path_of_csv, index_of_conf, index_of_v):
    dict_of_conv = dict()
    num = 0
    index_of_val = []

    if type(index_of_v) is str:
        index_of_val = [x.strip() for x in index_of_v.split(',')]
    elif type(index_of_v) is list:
        index_of_val = index_of_v

    list_of_conv = [[] for i in range(len(index_of_val)) if i is i]

    with open(path_of_csv, 'r', encoding='utf-8_sig') as f:
        for d1 in csv.DictReader(f):
            num += 1
            for i2 in range(len(index_of_val)):
                tmp_list = [d1[index_of_conf], d1[index_of_val[i2]]]
                list_of_conv[i2].append(tmp_list)

    for i in range(len(list_of_conv)):
        dict_of_conv[index_of_val[i]] = dict((list_of_conv[i]))

    return dict_of_conv
