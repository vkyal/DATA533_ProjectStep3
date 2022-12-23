# Test Table

#from BookMySpot.Data.CustomerInteraction import *
#from BookMySpot.Data.Database import *
#from BookMySpot.Structure.Restaurant import *
from BookMySpot.Structure.Table import *

import unittest



class TestTable(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    
    def setUp(self):
        self.table1 =Table('CRAFT','Downtown','Canadian','https://goo.gl/maps/NWo2ELGLaTQYtLJ17',4.3,1683,4,[4,4,4,6])
        self.table2 =Table('Cactus Club','Downtown','Canadian','https://goo.gl/maps/RmsGijZ2kTZ6BSxS6',4.4,1870,4,[8,8,8,8])
        self.table1setted1 = self.table1.setTable()
        self.table1setted2 = self.table2.setTable()
        self.emptyTable5 = self.table1.emptyTable(5)
        self.emptyTable4 = self.table1.emptyTable(4)
        self.emptyTable3 = self.table1.emptyTable(3)
        self.emptyTable2 = self.table1.emptyTable(2)
        self.emptyTable1 = self.table1.emptyTable(1)
        self.bookTable1  = self.table1.bookTable(1,"10am:12pm")
        self.bookTable2  = self.table1.bookTable(1,"12pm:02pm")
        self.bookTable3  = self.table1.bookTable(2,"10am:12pm")
        self.bookTable4  = self.table1.bookTable(2,"12pm:02pm")
        self.bookTable5  = self.table1.bookTable(1,"10am:12pm")
       
        
    def tearDown(self):
        pass
    
    
    def testAttribute(self):
        self.assertEqual(self.table1.name,'CRAFT')
        self.assertEqual(self.table2.name,'Cactus Club')
        self.assertEqual(self.table1.tables,4)
        self.assertEqual(self.table2.tables,4)
        self.assertNotEqual(self.emptyTable5,5)
        self.assertNotEqual(self.emptyTable4,4)
        self.assertNotEqual(self.emptyTable3,3)
        self.assertNotEqual(self.emptyTable2,2)
        self.assertNotEqual(self.emptyTable1,1)
        self.assertNotEqual(self.bookTable1,3)
       
      
        
    def testClass(self):
        self.assertIsInstance(self.table1,Table)
        self.assertIsInstance(self.table2,Table)
        self.assertIsNot(self.table1,self.table2)
        self.assertIsNotNone(self.table1)
       
    
        
#unittest.main(argv=[''], verbosity=2, exit=False)




