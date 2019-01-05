# -*- coding: utf-8 -*-

import os
import openpyxl
from copy import copy
from openpyxl.utils import column_index_from_string


class ExecPslsx:

    def __init__(self, dict_of_module, path_of_module, dict_of_parameter, dict_of_option):
        self.dict_of_module = dict_of_module
        self.path_of_module = path_of_module
        self.dict_of_parameter = dict_of_parameter
        self.dict_of_option = dict_of_option

        self.list_of_keys = []
        self.path_of_outputdir = ''
        self.key_of_templatestr = ''

        self.num_of_space = int(self.dict_of_option['option_rowspace'])

    def get_outputpath(self):
        self.key_of_templatestr = list(self.dict_of_parameter.keys())[0]
        self.path_of_outputdir = os.path.join(os.path.dirname(self.path_of_module), 'output', self.key_of_templatestr)
        os.makedirs(self.path_of_outputdir, exist_ok=True)

    def get_keys(self):
        self.list_of_keys = list(self.dict_of_module.keys())

    def get_spacerow(self):
        self.num_of_space = 0

    def get_template(self):

        to_wb = openpyxl.Workbook()

        for listkey in self.list_of_keys:
            to_wb.create_sheet(title=listkey)
            to_ws = to_wb[listkey]

            position_row = 0

            for i2 in self.dict_of_module[listkey]:

                path_of_wb = os.path.join(self.path_of_module, i2[0])
                wb = openpyxl.load_workbook(path_of_wb)
                ws = wb[i2[1]]

                nrow = ws.min_row
                xrow = ws.max_row

                for key, x in enumerate(ws.rows):

                    for ind, source_cell in enumerate(x):
                        dest_cell = to_ws[source_cell.coordinate]

                        num_of_row = dest_cell.row + position_row
                        num_of_column = column_index_from_string(dest_cell.column)

                        dest_cell = to_ws.cell(row=num_of_row, column=num_of_column)
                        dest_cell.value = source_cell.value

                        if source_cell.has_style:
                            dest_cell.font = copy(source_cell.font)
                            dest_cell.border = copy(source_cell.border)
                            dest_cell.fill = copy(source_cell.fill)
                            dest_cell.alignment = copy(source_cell.alignment)
                            dest_cell.number_format = copy(source_cell.number_format)
                            dest_cell.protection = copy(source_cell.protection)

                position_row += xrow - nrow + 1 + self.num_of_space

        to_wb.remove_sheet(to_wb.get_sheet_by_name('Sheet'))
        to_wb.save(os.path.join(self.path_of_outputdir, self.key_of_templatestr + '.xlsx'))
