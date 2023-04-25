const API_KEY = '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' // apikey from openai

const form = document.getElementById('input_form');
const mytextInput = document.getElementById('chat_input_message');
const responseTextarea = document.getElementById('response');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Display Input message
    console.log('Input: ' + mytextInput.value)
    const timestamp = new Date().toLocaleString();
    const newMessage = document.createElement('div');
    newMessage.innerHTML = '<p class="message-content">' + mytextInput.value + '</p><p class="message-timestamp">' + timestamp + '</p>';
    newMessage.classList.add('message', 'message-input');
    responseTextarea.appendChild(newMessage);

    const mytext = mytextInput.value.trim(); // remove unnecessary white spaces

        if (mytext) {
            try {
                const response = await fetch('https://api.openai.com/v1/chat/completions', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${API_KEY}`,
                    },
                    body: JSON.stringify({
                        model: 'gpt-3.5-turbo',
                        messages: [{role: 'user', content: mytext }],
                        temperature: 1.0,
                        top_p: 0.7,
                        n: 1,
                        stream: false,
                        presence_penalty: 0,
                        frequency_penalty: 0,
                    }),
                });

            if (response.ok) {
                const data = await response.json();
                const messageContent = data.choices[0].message.content;
                console.log('Response: ' + messageContent)
                const timestamp = new Date().toLocaleString();
                const newMessage = document.createElement('div');
                newMessage.innerHTML = '<p class="message-content">' + messageContent + '</p><p class="message-timestamp">' + timestamp + '</p>';
                newMessage.classList.add('message', 'message-response');
                responseTextarea.appendChild(newMessage);
                mytextInput.value = []; // clear mytextInput field
            } else {
                responseTextarea.value = 'Error';
            }
        } catch (error) {
            console.log(error);
            responseTextarea.value = 'Error';
        }
    }
})