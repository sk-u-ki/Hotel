from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['demo'] 
collection = db['hotels']     

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    location = request.form['location']
    # guests = int(request.form['adults'])
    # rooms = int(request.form['rooms'])
    # comfort = request.form['comfort']
    

    # Пример простого запроса к MongoDB
    query = {
        "countyName": location
        # "max_guests": {"$gte": guests},
        # "rooms_available": {"$gte": rooms},
        # "comfort": {"$lte": comfort}
        
    }

    results = collection.find(query)

    
    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)