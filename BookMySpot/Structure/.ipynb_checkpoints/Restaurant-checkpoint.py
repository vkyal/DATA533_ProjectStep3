# Module 3 Restaurant
#from .Table import Table 

class Restaurant():
    def __init__(self,name ='NA',
                 location='NA',
                 cuisine='NA',
                 maplink='NA',
                 cust_rating='NA',
                 cust_num='NA'):
        self.name = name
        self.location = location
        self.cuisine = cuisine
        self.maplink = maplink
        self.cust_rating = cust_rating
        self.cust_num = cust_num

    def getRest(self,other):
        if self.location == other.location and self.cuisine == other.cuisine:
            print(" ")
            print(f" Name:{self.name}   Link:{self.maplink}   Rating:{self.cust_rating}   Customers:{self.cust_num}")


    def updateRating(self,rate):
        # Try Except 6
        try:
            self.cust_rating = (self.cust_rating/self.cust_num)*(self.cust_num+1)
        except ArithmeticError:
            print('An calculation error occured, chekc the rating')
            

    def updateCustomer(self):
        self.cust_num = self.cust_num+1

    def resInfo(self):
        print(self.cust_num)
