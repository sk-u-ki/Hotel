import pandas as pd



hotels = pd.read_csv('hotels_1.csv',  encoding="ISO-8859-1")
hotels.drop('Unnamed: 0', axis=1, inplace=True)

for i in hotels.columns.tolist():
    #hotels.rename(columns=i: i.)
    print(i)
    
hotels.info()
print(hotels.head(4))
print(hotels.columns.tolist())


hotels.to_json('/Users/kirill/Desktop/Study/Python/hotels_json_1.json',orient="records")
# hotels_new = pd.DataFrame()

# for i in range(0,len(hotels),20):
#     hotels_new = hotels_new._append(hotels.loc[i])
# print(hotels_new.head(5))
# hotels_new.info()

# hotels_new.to_csv('hotels_1.csv', encoding="ISO-8859-1")
    # for i in range(0,len(hotels)):
    #   print(f"Hotel number {i}")
    #   if i%2==0:
    #      hotels = hotels.drop(i,axis='rows')
    # hotels.info()
    # hotels.to_json('/Users/kirill/Desktop/Study/Python/hotels_json_1.json',orient="records")

