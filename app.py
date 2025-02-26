from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import ast

app = Flask(__name__, static_folder='', static_url_path='')  # Crucial for serving from the same directory
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')  # Serve index.html from the current directory

@app.route('/check_code', methods=['POST'])
def check_code():
    # ... (rest of your code remains the same)
    code = request.json.get('code')  # Get the code from the request
    result = check_syntax(code)  # Use the check_syntax function to check code
    return jsonify({"result": result})

def check_syntax(code):
    try:
        compile(code, '<string>', 'exec')  # Python's built-in syntax checking
        return "Code is syntactically correct!"
    except SyntaxError as e:
        return f"Syntax Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
