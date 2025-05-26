import unittest
from unittest.mock import patch, MagicMock
import os
# Adjust the import path based on your project structure
from src.my_chat_app.core import gemini_service

class TestGeminiService(unittest.TestCase):

    @patch.dict(os.environ, {"GEMINI_API_KEY": "test_api_key"})
    @patch('google.generativeai.configure')
    def test_configure_gemini(self, mock_configure):
        gemini_service.configure_gemini()
        mock_configure.assert_called_once_with(api_key="test_api_key")

    @patch('google.generativeai.GenerativeModel')
    def test_initialize_model(self, mock_generative_model):
        model_instance_mock = MagicMock()
        mock_generative_model.return_value = model_instance_mock
        
        model = gemini_service.initialize_model('gemini-1.5-flash')
        
        mock_generative_model.assert_called_once_with('gemini-1.5-flash')
        self.assertEqual(model, model_instance_mock)

    @patch('google.generativeai.GenerativeModel') # Keep this if initialize_model is called inside generate_text or if model is passed
    def test_generate_text(self, MockGenerativeModel): # MockGenerativeModel might not be needed if model is passed as arg
        # Mock the model instance that would be returned by initialize_model or passed to generate_text
        mock_model_instance = MagicMock() # This represents the 'model' argument in generate_text

        # Configure the mock for the generate_content method
        mock_response = MagicMock()
        mock_response.text = "Test response"
        mock_model_instance.generate_content.return_value = mock_response # Mocking generate_content
        
        # Call the function with the mocked model instance
        response = gemini_service.generate_text(mock_model_instance, "Hello")
        
        # Assert that generate_content was called correctly on the passed mock_model_instance
        mock_model_instance.generate_content.assert_called_once_with("Hello")
        self.assertEqual(response, "Test response")

if __name__ == '__main__':
    unittest.main()
