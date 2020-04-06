#!/usr/bin/env python3

##
# Convert from Excel XLSX format to Unicode Separated Values (USV)
#
# Syntax: 
#
#     excel-xlsx-to-usv <file-name> [sheet-name]
#
# Example:
#
#     excel-xlsx-to-usv example.xlsx Sheet1
#
# Output is USV:
#
#   * “␟” U+241F Symbol For Unit Separator Unicode Character
#
#   * “␞” U+241E Symbol For Record Separator Unicode Character
##

import pandas
import argparse

parser = argparse.ArgumentParser(description='Process an Excel file to output tab separated values (TSV)')
parser.add_argument('input_excel_file_name', type=str, help='Input Excel file name such as "example.xlsx"')
parser.add_argument('input_excel_sheet_name', type=str, nargs='?', default='Sheet1', help='Input Excel sheet name such as "Sheet1"')
args = parser.parse_args()

data = pandas.read_excel(args.input_excel_file_name, args.input_excel_sheet_name, index_col=None)
data = data.replace('[\t\r\n]+', ' ', regex=True)
print(data.to_csv(encoding='utf-8', index=False, line_terminator='␞', sep='␟'))
