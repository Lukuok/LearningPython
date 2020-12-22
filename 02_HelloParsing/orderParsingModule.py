import xlrd  
import csv 
from purchaseOrder import PurchaseOrder, PurchaseOrderItem

def xls2Csv(srcFilePath, desFilePath):
    sheet = xlrd.open_workbook(srcFilePath).sheet_by_index(0) 
    col = csv.writer(open(desFilePath, 'w', encoding='UTF-8', newline="")) 
    
    for row in range(sheet.nrows): 
        col.writerow(sheet.row_values(row))
        
def csv2String(csvFilePath, parseString):
    csvFile = open(csvFilePath, 'r', encoding='UTF-8')
    csvReader = csv.reader(csvFile, delimiter = parseString)
    csvContent = list(csvReader)
    csvFile.close()
    
    return csvContent

def eoc2String(eocFilePath, parseString):
    eocFile = open(eocFilePath, 'r', encoding='UTF-16')
    eocReader = csv.reader(eocFile, delimiter = parseString)
    eocContent = list(eocReader)
    eocFile.close()
    
    return eocContent

def string2ObjectForKCC(csvContent):
    order = PurchaseOrder()
    order.purchaseOrderId   = csvContent[2][3]
    order.purchaseOrderDate = csvContent[4][5]
    order.purchaseOrderSupplierName = "KCC"  #임의값
    order.purchaseOrderSupplierType = 0      #임의값
    for rowIdx in range(12, len(csvContent)):
        item = PurchaseOrderItem()
        print(rowIdx)
        if rowIdx%2 == 0 and csvContent[rowIdx][2] != '':
            item.purchaseItemId     = csvContent[rowIdx][2]
            item.purchaseItemName   = csvContent[rowIdx][2]
        if rowIdx%2 == 1 and csvContent[rowIdx][9] != '':
            item.purchaseItemUnitAmount = csvContent[rowIdx][9]
            item.purchaseItemUnit   = csvContent[rowIdx][10]
            item.purchaseItemAmount = csvContent[rowIdx][11]
            item.purchaseItemPrice  = csvContent[rowIdx][14]
            item.purchaseItemMemo   = csvContent[rowIdx][17]
            order.purchaseOrderPrice += int(float(item.purchaseItemPrice))
            order.purchaseOrderItemList.append(item);

def string2ObjectFor3M(eocContent):
    order = PurchaseOrder()
    order.purchaseOrderId