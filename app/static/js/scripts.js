// Script for base.html
// try {
//   var dropdownContent = document.getElementsByClassName("dropdown-content");
//   function toggleDropdown() {
//     dropdownContent.style.display = (dropdownContent.style.display === "block") ? "none" : "block";
//   }
//   document.addEventListener("click", function(event) {
//     var target = event.target;
//     if (!target.closest(".dropdown")) {
//       dropdownContent.style.display = "none";
//     }
//   });
// } catch (err) {}


try {
  fetch('/me')
  .then(response => response.json())
  .then(data => {
    console.log('Logged-in user details:', data);
  })
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
    console.log('Logged in user:', response.user);
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

// logout function
try {
  function logout() {
    fetch('/logout', { method: 'GET' })
      .then(response => response.redirected ? window.location.href = response.url : null)
      .catch(error => console.error('Error:', error));
  }
} catch (err) {}

//Script for register.html
try {
  var password = document.getElementById("newPW")
  var letter = document.getElementById("letter");
  var capital = document.getElementById("capital");
  var number = document.getElementById("number");
  var special = document.getElementById("special");
  var length = document.getElementById("length");
  var confirm_password = document.getElementById("confirmPW");

  // When the user clicks on the password field, show the message box
  password.onfocus = function() {
    document.getElementById("pw-message").style.display = "block";
  }

  // When the user clicks outside of the password field, hide the message box
  password.onblur = function() {
    document.getElementById("pw-message").style.display = "none";
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

    // Validate special characters
    var specialChars = /[!@#$%_^&+=]/g;
    if(password.value.match(specialChars)) {  
      special.classList.remove("invalid");
      special.classList.add("valid");
    } else {
      special.classList.remove("valid");
      special.classList.add("invalid");
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

// toggle for login page
try {
  const togglePassword = document.querySelector('#showPassword');
  const password = document.getElementById('password');

  togglePassword.addEventListener('click', function (e) {
    // toggle the type attribute
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);
    // toggle the eye slash icon
    this.classList.toggle('fa-eye-slash');
  });
} catch (err) {}

// toggle for reg page
try {
  const togglePassword1 = document.querySelector('#showPassword');
  const newPW = document.getElementById('newPW');
  const togglePassword2 = document.querySelector('#showPassword2');
  const confirmPW = document.getElementById('confirmPW');

  togglePassword1.addEventListener('click', function (e) {
    // toggle the type attribute
    const type = newPW.getAttribute('type') === 'password' ? 'text' : 'password';
    newPW.setAttribute('type', type);
    // toggle the eye slash icon
    this.classList.toggle('fa-eye-slash');
  });

  togglePassword2.addEventListener('click', function (e) {
    // toggle the type attribute
    const type = confirmPW.getAttribute('type') === 'password' ? 'text' : 'password';
    confirmPW.setAttribute('type', type);
    // toggle the eye slash icon
    this.classList.toggle('fa-eye-slash');
  });
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