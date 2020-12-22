class PurchaseOrder:
    def __init__(self):
        self.__purchaseOrderId   = ""
        self.__purchaseOrderDate = ""
        self.__purchaseOrderSupplierName = ""
        self.__purchaseOrderSupplierType = ""
        self.__purchaseOrderItemList     = []
        self.__purchaseOrderPrice   = 0
        self.__purchaseOrderMemo    = ""
        
    def getPurchaseOrderId(self):
        return self.__purchaseOrderId
    
    def setPurchaseOrderId(self, purchaseOrderId):
        self.__purchaseOrderId = purchaseOrderId
        
    def getPurchaseOrderDate(self):
        return self.__purchaseOrderDate
    
    def setPurchaseOrderDate(self, purchaseOrderDate):
        self.__purchaseOrderDate = purchaseOrderDate

    def getPurchaseOrderSupplierName(self):
        return self.__purchaseOrderSupplierName
    
    def setPurchaseOrderSupplierName(self, purchaseOrderSupplierType):
        self.__purchaseOrderSupplierName = purchaseOrderSupplierType
        
    def getPurchaseOrderSupplierType(self):
        return self.__purchaseOrderSupplierType
    
    def setPurchaseOrderSupplierType(self, purchaseOrderSupplierType):
        self.__purchaseOrderSupplierType = purchaseOrderSupplierType
        
    def getPurchaseOrderItemList(self):
        return self.__purchaseOrderItemList
    
    def setPurchaseOrderItemList(self, purchaseOrderItemList):
        self.__purchaseOrderItemList = purchaseOrderItemList
        
    def getPurchaseOrderPrice(self):
        return self.__purchaseOrderPrice
    
    def setPurchaseOrderPrice(self, purchaseOrderPrice):
        self.__purchaseOrderPrice = purchaseOrderPrice
        
    def getPurchaseOrderMemo(self):
        return self.__purchaseOrderMemo
    
    def setPurchaseOrderMemo(self, purchaseOrderMemo):
        self.__purchaseOrderMemo = purchaseOrderMemo
        