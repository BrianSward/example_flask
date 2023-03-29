from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return "Index Page"

@app.route('/user-post', methods=['POST'])
def user_post():
    try:
        # Extract data from request JSON
        data = request.get_json()
        username = data['username']
        text = data['text']
        
        # Restructure data with current datetime
        restructured_data = {
            'data': {
                'username': username,
                'text': text,
                'created': datetime.now()
            },
            'success': True
        }
        
        # Return restructured data as JSON response
        return jsonify(restructured_data)
    except:
        # Handle any exceptions
        return jsonify({'success': False})