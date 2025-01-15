let menubtn = document.querySelector(".harmbugger");
let closebtn = document.querySelector(".removed");
let ul = document.querySelector(".ul");
let pbtn = document.querySelector(".button");
let navbar = document.querySelector("#header")
let doc  = document.documentElement;

menubtn.addEventListener("click", function(){
	menubtn.classList.add("closed");
	ul.classList.add("opened");
})

closebtn.addEventListener("click", function(){
	menubtn.classList.remove("closed")
	ul.classList.remove("opened");
})
        
/** Circle Scrolling **/
let scrollPercentage = () =>{
	let scrollProgress = document.getElementById("progress");
	let progressValue = document.getElementById("progress-value");
	let pos =document.documentElement.scrollTop;
	let calcHeight = document.documentElement.scrollHeight -document.documentElement.clientHeight;
	let scrollValue = Math.round( pos * 100 / calcHeight);
	scrollProgress.style.background = `conic-gradient(rgb(7 ,7 ,200) ${scrollValue}%, #c0c0ff ${scrollValue}%)`;
	progressValue.textContent =  `${scrollValue}%`;
}

window.onscroll = scrollPercentage;
window.onload  = scrollPercentage;

function eMail() {
	window.open("mailto:abiolaayokunnu101@gmail.com", "_blank");
}

window.addEventListener("scroll", function(){
	if(window.scrollY > 15 ){
		navbar.classList.add("scrolled")
	}else{
		navbar.classList.remove("scrolled")
	}
})