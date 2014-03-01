""" 
A simple application denoting how to make abstract classes in python
"""

from abc import ABCMeta, abstractmethod
class Shape(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def area(self):
        raise NotImplementedError("Implement area method")
    
    @abstractmethod
    def perimeter(self):
        raise NotImplementedError("Implement area method")
    
class Rectangle(Shape):
    length, width = None, None
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    """ 
    overriding area function
    """    
    def area(self):                        
        print self.length * self.width
    
    """ 
    overriding permimeter function
    """
    def perimeter(self):
        print 2*(self.length + self.width)
    
class Circle(Shape):
    radius = None
    
    """ 
    constructor of Circle
    """
    def __init__(self, radius):
        self.radius = radius        
    
    """ 
    overriding area function
    """
    def area(self):
        print 3.14*(self.radius**2)
    
    """ 
    overriding permimeter function
    """
    def perimeter(self):
        print (2 * 3.14 * self.radius)    
    
""" 
main function
"""      
if __name__ == '__main__':
    r = Rectangle(3,4)
    r.area()
    r.perimeter()
    
    c = Circle(2)
    c.area()
    c.perimeter()


