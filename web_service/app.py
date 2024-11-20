from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    with open('config/config.json', 'r') as config_file:
        config_data = json.load(config_file)
    return jsonify(message=config_data["message"])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
