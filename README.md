# ML Flask API 🚀

This is a simple **Machine Learning API** built with **Flask**.  
It loads a trained Ridge Regression model and scaler, and provides predictions through a REST API.

---

## ⚡ Features
- Flask-based REST API
- Ridge Regression model with preprocessing scaler
- JSON input/output
- CORS enabled for frontend usage

---

## 📂 Project Structure
ML_FLASK_1st/
├── models/
│ ├── ridge.pkl # Trained ML model
│ └── scaler.pkl # Scaler used for preprocessing
├── notebooks/
│ ├── height-weight.csv
│ └── ml_cycle_implementation.ipynb
├── app.py # Flask API code
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## ▶️ How to Run Locally
1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/ml-flask-api.git
   cd ml-flask-api


Install dependencies:

pip install -r requirements.txt


Run the Flask app:

python app.py


Open in browser:

http://127.0.0.1:5000/

📡 API Usage
Endpoint: /predict

Method: POST
Input JSON:

{
  "input": [5.1, 3.5, 1.4, 0.2]
}


Response JSON:

{
  "prediction": [42.7]
}

🚀 Deployment

This project is ready to deploy on Render or any cloud provider.
On Render:

Build Command → pip install -r requirements.txt

Start Command → python app.py

👨‍💻 Author

Mohit Bohra

📧 Email: bohramohit93199@gmail.com

🌐 GitHub: Mohit05012005