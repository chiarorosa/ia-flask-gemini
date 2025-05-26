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

There are two main ways to run this application:

### 1. Running from a Cloned Repository

This method is suitable if you want to run the latest version directly from the source code or contribute to development.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/my_chat_app.git 
    # Replace with the actual repository URL when available
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd my_chat_app 
    # Or the actual name of the directory created by git clone
    ```
3.  **Configure Your Gemini API Key:**
    Follow the instructions in the "Configuring Your Gemini API Key" section above to set your `GEMINI_API_KEY` environment variable.
4.  **Install dependencies:**
    It's recommended to create a virtual environment first.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```
5.  **Run the application:**
    ```bash
    python -m src.my_chat_app.routes
    ```
    The application will typically be available at `http://127.0.0.1:5000`.

### 2. Running as an Installed Package (Hypothetical)

This method assumes the package has been published to PyPI.

1.  **Install the package:**
    ```bash
    pip install my_chat_app 
    # Note: This package is not yet on PyPI. This is a hypothetical instruction.
    ```
2.  **Configure Your Gemini API Key:**
    Follow the instructions in the "Configuring Your Gemini API Key" section above to set your `GEMINI_API_KEY` environment variable.
3.  **Run the application:**
    ```bash
    python -m my_chat_app.routes
    ```
    The application will typically be available at `http://127.0.0.1:5000`.
