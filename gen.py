import json
import pandas as pd
import random

 
# filename = '/Users/kirill/Desktop/Study/Python/hotels_json_1.json'
file = "hotels_img.csv"
# hotels = pd.read_json(file,orient="records")

hotel = pd.read_csv("hotels_img.csv")


img = hotel["hotel_image"]
print(img.info())
print(random.choice(img))
if (input("Y/n") != "Y"):
    pass

print(img[0])
print(img.head())

# with open(file, 'w') as json_file:
#     json.dump(hotels, json_file, 
#                         indent=4,  
#                         separators=(',',': '))

#hotels.to_json(filename,orient="records")
 
print('Successfully appended to the JSON file')