from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['demo'] 
collection = db['hotels']     

@app.route('/')

def index():
    return render_template('index.html')

def resu(results, guests):
        resul = []
        for i in results:
            x=1
            for j in range(1,i["Rooms"]):
                while x==1:
                    f = f"Room{j}"
                    if i[f]["available"] == 0 and guests <= i[f]["numberGuests"]:
                        resul.append(i)
                        break
                    
                

        return resul


@app.route('/search', methods=['POST'])
def search():
    location = request.form['location']
    guests = int(request.form['adults'])
    wifi = request.form['amenities']
    breakfast = request.form['amenities_2']
    parking = request.form['amenities']
    Balkon = request.form['amenities']
    # rooms = int(request.form['rooms'])
    comfort = request.form['comfort']
    print(wifi)
    print(Balkon)
    if comfort == "3":
        comfort = "ThreeStar"
    # Пример простого запроса к MongoDB
    query = {
        "countyName": location,
        # "max_guests": {"$gte": guests},
        # "rooms_available": {"$gte": rooms},
        "HotelRating": comfort
        # "aviable": 1
        
    }
    print(comfort)
    results = collection.find(query)
    results_1 = []

    for i in results:
        for j in range(1,i["Rooms"]):
            f = f"Room{j}"
            if i[f]["available"] == 0 and guests <= i[f]["numberGuests"]:
                results_1.append(i)
                print("konic")
                break
   
            
            

        
    
    
    return render_template('results.html', results=results_1)

if __name__ == '__main__':
    app.run(debug=True)

