import os
import google.generativeai as genai

def configure_gemini():
    """Configures the Gemini API key."""
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def initialize_model(model_name: str):
    """Initializes the Gemini model.

    Args:
        model_name: The name of the model to initialize.

    Returns:
        The initialized generative model.
    """
    return genai.GenerativeModel(model_name)

def generate_text(model, user_input: str):
    """Generates text using the provided model and user input.

    Args:
        model: The initialized generative model.
        user_input: The user's input message.

    Returns:
        The generated text response.
    """
    response = model.generate_content(user_input)  # Changed from generate_text to generate_content
    return response.text
