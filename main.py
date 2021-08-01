""" Main driver module """

import sys

from lot import input_parser

infile = sys.argv[1]
outfile = sys.argv[2]
print(f'Input File Path: {infile}')
print(f'Output File Path: {outfile}')

parser2 = input_parser.InputParser()
parser2.run(infile, outfile)
