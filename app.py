from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import os
import ast
import subprocess
import shutil

app = Flask(__name__, static_folder='', static_url_path='')
CORS(app)

# OpenRouter API Key (Required)
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    raise ValueError("❗ Error: OPENROUTER_API_KEY is not set in environment variables.")

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# ✅ **Syntax Checking for Python**
@app.route('/check_code', methods=['POST'])
@app.route('/check_code', methods=['POST'])
@app.route('/check_code', methods=['POST'])
def check_code():
    data = request.get_json()
    code = data.get("code", "")
    language = data.get("language", "").lower()

    if not code or not language:
        return jsonify({"result": "❌ Error: Code or language not provided!"}), 400

    if language == "python":
        try:
            ast.parse(code)
            return jsonify({"result": "✅ Python Syntax is correct!"})
        except SyntaxError as e:
            return jsonify({"result": f"❌ Python Syntax Error: {e.msg} at line {e.lineno}"}), 400

    elif language == "java":
        try:
            # Use raw code if it looks like a complete class/program
            if "class" in code or "public static void main" in code:
                java_code = code
            else:
                java_code = f"""
public class Main {{
    public static void main(String[] args) {{
        {code}
    }}
}}
"""

            with open("Main.java", "w") as f:
                f.write(java_code)

            compile_result = subprocess.run(["javac", "Main.java"], capture_output=True, text=True)

            if compile_result.returncode != 0:
                return jsonify({"result": f"❌ Java Compilation Error:\n{compile_result.stderr}"}), 400

            return jsonify({"result": "✅ Java Syntax is correct!"})

        except Exception as e:
            return jsonify({"result": f"❌ Error: {str(e)}"}), 500

    elif language == "javascript":
        try:
            # Check if the JS code is valid (basic check using Node.js)
            result = subprocess.run(["node", "-e", code], capture_output=True, text=True)
            if result.returncode != 0:
                return jsonify({"result": f"❌ JavaScript Syntax Error:\n{result.stderr}"}), 400

            return jsonify({"result": "✅ JavaScript Syntax is correct!"})

        except Exception as e:
            return jsonify({"result": f"❌ Error: {str(e)}"}), 500

    else:
        return jsonify({"result": "❌ Error: Only Python, Java, and JavaScript syntax checking are supported!"}), 400


# ✅ **AI Chatbot with OpenRouter**
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '')

    if not message:
        return jsonify({"error": "No message provided!"}), 400

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "deepseek/deepseek-r1-zero:free",
        "messages": [{"role": "user", "content": message}],
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        response_data = response.json()

        if response.status_code == 200 and "choices" in response_data:
            reply = response_data["choices"][0]["message"]["content"]
            return jsonify({"result": reply})
        else:
            return jsonify({"error": "Invalid response from OpenRouter API"}), 500

    except Exception as e:
        return jsonify({"error": f"API request failed: {str(e)}"}), 500

# ✅ **Code Execution for Python, JavaScript, Java**
@app.route('/run_code', methods=['POST'])
def run_code():
    data = request.get_json()
    code = data.get("code")
    language = data.get("language").lower()

    if not code or not language:
        return jsonify({"output": "❌ Error: Code or language not provided!"}), 400

    try:
        if language == "python":
            result = subprocess.run(["python", "-c", code], capture_output=True, text=True, timeout=5)

        elif language == "javascript":
            result = subprocess.run(["node", "-e", code], capture_output=True, text=True, timeout=5)

        elif language == "java":
            # Use full code if user wrote a class or method
            if "class" in code or "public static void main" in code:
                java_code = code
            else:
                java_code = f"""
public class Main {{
    public static void main(String[] args) {{
        {code}
    }}
}}
"""

            with open("Main.java", "w") as f:
                f.write(java_code)

            compile_result = subprocess.run(["javac", "Main.java"], capture_output=True, text=True, timeout=5)
            if compile_result.returncode != 0:
                return jsonify({"output": f"❌ Compilation Error:\n{compile_result.stderr}"}), 400

            result = subprocess.run(["java", "Main"], capture_output=True, text=True, timeout=5)

            try:
                os.remove("Main.java")
                os.remove("Main.class")
            except FileNotFoundError:
                pass

        else:
            return jsonify({"output": "❌ Error: Unsupported language!"}), 400

        output = result.stdout if result.stdout else result.stderr
        return jsonify({"output": output.strip()})

    except subprocess.TimeoutExpired:
        return jsonify({"output": "❌ Error: Execution timed out!"}), 400
    except Exception as e:
        return jsonify({"output": f"❌ Error: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
