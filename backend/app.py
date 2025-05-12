from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Search
import requests
import datetime

app = Flask(__name__)
CORS(app)  # Allow frontend to access backend

# Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Weather API config
API_KEY = 'a2ff93ad07cff882f33419cde4de0253'
WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather'

with app.app_context():
    db.create_all()


@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter required'}), 400

    # Call weather API
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(WEATHER_URL, params=params)
    data = response.json()

    if response.status_code != 200:
        return jsonify({'error': data.get('message', 'Unknown error')}), 400

    # Save search to DB
    search = Search(city=city, timestamp=datetime.datetime.utcnow())
    db.session.add(search)
    db.session.commit()

    return jsonify({
        'city': data['name'],
        'temp': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon']
    })

@app.route('/history', methods=['GET'])
def get_history():
    searches = Search.query.order_by(Search.timestamp.desc()).limit(5).all()
    return jsonify([s.city for s in searches])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

