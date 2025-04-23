from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Set your OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    
    # Call the LLM
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ]
    )
    
    return jsonify({
        "reply": response.choices[0].message.content
    })

@app.route('/', methods=['GET'])
def home():
    return "Chatbot API is running!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)