#Model 2 Database

from BookMySpot.Structure.Restaurant import *
from BookMySpot.Structure.Table import *

def restInfo(userRes,tableList):
    # filtering eligible
    for res in tableList:
        res.getRest(userRes)



def chosenTable(name,tableList):
    for table in tableList:
        if name == table.name:
            return table


def askFeedback():
    # try except 5
    try:
        rate = int(input('\n What is your rating, given the scale of 1-5  :'))
        print("\n Thankyou for your Feedback!")
        return rate
    except ValueError:
        print('please enter a number to rate')
   
