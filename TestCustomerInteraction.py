# Module 1 CustomerInteraction

from BookMySpot.Data.CustomerInteraction import *
import unittest

class TestCustomer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    
    def setUp(self):
        self.initialize = initialize()
        self.location = "Downtown"
        self.cuisine = "Canadian"
        self.askbooking = "CRAFT"
        self.checkin = 1
        self.locationChoice = ['Downtown', 'Glenmore', 'Around Campus',' Rutland']
        self.cuisineChoice = ['Canadian',' Chinese',' Indian','Vietnamaese','Taiwanese']
        self.bookChoice = ['Golden island','Tossing Pizza','CRAFT','Cactus Club','Pho Soc Trang','O Machi','Ozeki','New Punjab','eMDees Indian Bistro']
        self.checkinChoice = [1,2,3,4,5]
        
    def tearDown(self):
        pass
    
    
    def testType(self):
        self.assertEqual(type(self.location),str)
        self.assertEqual(type(self.cuisine),str)
        self.assertEqual(type(self.askbooking),str)
        self.assertEqual(type(self.checkin),int)
        self.assertNone(greeting())
        
    def testInGivenChoice(self):
        self.assertIn(self.location,self.locationChoice)
        self.assertIn(self.cuisine,self.cuisineChoice)
        self.assertIn(self.askbooking,self.bookChoice)
        self.assertIn(self.checkin,self.checkinChoice)
    
        
#unittest.main(argv=[''], verbosity=2, exit=False)
