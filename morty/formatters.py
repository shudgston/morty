import csv
import sys
from prettytable import PrettyTable


class Formatter:

    def __init__(self, data, header):
        self.data = data
        self.header = header

    def write(self):
        raise NotImplemented()


class TableFormatter(Formatter):

    def __init__(self, data, header):
        super().__init__(data, header)
        table = PrettyTable(header)
        table.header_style = 'upper'
        table.align = 'r'
        self.table = table

    def write(self):
        for row in self.data:
            self.table.add_row(row)
        print(self.table)


class CSVFormatter(Formatter):

    def __init__(self, data, header):
        super().__init__(data, header)
        self.writer = csv.writer(sys.stdout)

    def write(self):
        rows = [self.header]
        rows.extend(self.data)
        for row in rows:
            self.writer.writerow(row)
