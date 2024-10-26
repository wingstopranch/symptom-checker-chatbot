document.addEventListener("DOMContentLoaded", () => {
    const chatBox = document.getElementById("chat-box");
    const userInput = document.getElementById("user-input");
    const sendBtn = document.getElementById("send-btn");
    const typingIndicator = document.getElementById("typing-indicator");

    function appendMessage(content, className) {
        const messageElement = document.createElement("div");
        messageElement.className = className;
        messageElement.textContent = content;
        chatBox.appendChild(messageElement);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    sendBtn.addEventListener("click", () => {
        const userText = userInput.value.trim();
        if (userText) {
            appendMessage(userText, "user-message");
            userInput.value = "";
            typingIndicator.style.display = "block";
            
            // Simulate bot response
            setTimeout(() => {
                typingIndicator.style.display = "none";
                const botResponse = getBotResponse(userText);
                appendMessage(botResponse, "bot-message");
            }, 1000);
        }
    });

    userInput.addEventListener("keypress", (e) => {
        if (e.key === "Enter") {
            sendBtn.click();
        }
    });

    function getBotResponse(input) {
        // Basic keyword matching for bot response
        const responses = {
            "hello": "Hi there! How can I assist you today?",
            "fever": "It sounds like you may have a fever. Please consult with a healthcare provider for further assistance.",
            "headache": "I'm sorry to hear that. A headache could be caused by various reasons, like dehydration or stress. Consider resting and drinking water.",
            "default": "I'm not sure about that. Could you please provide more details?"
        };

        input = input.toLowerCase();
        for (const key in responses) {
            if (input.includes(key)) {
                return responses[key];
            }
        }
        return responses["default"];
    }
});
