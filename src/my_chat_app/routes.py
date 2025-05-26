from flask import Flask, request, jsonify
from src.my_chat_app.core.gemini_service import configure_gemini, initialize_model, generate_text

app = Flask(__name__)

# Configure Gemini API and initialize the model
configure_gemini()
model = initialize_model('gemini-1.5-flash')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'error': 'Mensagem não fornecida'}), 400

    response_text = generate_text(model, user_input)
    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(debug=True)
