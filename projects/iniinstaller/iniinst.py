import configparser
import os


class IniInstall:
    def __init__(self, arg1):
        if os.path.exists(arg1):
            print('ini path check...OK: ' + arg1)
            self.arg1 = arg1
        else:
            print('ini path check...NG: ' + arg1)
            exit()

    def read_ini(self):
        date_of_ini = configparser.ConfigParser()
        date_of_ini.read(self.arg1, 'UTF-8')
        list_of_inisection = date_of_ini.sections()
        dict_of_ini = {}

        for i in list_of_inisection:
            dict_of_ini[i] = dict(date_of_ini.items(i))

        return dict_of_ini
