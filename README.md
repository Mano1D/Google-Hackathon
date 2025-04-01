# Google-Hackathon
# AI IDE Debugger with AI Code Generation

This project is a web-based ide debugger that allows users to write code in Python, JavaScript, and Java, check its syntax, run the code (currently only for Python and JavaScript), and even generate code from natural language questions using an AI model.

## Features

*   **Code Editor:**  A user-friendly code editor with line numbers.
*   **Syntax Checking:** Supports syntax checking for Python, JavaScript, and Java.
*   **Code Execution:**  Allows users to run Python and JavaScript code directly in the browser (with server-side execution for security).
*   **AI Code Generation:** Integrates with the Hugging Face Inference API to generate code from natural language prompts.
*   **Multiple Language Support:**  Supports Python, JavaScript, and Java.

## Technologies Used

*   **Frontend:** HTML, CSS, JavaScript
*   **Backend:** Python (Flask)
*   **AI Model:** BigCode/CodeGen (Hugging Face)
*   **JavaScript Linting:** ESLint, @babel/eslint-parser

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://www.google.com/search?q=https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)  # Replace with your repo URL
    cd YOUR_REPOSITORY_NAME
    ```

2.  **Install Python dependencies:**
    ```bash
    pip install Flask Flask-CORS transformers
    ```

3.  **Install JavaScript dependencies:**
    ```bash
    npm install eslint @babel/eslint-parser
    ```

4.  **Set up Hugging Face API Key:**
    *   Create a Hugging Face account (if you don't have one).
    *   Obtain your API key from your Hugging Face settings.
    *   Replace `"YOUR_HUGGING_FACE_API_KEY"` in the `index.html` file with your actual API key.

5.  **Run the Flask server:**
    ```bash
    python app.py
    ```

6.  **Open in browser:** Open `index.html` in your web browser.  If you are running the Flask server locally, it's likely accessible at `http://127.0.0.1:5000/`.

## Usage

1.  **Write code:** Enter your code in the code editor.
2.  **Select language:** Choose the appropriate language (Python, JavaScript, or Java) from the dropdown menu.
3.  **Check syntax:** Click the "Check Syntax" button to validate the code.  Any syntax errors will be displayed in the "Result" area.
4.  **Run code:** Click the "Run" button to execute the code. The output will be displayed in the "Result" area.  (Currently only Python and JavaScript are supported for execution.)
5.  **AI code generation:** Type a programming question in the chat box and click the "up" arrow. The AI will attempt to generate the code in the selected language.

## Future Development

This project is under active development, and there are plans to make it even more interactive and useful in the future.  Here are some areas for future development:

*   **Enhanced AI Code Generation:**  Improving the accuracy and capabilities of the AI code generation, potentially by fine-tuning models on specific code datasets or exploring different AI architectures.
*   **Expanded Language Support:** Adding support for more programming languages for both syntax checking and code execution.
*   **Interactive Debugging:** Implementing debugging tools to help users identify and fix errors in their code.
*   **Code Collaboration:**  Adding features to allow multiple users to collaborate on code in real-time.
*   **Improved User Interface:**  Enhancing the user interface to make it more intuitive and visually appealing.
*   **Sandboxed Code Execution:** Implementing a more secure sandboxed environment for code execution to prevent potentially harmful code from affecting the server.
*   **Integration with External Services:**  Integrating with external services such as version control systems (Git) or online coding platforms.

## Contributing

Contributions are welcome!  Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

## License

[Choose a license (e.g., MIT, Apache 2.0)]

## Acknowledgements

*   Thanks to Hugging Face for providing the BigCode/CodeGen model.
*   Thanks to the developers of Flask, Flask-CORS, and the other libraries used in this project.

