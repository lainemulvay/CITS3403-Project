// Script for base.html
try {
  var dropdownContent = document.getElementById("dropdownContent");
  function toggleDropdown() {
    dropdownContent.style.display = (dropdownContent.style.display === "block") ? "none" : "block";
  }
  document.addEventListener("click", function(event) {
    var target = event.target;
    if (!target.closest(".dropdown")) {
      dropdownContent.style.display = "none";
    }
  });
} catch (err) {}


// login page JS
try {
  var login_form = document.getElementById("login-form");
  login_form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const formData = new FormData(login_form);
    const response = await fetch('/login/', {
        method: 'POST',
        body: formData
    });
    console.log(response)
    const data = await response.json();
    console.log(data)
    if (!data.success) {
      Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: data.message,
      })
    } else {
        window.location.href = '/chat';
    }
  });
} catch (err) {}


//Script for chat.html
// const API_KEY = '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' // apikey from openai

// const form = document.getElementById('input_form');
// const mytextInput = document.getElementById('chat_input_message');
// const responseTextarea = document.getElementById('response');

// form.addEventListener('submit', async (e) => {
//     e.preventDefault();

//     // Display Input message
//     console.log('Input: ' + mytextInput.value)
//     const timestamp = new Date().toLocaleString();
//     const newMessage = document.createElement('div');
//     newMessage.innerHTML = '<p class="message-content">' + mytextInput.value + '</p><p class="message-timestamp">' + timestamp + '</p>';
//     newMessage.classList.add('message', 'message-input');
//     responseTextarea.appendChild(newMessage);
    
//     const mytext = mytextInput.value.trim(); // remove unnecessary white spaces
//     mytextInput.value = []; // clear mytextInput field

//         if (mytext) {
//             try {
//                 const response = await fetch('https://api.openai.com/v1/chat/completions', {
//                     method: 'POST',
//                     headers: {
//                         'Content-Type': 'application/json',
//                         'Authorization': `Bearer ${API_KEY}`,
//                     },
//                     body: JSON.stringify({
//                         model: 'gpt-3.5-turbo',
//                         messages: [{role: 'user', content: mytext }],
//                         temperature: 1.0,
//                         top_p: 0.7,
//                         n: 1,
//                         stream: false,
//                         presence_penalty: 0,
//                         frequency_penalty: 0,
//                     }),
//                 });

//             if (response.ok) {
//                 const data = await response.json();
//                 const messageContent = data.choices[0].message.content;
//                 console.log('Response: ' + messageContent)
//                 const timestamp = new Date().toLocaleString();
//                 const newMessage = document.createElement('div');
//                 newMessage.innerHTML = '<p class="message-content">' + messageContent + '</p><p class="message-timestamp">' + timestamp + '</p>';
//                 newMessage.classList.add('message', 'message-response');
//                 responseTextarea.appendChild(newMessage);
//             } else {
//                 responseTextarea.value = 'Error';
//             }
//         } catch (error) {
//             console.log(error);
//             responseTextarea.value = 'Error';
//         }
//     }
// })

// TODO: make it press submit when you press enter. At the moment it sends a message but doesnt generate a response

//Script for register.html
try {
  var password = document.getElementById("newPW")
  var letter = document.getElementById("letter");
  var capital = document.getElementById("capital");
  var number = document.getElementById("number");
  var length = document.getElementById("length");
  var confirm_password = document.getElementById("confirmPW");

  // When the user clicks on the password field, show the message box
  password.onfocus = function() {
    document.getElementById("pw_message").style.display = "block";
  }

  // When the user clicks outside of the password field, hide the message box
  password.onblur = function() {
    document.getElementById("pw_message").style.display = "none";
  }

  // When the user starts to type something inside the password field
  password.onkeyup = function() {
    // Validate lowercase letters
    var lowerCaseLetters = /[a-z]/g;
    if(password.value.match(lowerCaseLetters)) {  
      letter.classList.remove("invalid");
      letter.classList.add("valid");
    } else {
      letter.classList.remove("valid");
      letter.classList.add("invalid");
    }
    
    // Validate capital letters
    var upperCaseLetters = /[A-Z]/g;
    if(password.value.match(upperCaseLetters)) {  
      capital.classList.remove("invalid");
      capital.classList.add("valid");
    } else {
      capital.classList.remove("valid");
      capital.classList.add("invalid");
    }

    // Validate numbers
    var numbers = /[0-9]/g;
    if(password.value.match(numbers)) {  
      number.classList.remove("invalid");
      number.classList.add("valid");
    } else {
      number.classList.remove("valid");
      number.classList.add("invalid");
    }
    
    // Validate length
    if(password.value.length >= 8) {
      length.classList.remove("invalid");
      length.classList.add("valid");
    } else {
      length.classList.remove("valid");
      length.classList.add("invalid");
    }
  }

  // confirm password matched
  function validatePassword() {
    if (password.value != confirm_password.value) {
      confirm_password.setCustomValidity("Passwords Don't Match");
    } else {
      confirm_password.setCustomValidity('');
    }
  }

  password.onchange = validatePassword;
  confirm_password.onkeyup = validatePassword;
} catch (err) {}

try {
  var regform = document.getElementById("reg-form");
  regform.addEventListener('submit', async (event) => {
      event.preventDefault();
      const formData = new FormData(regform);
      const response = await fetch('/register/', {
          method: 'POST',
          body: formData
      });
      console.log(response)
      const data = await response.json();
      console.log(data)
      if (!data.success) {
        Swal.fire({
          icon: 'warning',
          title: data.message,
          confirmButtonText: 'Go to Login page',
        }).then((res)=> {
          if (res.isConfirmed) {
            window.location.href = '/login';
          }
        })
      } else {
        Swal.fire({
          icon: 'success',
          title: data.message,
          confirmButtonText: 'Go to Login page',
        }).then((res) => {
          if (res.isConfirmed) {
            window.location.href = '/login';
          }
        })
      }
  });
} catch (err) {}