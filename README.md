# My Chat App (Formerly Chatbot com Gemini 1.5 Flash)

This project implements an interactive chatbot using Google's Gemini 1.5 Flash model, packaged as a Python application.

## Installation

1.  **Install Python 3.7 or superior**:
    *   Download and install Python from the [official Python website](https://www.python.org/).
    *   This project was tested with Python 3.10.

2.  **Clone the repository (Optional, if not installing as a package)**:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

3.  **Create and activate a virtual environment** (Recommended):
    ```bash
    python -m venv venv
    ```
    **Windows**:
    ```bash
    venv\Scripts\activate
    ```
    **macOS/Linux**:
    ```bash
    source venv/bin/activate
    ```

4.  **Install dependencies**:
    If you cloned the repository and have a `requirements.txt` or `setup.py`/`pyproject.toml`:
    ```bash
    pip install . 
    # or pip install -r requirements.txt
    ```
    The main dependencies are `google-generativeai` and `Flask`.

## Configuring Your Gemini API Key

To use this application, you need to obtain a Gemini API key and configure it as an environment variable.

### Step 1: Create a Google AI Studio Account
- Access [Google AI Studio](https://aistudio.google.com/) and create an account or sign in.

### Step 2: Obtain Your API Key
- Follow the detailed instructions in the [Gemini API Quickstart guide](https://ai.google.dev/gemini-api/docs/quickstart) to get your API key.

### Step 3: Configure the API Key in Your Terminal

**For Windows:**
```bash
set GEMINI_API_KEY=sua_chave_api_aqui
```

**For macOS/Linux:**
```bash
export GEMINI_API_KEY=sua_chave_api_aqui
```
Replace `sua_chave_api_aqui` with your actual API key.

## Usage

1.  **Ensure your `GEMINI_API_KEY` environment variable is set** as described in the "Configuring Your Gemini API Key" section.

2.  **Run the Flask application**:
    ```bash
    python -m src.my_chat_app.routes
    ```
    (Note: If installed as a package, the command might change to a script provided by the package, e.g., `my_chat_app_run`)

3.  **Interact with the chatbot**:
    Once the server is running (typically on `http://127.0.0.1:5000`), you can send requests to the `/chat` endpoint.
    Using `curl`:
    ```bash
    curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d "{\"message\": \"Olá, como você está?\"}"
    ```

## Advanced Usage Examples

This section retains the original examples for customizing the chatbot and integrating with third-party APIs.

1.  **Personalization for a Domain (Customer Service)**

    - Add a personalization layer to the prompt for customer service. Modify the `/chat` endpoint to include a "system" message that guides the model.
    *(The following code snippet is illustrative of how you would modify `src/my_chat_app/core/gemini_service.py` or the prompt construction in `src/my_chat_app/routes.py`)*

    ```python
    # Example modification (conceptual)
    # In gemini_service.py or how prompt is constructed in routes.py:
    # def generate_text(model, user_input: str):
    #     prompt = f"""
    #     Você é um chatbot de atendimento ao cliente para uma loja de eletrônicos.
    #     Responda as dúvidas dos clientes de forma educada e precisa.
    #     Pergunta: {user_input}
    #     """
    #     response = model.generate_content(prompt)
    #     return response.text
    ```

    - **How to test**: Send a request related to electronics customer service:
      ```bash
      curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d "{\"message\": \"Vocês trabalham com troca de fonte de Computador?\"}"
      ```

2.  **Integration with Third-Party API (Weather Check)**

    - Add an additional endpoint to integrate the chatbot with a public API, like [OpenWeatherMap](https://openweathermap.org/).
    *(The following code snippet would be added to `src/my_chat_app/routes.py`)*

    ```python
    # import requests # Add to imports in routes.py
    #
    # @app.route('/weather', methods=['POST'])
    # def get_weather():
    #     city = request.json.get('city')
    #     if not city:
    #         return jsonify({'error': 'Cidade não fornecida'}), 400
    #
    #     # Replace 'sua_chave_api_openweathermap' with your actual OpenWeatherMap API key
    #     api_key = "sua_chave_api_openweathermap"
    #     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=pt_br"
    #
    #     response = requests.get(url)
    #     if response.status_code == 200:
    #         data = response.json()
    #         weather_description = data['weather'][0]['description']
    #         temp = data['main']['temp']
    #         return jsonify({
    #             'city': city,
    #             'weather': weather_description,
    #             'temperature': f"{temp} °C"
    #         })
    #     else:
    #         return jsonify({'error': 'Não foi possível obter o clima', 'details': response.text}), response.status_code

    ```

    - **How to test**: Send a request with a city name to the `/weather` endpoint:
      ```bash
      curl -X POST http://127.0.0.1:5000/weather -H "Content-Type: application/json" -d "{\"city\": \"Porto Alegre\"}"
      ```
      (Ensure the `/weather` endpoint is implemented and the server is running.)
```
