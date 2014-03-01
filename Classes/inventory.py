"""
Simple python application for maintaining the product list in the inventory
"""

class product:
    price, id, quantity = None, None, None
    
    """
    constructor for product class
    """    
    def __init__(self, price, id, quantity):
        self.price = price        
        self.id = id
        self.quantity = quantity
        
    """ 
    update price function
    """    
    def update_price(self, price):
        self.price = price
    
    """ 
    update quantity function
    """    
    def update_quantity(self,quantity):
        self.quantity = quantity
    
    """ 
    print product function
    """    
    def print_product(self):
        print "id is %d\nprice is %.2f\nquantity is %d\n" % (self.id, self.price, self.quantity)

class Inventory:
    
    """ 
    constructor for inventory class
    """    
    def __init__(self):
        self.product_list = []
        
    """ 
    add product function
    """    
    def add_product(self,product):
        self.product_list.append(product)
    
    """ 
    remove product function
    """    
    def remove_product(self,product):       
        self.product_list.remove(product)
        
    """ 
    print inventory function
    """    
    def print_inventory(self): 
        total= 0.0      
        for p in self.product_list:  
            total+= p.quantity * p.price
            print p.print_product()
        print "total is %.2f" % total
    
""" 
main function
"""    
if __name__ == '__main__':
    p1 = product(1.4, 123, 5)
    p2 = product(1, 3432, 100)
    p3 = product(100.4, 2342, 99)
    
    I = Inventory()
    I.add_product(p1)
    I.add_product(p2)
    I.add_product(p3)
    
    I.print_inventory()








