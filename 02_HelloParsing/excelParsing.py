import xlsxwriter

 

# Create an new Excel file and add a worksheet. ( filename = test.xlsx )
# test.xlsx 라는 엑셀 파일 생성 후 오픈

workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet()



# Make cell_format which we need with setting that we want
# cell_format 만들어두기 (나중에 여러번 사용할 것을 대비하여)

cell_format = workbook.add_format({'border': 1})
cell_format2 = workbook.add_format({'border': 1})
cell_format2.set_bold(1)



# Widen the first column to make the text clearer. ( A~A column )
# A 열부터 A 열까지 너비를 20으로 세팅

worksheet.set_column('A:A', 20)



# Add a bold format to use to highlight cells.
# cell_boldform 변수를 글씨 굵게 셀 세팅으로 설정

cell_boldform = workbook.add_format({'bold': True})



# Write some simple text.
# A1 셀에 Hello 입력

worksheet.write('A1', 'Hello')



# Set background color.
# 셀의 배경 색을 세팅 - 괄호 안의 내용은 구글에 검색하면 원하는 색의 값을 알 수 있음

cell_format.set_bg_color('#CECECE')



# Text with formatting.
# A2 셀에 cell_boldform 포맷으로 World 입력 (위에 굵게로 세팅하였음)

worksheet.write('A2', 'World', cell_boldform)



# Write some numbers, with row/column notation.
# 행, 열, 내용 >> 쓰기

worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)



# Insert an image.
# 해당 셀에 이미지 파일 넣기

#worksheet.insert_image('B5', 'picture_test.png')



# save and close excel file.
# 저장 후 엑셀 파일 닫기

workbook.close()



# And so on
# 기타 참고 예시

cell_format = workbook.add_format({'align': 'center', 'valign': 'vcentoer', 'border': 1})
cell_format.set_font_color('red')
cell_format = workbook.add_format({'bold': True, 'font_color': 'red'})
worksheet.set_row(0, 18, cell_format)
worksheet.set_column('A:D', 20, cell_format)