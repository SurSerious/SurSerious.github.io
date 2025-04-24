from flask import Flask, request, jsonify, render_template, send_from_directory
import requests
from dotenv import load_dotenv
import os
from flask_cors import CORS

# Load environment and setup
load_dotenv()
app = Flask(__name__, static_folder='static')
CORS(app)  # Enable CORS for all routes

# Configuration
HF_API_KEY = os.getenv("HF_API_TOKEN")
MODEL_API_URL = "https://api-inference.huggingface.co/models/openai-community/gpt2"
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}

@app.route('/')
def index():
    """Serve the chatbot interface"""
    return render_template('index.html')

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/health')
def health_check():
    """Verify the server is running"""
    return jsonify({"status": "active", "model": "gpt2"})

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Validate input
        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 400
            
        user_message = request.json.get('message')
        if not user_message:
            return jsonify({"error": "Message is required"}), 400

        # Call Hugging Face API
        response = requests.post(
            MODEL_API_URL,
            headers=HEADERS,
            json={"inputs": user_message, "parameters": {"max_length": 100}},
            timeout=30  # 30-second timeout
        )

        # Handle Hugging Face errors
        if response.status_code != 200:
            error_msg = response.json().get('error', 'Unknown error from Hugging Face')
            return jsonify({"error": f"Hugging Face API: {error_msg}"}), 502

        # Extract and return response
        generated_text = response.json()[0]['generated_text']
        return jsonify({"reply": generated_text})

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Connection error: {str(e)}"}), 503
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
