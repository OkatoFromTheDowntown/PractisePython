import xlrd 
import xlwt # doesn't work on .xlsx
import xlutils # doesn't work on .xlsx

# open .xlsx
book = xlrd.open_workbook(r'target.xlsx')
print('The number of sheets: %d' % book.nsheets)
print('The name of sheets: %s' % book.sheet_names())

# get sheets info
for index in range(book.nsheets):
  sh = book.sheet_by_index(index)
  print('Name: {0} Rows: {1} Cols: {2}'.format(sh.name, sh.nrows, sh.ncols))

# full loop all sheets
for sh in book.sheets():
  print(r'>>>>>>{0}<<<<<<'.format(sh.name))
  for row in range(sh.nrows):
    values = []
    # print(sh.row(row))
    for col in range(sh.ncols):
      cell = sh.cell(row, col)
      # print(cell, cell.ctype, xlrd.empty_cell.ctype, cell is xlrd.empty_cell)
      # if not cell is xlrd.empty_cell: # Always False
      if not cell.ctype in (xlrd.XL_CELL_BLANK, xlrd.XL_CELL_EMPTY):
        # values.append(sh.cell(row, col).value)
        values.append(cell.value)
      # print(xlrd.cellname(row, col))
    print(values)
  print()
  
    