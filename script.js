function checkCode() {
    const code = document.getElementById("codeInput").value;
    const language = document.getElementById("languageSelect").value;
    const resultDiv = document.getElementById("result");

    if (!code.trim()) {
        resultDiv.innerText = "❌ Error: Code cannot be empty!";
        resultDiv.style.color = "red";
        return;
    }

    fetch("http://127.0.0.1:5000/check_code", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code, language })
    })
    .then(response => response.json())
    .then(data => {
        resultDiv.innerText = data.result;
        resultDiv.style.color = data.result.includes("❌") ? "red" : "green";
    })
    .catch(error => {
        resultDiv.innerText = "❌ Error checking the code!";
        resultDiv.style.color = "red";
        console.error("Error:", error);
    });
}

async function chatWithAI() {
    let userInput = document.getElementById("chatBox").value.trim();
    let resultDiv = document.getElementById("result");

    if (!userInput) {
        resultDiv.innerText = "❌ Error: Please enter a message!";
        resultDiv.style.color = "red";
        return;
    }

    // Simple AI suggestions for common programming queries
    if (userInput.toLowerCase().includes("print from 1 to 10")) {
        resultDiv.innerHTML = `<pre><code>for i in range(1, 11): print(i)</code></pre>`;
        resultDiv.style.color = "blue";
    } else {
        try {
            const response = await fetch("http://127.0.0.1:5000/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: userInput })
            });

            const data = await response.json();

            if (response.ok && data.result) {
                resultDiv.innerHTML = `<pre>🤖 AI: ${data.result}</pre>`;
                resultDiv.style.color = "green";
            } else {
                resultDiv.innerText = data.error || "❌ Error: Failed to get AI response!";
                resultDiv.style.color = "red";
            }
        } catch (error) {
            resultDiv.innerText = "❌ Error: Unable to contact AI!";
            resultDiv.style.color = "red";
            console.error("Error:", error);
        }
    }

    // Clear the chat box after sending the message
    document.getElementById("chatBox").value = "";
}

function updateLineNumbers() {
    const codeInput = document.getElementById("codeInput");
    const lineNumbers = document.getElementById("lineNumbers");
    const lines = codeInput.value.split("\n").length;
    lineNumbers.innerHTML = Array.from({ length: lines }, (_, i) => i + 1).join("<br>");
}

function runCode() {
    const code = document.getElementById("codeInput").value;
    const language = document.getElementById("languageSelect").value;
    const resultDiv = document.getElementById("result");

    if (!code.trim()) {
        resultDiv.innerText = "❌ Error: Code cannot be empty!";
        resultDiv.style.color = "red";
        return;
    }

    fetch("http://127.0.0.1:5000/run_code", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code, language })
    })
    .then(response => response.json())
    .then(data => {
        resultDiv.innerHTML = `<pre>${data.output}</pre>`;
        resultDiv.style.color = "black";
    })
    .catch(error => {
        resultDiv.innerText = "❌ Error executing code!";
        resultDiv.style.color = "red";
        console.error("Error:", error);
    });
}


updateLineNumbers();
