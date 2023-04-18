function loginButton() {
    var loginDiv = document.getElementById("login");
    var descriptionsDiv = document.getElementById("descriptions");
    var introButton = document.getElementById("intro_button");

    loginDiv.style.display = "block";
    descriptionsDiv.style.display = "none";
    introButton.style.display = "none"
}

function home() {
    var loginDiv = document.getElementById("login");
    var descriptionsDiv = document.getElementById("descriptions");
    var introButton = document.getElementById("intro_button");

    loginDiv.style.display = "none";
    descriptionsDiv.style.display = "block";
    introButton.style.display = "inline"
}