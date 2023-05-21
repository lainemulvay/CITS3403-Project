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
  var password = document.getElementById("newpw")
  var letter = document.getElementById("letter");
  var capital = document.getElementById("capital");
  var number = document.getElementById("number");
  var special = document.getElementById("special");
  var length = document.getElementById("length");
  var confirm_password = document.getElementById("confirmpw");

  // When the user clicks on the password field, show the message box
  password.onfocus = function() {
    document.getElementById("pw-message").style.display = "inline-block";
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
      confirm_password.setCustomValidity("Passwords don't match.");
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

// toggle for reset password page
try {
  const togglePassword = document.querySelector('#showPassword');
  const password = document.getElementById('oldpw');

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
  const togglePassword1 = document.querySelector('#showPassword1');
  const newpw = document.getElementById('newpw');
  const togglePassword2 = document.querySelector('#showPassword2');
  const confirmpw = document.getElementById('confirmpw');

  togglePassword1.addEventListener('click', function (e) {
    // toggle the type attribute
    const type = newpw.getAttribute('type') === 'password' ? 'text' : 'password';
    newpw.setAttribute('type', type);
    // toggle the eye slash icon
    this.classList.toggle('fa-eye-slash');
  });

  togglePassword2.addEventListener('click', function (e) {
    // toggle the type attribute
    const type = confirmpw.getAttribute('type') === 'password' ? 'text' : 'password';
    confirmpw.setAttribute('type', type);
    // toggle the eye slash icon
    this.classList.toggle('fa-eye-slash');
  });
} catch (err) {}

// Register function
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

// Script for history
function view_chat(button){
  var chat_id = button.value;
  window.location.href = '/history/'+ chat_id;
}

// toggle update user button
function update_ac() {
  var firstnameInput = document.getElementById("firstname");
  var lastnameInput = document.getElementById("lastname");
  var emailInput = document.getElementById("email");
  var updateButton = document.getElementById("update");
  var saveButton = document.getElementById("save")
  var inputgroup = document.querySelectorAll('.inputgroup');

  if (lastnameInput.readOnly) {
    // if is readonly, toggle to false
    firstnameInput.readOnly = false;
    lastnameInput.readOnly = false;
    emailInput.readOnly = false;
    updateButton.style.display = "none";
    saveButton.style.display = "inline-block";
    // set each inputgroup background color
    inputgroup.forEach(function(element) {
      element.style.backgroundColor = '#ffffff';
    });
  } else {
    firstnameInput.readOnly = true;
    lastnameInput.readOnly = true;
    emailInput.readOnly = true;
    updateButton.style.display = "block";
    saveButton.style.display = "none";
    // set each inputgroup background colors
    inputgroup.forEach(function(element) {
      element.style.backgroundColor = '#e9ecef';
    });
  }
}

// update user detail function
try {
  var updateform = document.getElementById("update-form");
  updateform.addEventListener('submit', async (event) => {
      event.preventDefault();
      const formData = new FormData(updateform);
      const response = await fetch('/profile/', {
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
          confirmButtonText: 'OK',
        }).then((res)=> {
          if (res.isConfirmed) {
            window.location.href = '/profile';
          }
        })
      } else {
        Swal.fire({
          icon: 'success',
          title: data.message,
          confirmButtonText: 'OK',
        }).then((res) => {
          if (res.isConfirmed) {
            window.location.href = '/profile';
          }
        })
      }
  });
} catch (err) {}

// change password function
try {
  var updateform2 = document.getElementById("changePW-form");
  updateform2.addEventListener('submit', async (event) => {
      event.preventDefault();
      const formData = new FormData(updateform2);
      const response = await fetch('/profile/', {
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
          confirmButtonText: 'OK',
        })
      } else {
        Swal.fire({
          icon: 'success',
          title: data.message,
          confirmButtonText: 'OK',
        }).then((res) => {
          if (res.isConfirmed) {
            window.location.href = '/profile';
          }
        })
      }
  });
} catch (err) {}

// tab controller for profile page
try {
  // Get the element with id="defaultOpen" and click on it
  document.getElementById("defaultOpen").click();
} catch (err) {}

function openTab(evt, tab) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("login-form");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(tab).style.display = "block";
  evt.currentTarget.className += " active";
}

function goBack() {
  window.history.back();
}
