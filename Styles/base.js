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