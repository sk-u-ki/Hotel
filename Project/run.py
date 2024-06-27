from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['demo'] 
collection = db['hotels']     

@app.route('/')
def index():
    return render_template('index.html')


def filtr(results, guests):
    results_new = []
    for i in results:
        for j in range(1,i["Rooms"]):
            f = f"Room{j}"
            if i[f]["available"] == 0 and guests <= i[f]["numberGuests"]:
                results_new.append(i)
                print("konic")
                break
    return results_new
def convert_stars(comfort):
    if comfort == "1":
        return "OneStar"
    if comfort == "2":
        return "TwoStar"
    if comfort == "3":
        return "ThreeStar"
    if comfort == "4":
        return "FourStar"
    if comfort == "5":
        return "FiveStar"    
def filtr_by_amenities(amenities):
    global wifi
    wifi = 0
    global breakfast
    breakfast = 0
    global parking
    parking = 0
    for i in amenities:
        match i :
            case "wifi":
                wifi = 1
            case "breakfast":
                breakfast = 1
            case "parking":
                parking = 1
@app.route('/search', methods=['POST'])
def search():
    location = request.form['location']
    guests = int(request.form['adults'])
    amenities = request.form.getlist('amenities')
    # rooms = int(request.form['rooms'])
    comfort = request.form['comfort']
    stars = convert_stars(comfort)
    filtr_by_amenities(amenities)
    #print(parking,wifi,breakfast)
    query = {
        "countyName": location,
        "HotelRating": comfort,
        "Parking":{"$gte": parking},
        "FreeWIFI":{"$gte": wifi},
        "Breakfast":{"$gte":breakfast}
    }
    
    results = collection.find(query)
    results_new = filtr(results,guests)
    print(results_new)
    return render_template('results.html', results=results_new)

if __name__ == '__main__':
    app.run(debug=True)

