from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# timeanddate.com API credentials
API_ACCESS_KEY = 'KRySdBTeW8'
API_SECRET_KEY = 'NZTdzFBdJBPWKtYVYcWE'
API_BASE_URL = 'https://api.xmltime.com'

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/moon-position')
def get_moon_position():
    try:
        # Get parameters from request
        lat = request.args.get('lat')
        lon = request.args.get('lon')
        date = request.args.get('date')
        
        if not all([lat, lon, date]):
            return jsonify({'error': 'Missing required parameters: lat, lon, date'}), 400
        
        # Parse the date string to get proper format
        date_obj = datetime.fromisoformat(date.replace('Z', '+00:00'))
        
        # Format the interval parameter for the API
        interval = date_obj.strftime('%Y-%m-%dT%H:%M:%S')
        
        # Build API request to timeanddate.com using the correct format
        # Based on the documentation, we use coordinates directly with the astrodata endpoint
        params = {
            'version': '3',
            'prettyprint': '1',
            'accesskey': API_ACCESS_KEY,
            'secretkey': API_SECRET_KEY,
            'placeid': f'{lat},{lon}',  # Use coordinates directly
            'object': 'moon',
            'interval': interval,
            'isotime': '1',  # Include ISO timestamps
            'utctime': '1'   # Include UTC timestamps
        }
        
        print(f"Calling timeanddate.com API with params: {params}")
        
        # Use the astrodata endpoint as specified in the documentation
        response = requests.get(f'{API_BASE_URL}/astrodata', params=params)
        
        if response.status_code == 200:
            data = response.json()
            print(f"API Response: {json.dumps(data, indent=2)}")
            return jsonify(data)
        else:
            print(f"API request failed: {response.status_code} - {response.text}")
            return jsonify({'error': f'API request failed: {response.status_code}'}), 500
            
    except Exception as e:
        print(f"Server error: {str(e)}")
        return jsonify({'error': f'Server error: {str(e)}'}), 500

if __name__ == '__main__':
    print("Starting Moon Position API Server...")
    print(f"Access Key: {API_ACCESS_KEY}")
    print("Server will be available at: http://localhost:8000")
    app.run(debug=True, port=8000) 