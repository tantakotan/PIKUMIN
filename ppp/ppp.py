# -*- coding: utf-8 -*-

import configparser
from distutils.util import strtobool
import os
import glob
import csv


class PppExe:

    path_of_exe = ''
    path_of_exedir = ''
    path_of_ini = ''
    path_of_projects = ''
    dict_of_ini = {}
    list_of_projects = []

    def __init__(self, path_of_exe):
        print('Starting... PPP')
        self.path_of_exe = path_of_exe
        self.path_of_exedir = os.path.dirname(path_of_exe)
        self.path_of_project = ''

    def import_ini(self):
        path_of_ini, trashbox = os.path.splitext(self.path_of_exe)
        self.path_of_ini = path_of_ini + '.ini'

    def import_projects(self):
        self.path_of_project = self.path_of_exedir + '/projects/'
        list_of_ap = glob.glob(self.path_of_project + '*.py')

        for x in list_of_ap:
            x = os.path.basename(x)
            i = x.split('.')[0]
            if i != '__init__':
                self.list_of_projects.append(i)

        return self.list_of_projects, self.path_of_project


class PppCsv:

    MODULE = 'module'
    MODULE_DIRECTORY = 'module_directory'
    MODULE_LIST = 'module_list'
    MODULE_INDEX = 'module_index'
    CSV = 'csv'
    CSV_DIRECTORY = 'csv_directory'
    CSV_FILE = 'csv_file'
    KEY = 'key'
    KEY_INDEX = 'key_index'
    ITEM_INDEX_ALL = 'item_index_all'
    ITEM_INDEX = 'item_index'

    path_of_moduledir = ''
    index_of_module = ''
    path_of_modulefile = ''

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

    def import_module(self):
        self.dict_of_module = self.dict_of_ppini[self.MODULE]
        self.path_of_moduledir = self.dict_of_module[self.MODULE_DIRECTORY]
        self.index_of_module = self.dict_of_module[self.MODULE_INDEX]
        self.path_of_modulefile = self.dict_of_module[self.MODULE_LIST]

        self.path_of_modulefile = os.path.join(self.path_of_moduledir, self.path_of_modulefile)

    def import_modulelist(self):

        with open(self.path_of_modulefile, 'r', encoding='utf-8_sig') as f:
            module = csv.reader(f, delimiter=',')
            list_of_index = next(module)
            count_of_index = [i for i, x in enumerate(list_of_index) if x == self.index_of_module]

            if len(count_of_index) >= 2:
                print(self.index_of_key + ' is ' + str(count_of_index) + ' count from ' + self.path_of_modulefile)
                exit()

            self.list_of_module = [x[0] for x in module if x[count_of_index[0]]]

    def import_csv(self):
        self.dict_of_csv = self.dict_of_ppini[self.CSV]
        self.path_of_csvdir = self.dict_of_csv[self.CSV_DIRECTORY]
        self.path_of_csvfile = self.dict_of_csv[self.CSV_FILE]
        self.index_of_key = self.dict_of_csv[self.KEY_INDEX]
        self.index_of_item = self.dict_of_csv[self.ITEM_INDEX]
        self.flag_of_itemsall = strtobool(self.dict_of_csv[self.ITEM_INDEX_ALL])

        self.path_of_csv = os.path.join(self.path_of_csvdir, self.path_of_csvfile)

        if self.flag_of_itemsall:
            try:
                self.get_index(self.path_of_csv)

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
        self.import_module()
        self.import_modulelist()
        self.import_csv()
        self.import_csvdictionary()

        return self.list_of_module, self.path_of_moduledir, self.dict_of_module

    def get_index(self, path_of_god):
        with open(path_of_god, 'r', encoding='utf-8_sig') as f:
            index_of_index = csv.reader(f, delimiter=',')
            self.index_of_items = next(index_of_index)

    def get_ppini(self):
        cp = configparser.ConfigParser()
        cp.read(self.path_of_ppini, 'UTF-8')
        list_of_inisections = cp.sections()

        for i in list_of_inisections:
            self.dict_of_ppini[i] = dict(cp.items(i))
