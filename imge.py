import csv
import random
import numpy as np
import pandas as pd

import json
from os import path

bool_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
             1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

def maker_upd(rooms,avg_price=400):
   bool_random_list = random.sample(bool_list,3+rooms*2)
   list_upd = {
      "Parking": bool_list[0],
      "FreeWIFI": bool_list[1],
      "Breakfast": bool_list[2],
      "Rooms":rooms
      }
      
   for i in range(1,rooms):
      price = round((random.random()+1)*avg_price)
      room = {
             "numberGuests":3,
             "available":bool_random_list[2*i+1],
             "balkon":bool_random_list[2*i+2],
             "price":price
             }
      list_upd[f"Room{i}"] = room
   
   return list_upd

def maker_price(rooms,avg_price=400):
   bool_random_list = random.sample(bool_list,3+rooms*2)

   list_upd = {
      "Parking": bool_list[0]
      }
   for i in range(1,rooms):
      guests = random.randint
      room = {
             "numberGuests":,
             "available":bool_random_list[2*i+1],
             "balkon":bool_random_list[2*i+2]
             }
      list_upd[f"Room{i}"] = room
   
   return list_upd

def exportDataFromCSV(name):
    hotels = pd.read_csv('hotels.csv',  encoding="ISO-8859-1")
    hotels.dropna(subset=['countyCode'], inplace=True)
    for i in hotels.columns.tolist():
        #hotels.rename(columns=i: i.)
        print(i)
    hotels.dropna(subset=[' PhoneNumber'], inplace=True)
    hotels.drop(' FaxNumber', axis=1, inplace=True)
    hotels.info()
    print(hotels.head(4))
    print(hotels.columns.tolist())
    hotels = pd.read_csv('hotels_1.csv',  encoding="ISO-8859-1")
    hotels.drop('Unnamed: 0', axis=1, inplace=True)

    hotels.info()
    first_four = hotels.head(4)
    print(hotels.tail())
    print(hotels.columns.tolist())
    hotels.info()
    hotels.to_json('/Users/kirill/Desktop/Study/Python/hotels_json_1.json',orient="records")



#exportDataFromCSV("hotels.csv")

# print(hotels)

 
filename = '/Users/kirill/Desktop/Study/Python/hotels_json_1.json'
listObj = []
 
# Check if file exists
if path.isfile(filename) is False:
  raise Exception("File not found")
 
# Read JSON file
with open(filename) as fp:
  listObj = json.load(fp)
 
# Verify existing list


for i in range(0,len(listObj)):
   print(f"Hotel number {i} processing...")
   listObj[i].update(maker_upd(random.randint(10,80),random.randint(200,1000)))
   print(f"Hotel number {i} already updated")

 
 
with open(filename, 'w') as json_file:
    json.dump(listObj, json_file, 
                        indent=4,  
                        separators=(',',': '))
 
print('Successfully appended to the JSON file')



# hotels.dropna(subset=['countyCode'], inplace=True)
# for i in hotels.columns.tolist():
#     #hotels.rename(columns=i: i.)
#     print(i)
# hotels.dropna(subset=[' PhoneNumber'], inplace=True)
# hotels.drop(' FaxNumber', axis=1, inplace=True)
# hotels.info()
# print(hotels.head(4))
# print(hotels.columns.tolist())
# hotels = pd.read_csv('hotels_1.csv',  encoding="ISO-8859-1")
# hotels.drop('Unnamed: 0', axis=1, inplace=True)

# hotels.info()
# first_four = hotels.head(4)
# print(hotels.tail())
# print(hotels.columns.tolist())

# hotels.to_json('/Users/kirill/Desktop/Study/Python/hotels_json_1.json',orient="records")
