import os
import pathlib
from importlib import machinery

INIDIR = 'ini/'


class PpmExe:

    path_of_ppexe = ''
    path_of_ppini = ''
    name_of_project = ''

    def __init__(self, projectname, path_of_project):
        self.path_of_ppexe = os.path.join(path_of_project, projectname + '.py')
        self.path_of_ppini = os.path.join(path_of_project, INIDIR, projectname + '.ini')
        self.name_of_project = projectname
        self.path_of_ppimport = ''

    def import_ppini(self):
        return self.path_of_ppini

    def start_project(self, list_of_module, path_of_module, dict_of_parameter, dict_of_option):
        print('Starting... PPM: ', self.path_of_ppexe)

        self.format_path()
        self.import_pymodule()
        self.ppexe.ExecPykumin(list_of_module, path_of_module, dict_of_parameter, dict_of_option)

        print('Successfully... PPM: ', self.path_of_ppexe)
        print('''--------------------''')

    def format_path(self):
        p = pathlib.Path(self.path_of_ppexe)
        self.path_of_ppimport = str(p.relative_to(p.cwd()))

    def import_pymodule(self):
        ppexe = machinery.SourceFileLoader('project', self.path_of_ppimport)
        self.ppexe = ppexe.load_module()
