# Module 4 Table


import pandas as pd
import numpy as np
from .Restaurant import Restaurant

class Table(Restaurant):
    def __init__(self,name ='NA',
                 location='NA',
                 cuisine='NA',
                 maplink='NA',
                 cust_rating='NA',
                 cust_num='NA',tables='NA',seats=[],data = 0,seat_map = 0):
        Restaurant.__init__(self,name,location,cuisine,maplink,cust_rating,cust_num)
        self.tables = tables
        self.data = data
        self.seats = seats
        self.seat_map = seat_map

    def setTable(self):
        data = np.zeros((self.tables,5))
        self.seat_map = pd.DataFrame(data, index = range(1,self.tables+1), columns=["10am:12pm","12pm:02pm","02pm:04pm","04pm:06pm","06pm:08pm"])
        self.seat_map.insert(0, "Seater", self.seats)
        self.seat_map.index.name = "Table number"

    def emptyTable(self,time_slot):
        if time_slot == 1:
            time = "10am:12pm"
        elif time_slot == 2:
            time = "12pm:02pm"
        elif time_slot == 3:
            time = "02pm:04pm"
        elif time_slot == 4:
            time = "04pm:06pm"
        else:
            time = "06pm:08pm"
        empty =self.seat_map.loc[self.seat_map[time] == 0]
        print("\n",empty[["Seater"]])
        return time

    def bookTable(self,t_num,time_slot):
        if time_slot == 1:
            time = "10am:12pm"
        elif time_slot == 2:
            time = "12pm:02pm"
        elif time_slot == 3:
            time = "02pm:04pm"
        elif time_slot == 4:
            time = "04pm:06pm"
        else:
            time = "06pm:08pm"

        if self.seat_map.at[t_num,time] == 0:
            self.seat_map.at[t_num,time] =1
            print("Hurray🎉!! Table is booked")
        else:
            print("Sorry, table is already booked")



