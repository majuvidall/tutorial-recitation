# Sample python File

class RetailItem:
    
    def __init__(self,itemtype,itemamount,price):
        self.__itemtype = itemtype
        self.__itemamount = itemamount
        self.__price = price

    def __str__(self):
        a = '{:<20}{:^10}${:<10.2f}'.format(self.__itemtype,self.__itemamount,self.__price)
        return a
    


