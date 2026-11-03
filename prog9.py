from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = 'your_api_key_here'


@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', 'London')

    url = 'https://api.openweathermap.org/data/2.5/weather'

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code != 200:
            return jsonify({
                "error": "City not found or API error"
            }), response.status_code

        data = response.json()

        formatted = {
            "city": data['name'],
            "temperature": data['main']['temp'],
            "feels_like": data['main']['feels_like'],
            "humidity": data['main']['humidity'],
            "description": data['weather'][0]['description'],
            "wind_speed": data['wind']['speed']
        }

        return jsonify(formatted)

    except requests.RequestException:
        return jsonify({
            "error": "Unable to connect to the weather service"
        }), 503


if __name__ == '__main__':
    app.run(debug=True)
