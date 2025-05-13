
import random
class Receipt(object):

    def __init__(self, retailer=None, purchase_date=None, purchase_time=None, items=None, total=None, id=None): 
        self.id = None
        self.retailer = retailer
        self.purchase_date = purchase_date
        self.purchase_time = purchase_time
        self.items = items
        self.total = total


    def get_retailer(self):
        return self._retailer

    def set_retailer(self, retailer):
        self._retailer = retailer


    def get_purchase_date(self):
        return self._purchase_date

    def set_purchase_date(self, purchase_date):
        self._purchase_date = purchase_date

    def get_purchase_time(self):
        return self._purchase_time

    def set_purchase_time(self, purchase_time):
        self._purchase_time = purchase_time

    def get_items(self):
        return self._items

    def set_items(self, items):
        self._items = items

    def get_total(self):
        return self._total

    def set_total(self, total):
        self._total = total

    def process(self):
        chars=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        rand=random.choices(chars,k=32)
        r=''.join(rand)
        self.id = r[:8] + "-" + r[8:12] + "-" + r[12:16] + "-" + r[16:20] + "-" + r[20:]
        return self.id

    def name_len(self):
        i=0
        count=0
        while (i <len(self._retailer)):
            if(self._retailer[i].isalnum()):
                count+=1
            i+=1
        return count
            
    def round_dollar(self):
        flt=float(self.total)
        if(flt-int(flt)==0):
            return 50
        return 0
        
    def total_multiple(self):
        ft=float(self.total)
        if(flt%0.25==0.0):
            return 25
        return 0
        
    def two_items(self):
        pairs=int(len(self._items)/2)
        return 5*pairs
        
    def item_len(self):
        i=0
        points=0
        while(i<len(self._items)):
            if(len(self._items[i].short_description)%3==0):
                points+=-1*((self._items[i].price*0.2)//-1)
            i+=1
        return points
        
    def odd_day(self):
        day=int(self.purchase_date[-2:])
        if(day%2!=0):
            return 6
        return 0
        
    def time_check(self):
        convert_time=int(self.purchase_time[0:2]+self.purchase_time[3:])
        if(convert_time>200 and convert_time<400):
            return 10
        return 0
