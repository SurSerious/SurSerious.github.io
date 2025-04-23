document.addEventListener('DOMContentLoaded', function() {
     const chatForm = document.getElementById('chat-form');
     const userInput = document.getElementById('user-input');
     const chatOutput = document.getElementById('chat-output');

     chatForm.addEventListener('submit', async function(e) {
       e.preventDefault();
       
       const message = userInput.value;
       if (!message) return;

       // Add user message to chat
       chatOutput.innerHTML += `<div class="user-message">${message}</div>`;
       userInput.value = '';
       
       try {
         const response = await fetch('http://localhost:5000/chat', {
           method: 'POST',
           headers: { 'Content-Type': 'application/json' },
           body: JSON.stringify({ message: message })
         });
         
         const data = await response.json();
         chatOutput.innerHTML += `<div class="bot-message">${data.reply}</div>`;
       } catch (error) {
         console.error('Error:', error);
         chatOutput.innerHTML += `<div class="error">Error connecting to chatbot</div>`;
       }
     });
   });
