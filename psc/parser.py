"""
This code creates a parser that can parse the fixed width file and generate a
delimited file, e.g. CSV format
"""

import csv
import numpy as np


class Parser:
    """
    This is a class for decoding on windows-1252 encoded files.

    """

    def __init__(self):
        """
        The constructor for parser class.
        Parameters: column names, offset as column data lengths,
        encoding methods for read and write files.
        """
        self.col_names = ['f1', 'f2', 'f3', 'f4', 'f5', \
                          'f6', 'f7', 'f8', 'f9', 'f10']
        self.offsets = ['5', '12', '3', '2', '13', \
                        '7', '10', '13', '20', '13']
        self.indices = [0] + list(np.cumsum([int(x) for x in self.offsets]))
        self.row_list = list()
        self.row_list.append(self.col_names)
        self.read_encoding = 'cp1252'
        self.write_encoding = 'utf-8'
        #self.IncludeHeader = "True"

    def read_data(self, read_file_name):
        """
        The function to read the windows-1252 encoded files

        Parameters:
        read_file_name (string): The file name where the data is stored

        Returns:
        data (string): Data in string format

        """

        with open(read_file_name, 'r', \
                  encoding=self.read_encoding) as file_:
            data = file_.read()

        return data

    def parse_data(self, data):
        """
        The function to Parse the constant width columnar data
        into utf-8 encoded file

        Parameters:
        data (string)

        Returns:
        row_list (list): list of lists of rows
        """

        num_lines = (int(len(data)/self.indices[-1]) \
                          if len(data)%self.indices[-1] == 0 \
                          else 1 + int(len(data)/self.indices[-1]))

        for i in range(num_lines):
            line_item = []
            for ind in range(len(self.col_names)):
                new_item = data[(i*self.indices[-1]) + \
                                     self.indices[ind]: \
                                     (i*self.indices[-1]) + \
                                     self.indices[ind+1]]

                line_item.append(new_item)

            self.row_list.append(line_item)
        return self.row_list

    def write_data(self, write_file_name):
        """
        The function to write the constant width columnar data
        into utf-8 encoded file

        Parameters:
        write_file_name (string): The file name where the data is written
        """

        with open(write_file_name, 'w', newline='\n', \
                  encoding=self.write_encoding) as file_:
            writer = csv.writer(file_)
            writer.writerows(self.row_list)
