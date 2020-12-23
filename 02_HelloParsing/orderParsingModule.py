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
    order.purchaseOrderDate = csvContent[2][3][0:8]
    order.purchaseOrderSupplierName = "KCC"  #임의값
    order.purchaseOrderSupplierType = 0      #임의값

    item = None
    for rowIdx in range(12, len(csvContent)):
        
        if (rowIdx%2 == 0 and csvContent[rowIdx][2] != ''):
            item = PurchaseOrderItem()
            item.purchaseItemId     = csvContent[rowIdx][2].split(' ] ')[0][2:]
            item.purchaseItemName   = csvContent[rowIdx][2].split(' ] ')[1]
        if (rowIdx%2 == 1 and csvContent[rowIdx][9] != ''):
            item.purchaseItemUnitAmount = csvContent[rowIdx][9]
            item.purchaseItemUnit   = csvContent[rowIdx][10]
            item.purchaseItemAmount = csvContent[rowIdx][11]
            item.purchaseItemPrice  = csvContent[rowIdx][14]
            item.purchaseItemMemo   = csvContent[rowIdx][17]
            order.purchaseOrderPrice += int(float(item.purchaseItemPrice))
            order.purchaseOrderItemList.append(item);

    return order;

def string2ObjectFor3M(eocContent):

    preOrderId = ''
    nowOrderId = ''
    orderList = []
    order = None
    item  = None

    for rowIdx in range(1, len(eocContent)):
        nowOrderId = eocContent[rowIdx][10]

        if (preOrderId != nowOrderId):
            if(rowIdx != 1): 
                orderList.append(order)

            preOrderId = eocContent[rowIdx][10];

            order = PurchaseOrder()
            order.purchaseOrderId    = eocContent[rowIdx][10];
            order.purchaseOrderDate  = eocContent[rowIdx][11];
            order.purchaseOrderPrice = eocContent[rowIdx][12];

        item = PurchaseOrderItem()
        item.purchaseItemId   = eocContent[rowIdx][20];
        item.purchaseItemName = eocContent[rowIdx][24];
        item.purchaseItemUnit = eocContent[rowIdx][27];
        item.purchaseItemUnitAmount = 0;
        item.purchaseItemAmount = eocContent[rowIdx][26];
        item.purchaseItemPrice  = eocContent[rowIdx][28];
        order.purchaseOrderItemList.append(item)

        if(rowIdx == len(eocContent)): 
            orderList.append(order)

    return orderList