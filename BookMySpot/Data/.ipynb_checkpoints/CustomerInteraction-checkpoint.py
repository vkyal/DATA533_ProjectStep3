    # Module 1 CustomerInteraction

from BookMySpot.Structure.Table import *

import pandas as pd

tableList =[]

def initialize():
    resdata = [['Golden island' ,'Around Campus','Chinese','https://goo.gl/maps/3zQXDAaT3ySVWqpA6',4.2,115],
['Tossing Pizza','Around Campus','Italian','https://goo.gl/maps/4TpQmM7WWmmZHyLCA',3.8,109],
['CRAFT','Downtown','Canadian','https://goo.gl/maps/NWo2ELGLaTQYtLJ17',4.3,1683],
['Cactus Club','Downtown','Canadian','https://goo.gl/maps/RmsGijZ2kTZ6BSxS6',4.4,1870],
['Pho Soc Trang','Downtown','Vietnamaese','https://goo.gl/maps/siWnih6ufA2f4EkH8',4.4,436],
['O Machi' ,'Glenmore' ,'Taiwanese','https://goo.gl/maps/oMrAAAv2PzHG1Dy38',4.8,178],
['Ozeki','Glemnore','Japanese','https://goo.gl/maps/hbptDNAZKDSYi4sg8',4.5,916],
['New Punjab','Rutland','Indian','https://goo.gl/maps/j8EtHEfTRwFC4brH7',4,520],
['eMDees Indian Bistro','Rutland','Indian','https://goo.gl/maps/DJqqFb5eF3QwPQML9',3.5,95]]
    tabledata = [[4,[5,6,7,8]],
             [3,[2,3,4]],
             [4,[4,4,4,6]],
             [4,[8,8,8,8]],
             [5,[4,4,4,8,8]],
             [4,[2,2,4,4]],
             [6,[2,2,2,4,4,4]],
             [3,[8,8,8]],
             [5,[3,4,5,6,7]]]
    tableList = [Table(name = resdata[i][0],
                      location = resdata[i][1],
                      cuisine = resdata[i][2],
                      maplink = resdata[i][3],
                      cust_rating = resdata[i][4],
                      cust_num = resdata[i][5],
                   tables = tabledata[i][0],
                     seats = tabledata[i][1]) for i in range(len(resdata))]

    setTableList = [table.setTable() for table in tableList]
    return tableList

        
    
    
# Module 1

def greeting():
    print('Welcome to')
    print('''
    ╔╗ ┌─┐┌─┐┬┌─  ╔╦╗┬ ┬  ╔═╗┌─┐┌─┐┌┬┐
    ╠╩╗│ ││ │├┴┐  ║║║└┬┘  ╚═╗├─┘│ │ │
    ╚═╝└─┘└─┘┴ ┴  ╩ ╩ ┴   ╚═╝┴  └─┘ ┴   --by Xinyu and Varshita
    ''')

def location():
    print('\n Options for location: Downtown, Glenmore, Around Campus, Rutland')
    
    try:# try except 1
        userLocation = input('\nFrom the above, where do you want to eat?')
        if userLocation not in ['Downtown', 'Glenmore','Around Campus', 'Rutland']:
            raise NameError()
        return userLocation
    
    except NameError():
        print('location out of avaliable options')
        

def cuisine():
    print('\n Options for cuisine: Canadian, Chinese, Indian,Vietnamaese,Taiwanese ')
    
    try:#try except 2
        userCuisine = input('\n From the above, which cuisine type do you want to eat?')
        if userCuisine not in ['Canadian', 'Chinese', 'Indian','Vietnamaese','Taiwanese']:
            raise NameError()
        return userCuisine

    except NameError():
        print('cuisine type out of avaliable options')



def record():
    ul = location()
    uc = cuisine()
    #ut = checkin()
    userRes = Table(location = ul,
                         cuisine = uc)
    return userRes



#User Defined Exception 1
class NotInListError(Exception):
    print('The Restaurant you choose is not in our database, contact us to add')
    

def askbooking():
    name = input('\n Please select a restaurant you want to book   :' )
    options = ['Golden island','Tossing Pizza','CRAFT','Cactus Club','Pho Soc Trang','O Machi','Ozeki','New Punjab','eMDees Indian Bistro']
    # Try Except 3+ User Defined Exception
    try:
        if name not in options:
            raise NotInListError()
        return name
    
    except NotInListError():
        print('An error occured')
    
    
def checkin():
    print(pd.DataFrame({'TimeSlot':["10am:12pm",
                                    "12pm:02pm",
                                    "02pm:04pm",
                                    "04pm:06pm",
                                    "06pm:08pm"]},index =range(1,6)))
    # Try Except 4
    try:
        userCheckin = int(input('\n Select a timeSlot you want to dine in?, enter 1-5  :'))
        return userCheckin
    except ValueError:
        print('please enter a number to choose the timeslot')
    
