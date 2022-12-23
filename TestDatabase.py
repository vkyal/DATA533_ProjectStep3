# Module 2 Database

from BookMySpot.Data.CustomerInteraction import *
from BookMySpot.Data.Database import *
#from BookMySpot.Structure.Restaurant import *
#from BookMySpot.Structure.Table import *

import unittest
tableList = initialize()

class TestDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    
    def setUp(self):
        self.tableList = initialize()
        self.userRes = Restaurant(location='Downtown', cuisine='Canadian')
        self.chosenTable = chosenTable('CRAFT',tableList)
        self.feedback = askFeedback()
        
       
        
    def tearDown(self):
        pass
    
    
    def testChosenTable(self):
        self.assertEqual(self.chosenTable.location,'Downtown')
        self.assertEqual(self.chosenTable.maplink,'https://goo.gl/maps/NWo2ELGLaTQYtLJ17')
        self.assertEqual(self.chosenTable.cust_rating,4.3)
        self.assertEqual(self.chosenTable.cust_num,1683)
        
    def testfeedback(self):
        self.assertIn(self.feedback,[1,2,3,4,5])
        self.assertEqual(type(self.feedback),int)
        self.assertNotEqual(self.feedback,4) 
        self.assertIsNotNone(self.feedback)
    
        
#unittest.main(argv=[''], verbosity=2, exit=False)


