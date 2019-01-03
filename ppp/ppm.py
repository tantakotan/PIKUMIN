import os

INIDIR = 'ini/'

class PpmExe:
    path_of_ppexe = ''
    path_of_ppini = ''
    def __init__(self, projectname, path_of_project):
        self.path_of_ppexe = os.path.join(path_of_project, projectname + '.py')
        self.path_of_ppini = os.path.join(path_of_project, INIDIR, projectname + '.ini')
        print(self.path_of_ppexe, self.path_of_ppini)

    def import_ini(self):
        return self.path_of_ppini