class PurchaseOrder:
    def __init__(self):
        self.purchaseOrderId   = ""           #주문ID
        self.purchaseOrderDate = ""           #주문날짜
        self.purchaseOrderSupplierName = ""   #거래처
        self.purchaseOrderSupplierType = ""   #거래처번호
        self.purchaseOrderItemList     = []   #거래품목
        self.purchaseOrderPrice   = 0         #주문가격
        self.purchaseOrderMemo    = ""        #메모

    def __str__ (self):
        return '({}, {}, {}, {}, {}, {}, {})'.format(
            self.purchaseOrderId, 
            self.purchaseOrderDate,
            self.purchaseOrderSupplierName,
            self.purchaseOrderSupplierType,
            self.purchaseOrderItemList,    
            self.purchaseOrderPrice,
            self.purchaseOrderMemo)

    def __repr__ (self):
        return str(vars(self))
        
class PurchaseOrderItem:
    def __init__(self):
        self.purchaseItemId         = "" #품목ID
        self.purchaseItemName       = "" #품목이름
        self.purchaseItemUnitAmount = "" #품목단위총량
        self.purchaseItemUnit       = "" #품목단위
        self.purchaseItemAmount     = "" #주문개수
        self.purchaseItemPrice      = 0  #가격
        self.purchaseItemMemo       = "" #메모
    
    def __repr__ (self):
        return str(vars(self))
        # '({}, {}, {}, {}, {}, {}, {})'.format(
        # self.purchaseItemId,  
        # self.purchaseItemName,
        # self.purchaseItemUnitAmount,
        # self.purchaseItemUnit,
        # self.purchaseItemAmount,
        # self.purchaseItemPrice,
        # self.purchaseItemMemo)
