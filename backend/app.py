from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

DATA_FILE = "submitted_data.json"

@app.route('/calculate', methods=['POST'])
def save_data():
    data = request.get_json()

    # Load existing data if file exists
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            try:
                existing_data = json.load(f)
            except json.JSONDecodeError:
                existing_data = []
    else:
        existing_data = []

    # Append new submission
    existing_data.append(data)

    # Save updated data
    with open(DATA_FILE, 'w') as f:
        json.dump(existing_data, f, indent=4)

    return jsonify({"message": "Data Submitted Successfully"})

# Direct GET route for backend testing
@app.route('/submit', methods=['GET'])
def submit_message():
    return "data submitted successfully"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug = True)
