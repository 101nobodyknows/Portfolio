var closealertbtn = document.getElementById("close-alert");
var close_alert = document.getElementById("alert");
var preloader = document.getElementById("loader");

closealertbtn.addEventListener("click", function() {
	close_alert.style.display = "none";
})

function load() {
  preloader.style.display = "none";
}