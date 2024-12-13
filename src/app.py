import os
from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configuração da chave de API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Inicialização do modelo Gemini 1.5 Flash
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'error': 'Mensagem não fornecida'}), 400

    # Envio da mensagem ao modelo
    response = model.generate_text(user_input)
    return jsonify({'response': response.text})

if __name__ == '__main__':
    app.run(debug=True)
