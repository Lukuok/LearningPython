class PurchaseOrderItem:
    def __init__(self):
        self.__purchaseItemId         = ""
        self.__purchaseItemUnitAmount = ""
        self.__purchaseItemUnit       = ""
        self.__purchaseItemAmount    = ""
        self.__purchaseItemPrice     = 0
        self.__purchaseItemMemo      = 0

    def getPurchaseItemId(self):
        return self.__purchaseItemId
    
    def setPurchaseItemId(self, purchaseItemId):
        self.__purchaseItemId = purchaseItemId
        
    def getPurchaseItemUnitAmount(self):
        return self.__purchaseItemUnitAmount
    
    def setPurchaseItemUnitAmount(self, purchaseItemUnitAmount):
        self.__purchaseItemUnitAmount = purchaseItemUnitAmount
        
    def getPurchaseItemUnit(self):
        return self.__purchaseItemUnit
    
    def setPurchaseItemUnit(self, purchaseItemUnit):
        self.__purchaseItemUnit = purchaseItemUnit

    def getPurchaseItemAmount(self):
        return self.__purchaseItemAmount
    
    def setPurchaseItemAmount(self, purchaseItemUnit):
        self.__purchaseItemAmount = purchaseItemUnit

    def getPurchaseItemUnit(self):
        return self.__purchaseItemPrice
    
    def setPurchaseItemUnit(self, purchaseItemUnit):
        self.__purchaseItemPrice = purchaseItemUnit
        
    def getPurchaseItemMemo(self):
        return self.__purchaseItemMemo
    
    def setPurchaseItemMemo(self, purchaseItemMemo):
        self.__purchaseItemMemo = purchaseItemMemo