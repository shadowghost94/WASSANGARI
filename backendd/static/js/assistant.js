
    const chatBox = document.getElementById('chat-box');
    const userInputChat = document.getElementById('user-input-chat');
    const sendButtonChat = document.getElementById('send-button-chat');

    async function sendMessage() {
        const inputText = userInputChat.value;

        // Construction de la requête JSON
        const data = {
            contents: [
                {
                    role: "user",
                    parts: [{ text: inputText }]
                }
            ]
        };

        try {
            const response = await fetch('https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=AIzaSyCgHDGBU-YzQeE0LSDi7grRP8lyH5rHzaU', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });

            const responseData = await response.json();

            // Extraction du texte généré
            const generatedText = responseData.candidates[0].content.parts[0].text;

            // Affichage du texte généré dans le chat box
            const userMessageDiv = document.createElement('div');
            userMessageDiv.textContent = `Vous: ${inputText}`;
            chatBox.appendChild(userMessageDiv);

            const botMessageDiv = document.createElement('div');
            botMessageDiv.textContent = `Bot: ${generatedText}`;
            chatBox.appendChild(botMessageDiv);

            chatBox.appendChild(document.createElement('br'));

            // Réinitialiser l'input de l'utilisateur
            userInputChat.value = '';

        } catch (error) {
            console.error('Erreur:', error);
            const errorMessageDiv = document.createElement('div');
            errorMessageDiv.textContent = 'Une erreur s\'est produite. Veuillez réessayer.';
            chatBox.appendChild(errorMessageDiv);
        }
    }

    sendButtonChat.addEventListener('click', (event) => {
        event.preventDefault();
        sendMessage();
    });

    userInputChat.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            event.preventDefault();
            sendMessage();
        }
    });
