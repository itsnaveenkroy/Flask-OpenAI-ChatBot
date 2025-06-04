#  Flask + OpenAI Chatbot API (with Mock Fallback)

This is a minimal Flask-based REST API that takes a user prompt and returns a response generated using OpenAI's GPT model (GPT-4o).  
When the API key quota is exceeded or not set, it automatically returns a mock response for testing/demo purposes.

---

##  Features

-  REST API built using Flask
-  GPT-4o integration using OpenAI's API
-  Auto fallback to mocked response if quota is exceeded
-  Clean error handling
-  Ready for local testing with Postman
-  Easy to deploy and extend


- Accepts JSON POST requests with a `prompt` field.
- Sends prompt to OpenAI GPT-4o (or GPT-3.5-turbo) API.
- Returns generated text response.
- Handles quota exceeded errors gracefully with a mock response fallback.
- Error handling for various failure scenarios.

---
## Installation

1. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your OpenAI API key:

   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

---

## Usage

Run the Flask server:

```bash
python app.py
```

By default, the server runs on `http://127.0.0.1:5000`.

---

## API Endpoint

### POST `/generate`

* Request JSON body:

```json
{
  "prompt": "Your question or text here"
}
```

* Response JSON:

```json
{
  "response": "Generated reply from GPT"
}
```

* Error responses include appropriate HTTP status codes and error messages.

---

## Notes

* The API uses GPT-4o model by default. You can change it in the code (`app.py`) if needed.
* If your OpenAI API quota is exceeded, the API will return a mock response instead of failing.
* Make sure your OpenAI API key is valid and has enough quota.

---

