from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json

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
        from datetime import datetime
        date_obj = datetime.fromisoformat(date.replace('Z', '+00:00'))
        
        # Build API request to timeanddate.com using the correct endpoint
        # Based on the documentation, we need to use the astrodata endpoint
        params = {
            'version': '3',
            'prettyprint': '1',
            'accesskey': API_ACCESS_KEY,
            'secretkey': API_SECRET_KEY,
            'placeid': f'{lat},{lon}',
            'startdt': date_obj.strftime('%Y-%m-%d'),
            'enddt': date_obj.strftime('%Y-%m-%dT%H:%M:%S'),
            'object': 'moon',
            'types': 'astrodata'
        }
        
        print(f"Calling timeanddate.com API with params: {params}")
        
        # Try the correct endpoint based on documentation
        api_endpoints = [
            f'{API_BASE_URL}/astrodata',
            f'{API_BASE_URL}/astro',
            f'{API_BASE_URL}/astronomy'
        ]
        
        for endpoint in api_endpoints:
            try:
                print(f"Trying endpoint: {endpoint}")
                response = requests.get(endpoint, params=params)
                
                if response.status_code == 200:
                    data = response.json()
                    print(f"API Response: {json.dumps(data, indent=2)}")
                    return jsonify(data)
                else:
                    print(f"Endpoint {endpoint} failed: {response.status_code} - {response.text}")
                    
            except Exception as e:
                print(f"Error with endpoint {endpoint}: {str(e)}")
                continue
        
        return jsonify({'error': 'All API endpoints failed'}), 500
        
    except Exception as e:
        print(f"Server error: {str(e)}")
        return jsonify({'error': f'Server error: {str(e)}'}), 500

if __name__ == '__main__':
    print("Starting Moon Position API Server...")
    print(f"Access Key: {API_ACCESS_KEY}")
    print("Server will be available at: http://localhost:5000")
    app.run(debug=True, port=5000) 