import pickle
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow cross-origin requests (useful if frontend calls this API)

# Load Ridge model and Scaler
with open('models/ridge.pkl', 'rb') as f:
    model = pickle.load(f)
with open('models/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

@app.route('/')
def home():
    return "<h1>ML Flask API Running!</h1>"

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return jsonify({
            'message': 'Send a POST request with JSON body {"input": [...]} to get predictions'
        })

    try:
        content = request.get_json()
        if not content or 'input' not in content:
            return jsonify({'error': 'Invalid input. Expected JSON with key "input".'}), 400
        
        # Convert input to numpy array and reshape
        data = np.array(content['input']).reshape(1, -1)
        scaled = scaler.transform(data)
        prediction = model.predict(scaled)
        
        return jsonify({'prediction': prediction.tolist()})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
