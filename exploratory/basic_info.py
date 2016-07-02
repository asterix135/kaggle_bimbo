"""
Run from command line with file name as argument
"""

import sys
import csv

def file_len(fname):
    """
    Prints file length
    """
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def check_csv_consistency(fname):
    """
    Checks to ensure that all rows are same number of elements
    """
    row_lengths = {}
    csv_file = csv.reader(open(fname, 'r'), delimiter=',')
    for row in csv_file:
        if len(row) in row_lengths:
            row_lengths[len(row)] += 1
        else:
            row_lengths[len(row)] = 1
    return row_lengths


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            print('File length: ', file_len(sys.argv[1]), 'lines')
            row_lengths = check_csv_consistency(sys.argv[1])
            for row_length in row_lengths:
                print('Row length: ', row_length,
                      "; count: ", row_lengths[row_length])
        except:
            print('Invalid file name')




