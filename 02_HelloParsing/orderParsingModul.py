import xlrd  
import csv 

def xls2Csv(srcFile, desFile):
    # open workbook by sheet index, 
    # optional - sheet_by_index() 
    sheet = xlrd.open_workbook(srcFile).sheet_by_index(0) 
    
    # writer object is created 
    col = csv.writer(open(desFile, 'w', newline="")) 
    
    # writing the data into csv file 
    for row in range(sheet.nrows): 
        col.writerow(sheet.row_values(row))
        
def csv2ObjectForKCC(csvFile):
    csv.reader()
    
def txt2ObjectFor3M(txtFile):