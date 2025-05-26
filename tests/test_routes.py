import unittest
from unittest.mock import patch, MagicMock
import json
import os

# Temporarily add src to sys.path to allow importing my_chat_app
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from my_chat_app.routes import app as flask_app
# If the model is initialized globally in routes.py, we might need to mock gemini_service functions
# before 'from my_chat_app.routes import app'
# For now, let's assume it's okay or handle it within tests.

class TestChatRoutes(unittest.TestCase):

    def setUp(self):
        flask_app.testing = True
        self.client = flask_app.test_client()
        # We need to ensure that the model used by the app is a mock,
        # or that generate_text is properly patched before any call.
        # Patching os.environ for GEMINI_API_KEY as it's used in routes.py at module level
        self.env_patch = patch.dict('os.environ', {'GEMINI_API_KEY': 'testkey_for_routes'})
        self.env_patch.start()

        # It's critical to mock the dependencies of routes.py (like gemini_service)
        # BEFORE the app uses them. If model initialization happens at import time in routes.py,
        # this patching needs to be more sophisticated, possibly by refactoring routes.py
        # to have a create_app() function.

        # For now, we will patch 'generate_text' where it's used in routes.py
        # And we will also patch 'configure_gemini' and 'initialize_model' to prevent real calls
        # if they are called at the module level in routes.py
        self.mock_configure_gemini = patch('src.my_chat_app.core.gemini_service.configure_gemini').start()
        self.mock_initialize_model = patch('src.my_chat_app.core.gemini_service.initialize_model').start()
        
        # Mock the model returned by initialize_model
        self.mock_model_instance = MagicMock()
        self.mock_initialize_model.return_value = self.mock_model_instance


    def tearDown(self):
        self.env_patch.stop()
        patch.stopall() # Stops all patches started with start()

    @patch('src.my_chat_app.routes.generate_text') # Patching where generate_text is directly used in routes
    def test_chat_endpoint_success(self, mock_routes_generate_text):
        mock_routes_generate_text.return_value = "Mocked Gemini Response"
        
        response = self.client.post('/chat', 
                                    data=json.dumps({'message': 'Hello Gemini'}),
                                    content_type='application/json')
        
        data = json.loads(response.data.decode())
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['response'], "Mocked Gemini Response")
        
        # Check if generate_text was called with the model instance and the message
        # The 'model' in routes.py should be the one returned by the mocked initialize_model
        mock_routes_generate_text.assert_called_once_with(self.mock_model_instance, "Hello Gemini")


    def test_chat_endpoint_no_message(self):
        response = self.client.post('/chat',
                                    data=json.dumps({}),
                                    content_type='application/json')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', data)
        # Assuming the error message is in Portuguese as per original app.py
        self.assertEqual(data['error'], 'Mensagem não fornecida')

if __name__ == '__main__':
    # Need to ensure src is in path for command line execution too
    if os.path.join(os.getcwd(), 'src') not in sys.path and os.path.join(os.getcwd(), '..', 'src') not in sys.path :
        sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
    unittest.main()
