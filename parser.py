"""
This code creates a parser that can parse the fixed width file and generate a
delimited file, e.g. CSV format
"""

import os, csv, sys
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

def main():
    
 
    #input_file = input('Please enter input file name:\n')
 
    #output_file = input('Please enter output file name:\n')
    input_file = os.environ['input_file']
    output_file = os.environ['output_file']
    """
    os.environ[env_var] = env_var_value    
    try:
        input_file = argv[1]
        output_file = argv[2]
    except IndexError:
        print('Error: There must be at least 3 arguments, ')
        print('example: python parser.py input.txt output.csv') 
        return None
    
    """
    parse = Parser()
    data = parse.read_data(input_file)

    try:
        data = parse.read_data(input_file)
    except FileNotFoundError:
        print('Error: No such file. Make sure to have your file!')
        return None
    
    parse.parse_data(data)

    
    if not output_file.endswith('.csv'):
        output_file+='.csv'

    output_path = os.getcwd()
    output_path = os.path.join(output_path, output_file)

    parse.write_data(output_path)
    print('Text data parsed successfully!')

if __name__ == "__main__":
    print(f'current folder={os.getcwd()}')
    main()
