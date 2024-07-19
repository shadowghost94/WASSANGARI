const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input-chat');
const sendButton = document.getElementById('send-button-chat');

async function sendMessage() {
    const userMessage = userInput.value.trim();
    if (!userMessage) return;

    // Display user message
    displayMessage(userMessage, 'user');

    // Clear input
    userInput.value = '';

    try {
        // Send message to ChatGPT API
        const response = await fetch('https://api.openai.com/v1/completions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer sk-proj-sVO9I1158GhO1x9Mt7lCT3BlbkFJQMPimCkd2OWwuZP8RoOL'
            },
            body: JSON.stringify({
                model: 'text-davinci-003',
                prompt: userMessage,
                max_tokens: 300,
                temperature: 0.7
            })
        });

        console.log(response);

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        const botMessage = data.choices[0].text.trim();

        // Display bot message
        displayMessage(botMessage, 'bot');
    } catch (error) {
        console.error('Error:', error);
        displayMessage(`Désolé, une erreur s'est produite: ${error.message}`, 'bot');
    }
}

function displayMessage(message, sender) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('chat-message', sender);

    const messageContent = document.createElement('div');
    messageContent.classList.add('message');
    messageContent.textContent = message;

    messageElement.appendChild(messageContent);
    chatBox.appendChild(messageElement);

    // Scroll to the bottom
    chatBox.scrollTop = chatBox.scrollHeight;
}

sendButton.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendMessage();
    }
});