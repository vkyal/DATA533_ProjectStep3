import unittest

from TestCustomerInteraction import TestCustomer
from TestDatabase import TestDatabase
from TestRestaurant import TestRestaurant
from TestTable import TestTable

def my_suite():
    
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    
    suite.addTest(unittest.makeSuite(TestCustomer))
    suite.addTest(unittest.makeSuite(TestDatabase))
    suite.addTest(unittest.makeSuite(TestRestaurant))
    suite.addTest(unittest.makeSuite(TestTable))
    
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

my_suite()