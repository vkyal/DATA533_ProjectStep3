# Test 3 Restaurant

#from BookMySpot.Data.CustomerInteraction import *
#from BookMySpot.Data.Database import *
from BookMySpot.Structure.Restaurant import *
#from BookMySpot.Structure.Table import *

import unittest

class TestRestaurant(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    
    def setUp(self):
        self.restaurant1 =Restaurant('CRAFT','Downtown','Canadian','https://goo.gl/maps/NWo2ELGLaTQYtLJ17',4.3,1683)
        self.restaurant2 =Restaurant('Cactus Club','Downtown','Canadian','https://goo.gl/maps/RmsGijZ2kTZ6BSxS6',4.4,1870)
        self.getRes = self.restaurant1.getRest(self.restaurant2)
        self.updateRating = self.restaurant1.updateRating(5)
        self.resInfo = self.restaurant1.resInfo()
        self.updateCustomer = self.restaurant1.updateCustomer
       
        
    def tearDown(self):
        pass
    
    
    def testAttribute(self):
        self.assertEqual(self.restaurant1.name,'CRAFT')
        self.assertEqual(self.restaurant2.name,'Cactus Club')
        self.assertEqual(self.restaurant1.cust_num,1683)
        self.assertEqual(self.restaurant2.cust_num,1870)
        self.assertNone(self.updateRating)
        self.assertNone(self.self.resInfo)
        self.assertNone(self.updateCustomer)
        
    def testClass(self):
        self.assertIsInstance(self.restaurant1,Restaurant)
        self.assertIsInstance(self.restaurant2,Restaurant)
        self.assertIsNot(self.restaurant1,self.restaurant2)
        self.assertIsNotNone(self.restaurant1)
       
    
        
#unittest.main(argv=[''], verbosity=2, exit=False)

