from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Set OpenAI API key from env
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "").strip()

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    try:
        # Attempt actual OpenAI API call
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # Or gpt-3.5-turbo
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        reply = response['choices'][0]['message']['content']
        return jsonify({"response": reply})

    except openai.error.OpenAIError as e:
        error_message = str(e)

        # 🛑 If quota exceeded or API fails, fallback to mock
        if "quota" in error_message.lower():
            print("⚠️ Quota exceeded — using mock response")
            reply = f"🤖 (Mocked) GPT says: You asked — '{prompt}'"
            return jsonify({"response": reply, "note": "Quota exceeded, using mock response"}), 200
        else:
            # Other OpenAI errors
            print(f"❌ OpenAI API error: {error_message}")
            return jsonify({
                "error": "OpenAI API error",
                "details": error_message
            }), 500

    except Exception as e:
        # Handle non-OpenAI errors
        print(f"❌ Unexpected error: {str(e)}")
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
