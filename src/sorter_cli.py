from sorter_api import Sorter
import sys

sort_type = sys.argv[1]
sort_order = sys.argv[2]
filename = sys.argv[3]
output_filename = sys.argv[4]

Sorter(filename, sort_type, sort_order)
if sort_type == int:
    output_filename = sort_nums(filename)
if sort_type == str:
    output_filename = sort_strings(filename)