from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS
from blockchain import Blockchain
from encryption_utils import generate_key

app = Flask(__name__)

# Enable CORS for the entire app
CORS(app)

# Initialize the blockchain
blockchain = Blockchain()

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the CryptoVault Blockchain API!"})

@app.route('/generate-key', methods=['POST'])
def generate_key_route():
    key = generate_key()
    return jsonify({"key": key})

@app.route('/add-data', methods=['POST'])
def add_data():
    data = request.json.get('data')
    key = request.json.get('key')
    new_block = blockchain.add_block(data, key)
    return jsonify({"blockchain": blockchain.get_chain()})

if __name__ == '__main__':
    app.run(debug=True)
