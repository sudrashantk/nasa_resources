import requests
from flask import Flask, render_template, request

app = Flask(__name__)

NASA_API_URL = 'https://images-api.nasa.gov/search'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    media_type = request.form.get('media_type', 'image')
    year_start = request.form.get('year_start', '')
    year_end = request.form.get('year_end', '')

    # Build query parameters for the API request
    params = {
        'q': query,
        'media_type': media_type,
        'year_start': year_start,
        'year_end': year_end
    }

    # Make the request to the NASA API
    response = requests.get(NASA_API_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        # Render the template and pass in the search results
        return render_template('results.html', results=data['collection']['items'])
    else:
        return f"Error: Unable to retrieve data from NASA. Status code: {response.status_code}"

if __name__ == '__main__':
    app.run(debug=True)
