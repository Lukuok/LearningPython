import xlrd

# 읽기 라이브러리를 통해 현재 같은 디렉터리상에 있는 test.xls를 불러와 workbook에 할당합니다.
workbook = xlrd.open_workbook('excel/report.xls')

# 워크북에 할당된 엑셀 데이터의 첫번째시트를 불러옵니다.
worksheet = workbook.sheet_by_index(0)

# nrows에 불러온 첫번째 시트의 행수를 불러옵니다.
totalRows = worksheet.nrows

orderNo   = worksheet.cell_value(2,3)
orderDate = worksheet.cell_value(4,15)
area      = worksheet.cell_value(5,4)
print(orderNo, orderDate, area)
print(totalRows)
print()

# 불러온 데이터를 저장할 딕셔너리를 선언합니다.
# datadict = {}

# # 행수만큼의 for loop 를 돌려서 행단위로 데이터를 불러와 datadict에 저장합니다.
# for row_num in range(nrows):
#     datadict[row_num] = {}
#     # field_cnt는 열의 개수입니다. 열갯수는 여러분이 지정하시면 됩니다.
#     for col in range(field_cnt):
#         # datadict[row_num]에 열숫자별로 셀데이터를 저장합니다.
#         datadict[row_num][col] = worksheet.cell_value(row_num, col)

for rowIdx in range(12,totalRows):
    if rowIdx%2 == 0 and worksheet.cell_value(rowIdx,2) != '':
        print(worksheet.cell_value(rowIdx,2))
    if rowIdx%2 == 1 and worksheet.cell_value(rowIdx,9) != '':
        print(worksheet.cell_value(rowIdx,9))
        print(worksheet.cell_value(rowIdx,10))
        print(worksheet.cell_value(rowIdx,11))
        print(worksheet.cell_value(rowIdx,14))
        print(worksheet.cell_value(rowIdx,17))
        print()
# for row_num in range(nrows):
#     datadict[row_num] = {}
#     # field_cnt는 열의 개수입니다. 열갯수는 여러분이 지정하시면 됩니다.
#     for col in range(field_cnt):
#         # datadict[row_num]에 열숫자별로 셀데이터를 저장합니다.
#         datadict[row_num][col] = worksheet.cell_value(row_num, col)
