//SIDEBAR
const mainImg = document.querySelector(".main-img");
const images = document.querySelectorAll(".gallery-wrapper img");
const closeBtn = document.querySelector(".close");
const nextBtn = document.querySelector(".next");
const prevBtn = document.querySelector(".prev");

nextBtn.addEventListener("click", nextImg);
prevBtn.addEventListener("click", prevImg);

closeBtn.addEventListener("click", (e) => {
	mainImg.style.display = "none";
	mainImg.classList.remove("active");
});

//ANIMACIONES PARA LAS TRANSICIONES DE LAS IMAGENES
const imgStyles = `animation: imgTransition 0.450s  ease-in-out`;
let showImg = document.querySelector(".main-img img");
let imagesArray = [];
let selectedImg;

//FUNCION NEXT BUTTON
function nextImg() {
	if (selectedImg < 0) return;
	let number = Number(selectedImg);
	let higestCount = Number(imagesArray.length - 1);
	if (number === higestCount) {
		number = 0;
	} else {
		number++;
	}
	selectedImg = number;
	showImg.src = imagesArray[selectedImg];
	addRemoveAnimation();
}

//FUNCION PREV BUTTON
function prevImg() {
	if (selectedImg < 0) return;
	let number = Number(selectedImg);
	let lowestCount = 0;
	let higestCount = Number(imagesArray.length - 1);
	if (number <= lowestCount) {
		number = higestCount;
	} else {
		number--;
	}
	selectedImg = number;
	showImg.src = imagesArray[selectedImg];
	addRemoveAnimation();
}

// Initial Click Handler
for (let image of images) {
	imagesArray.push(image.src);
	image.addEventListener("click", (e) => {
		let img = e.target;
		currentSelectedImg = imagesArray.indexOf(img.src);
		mainImg.style.display = "block";
		mainImg.classList.add("active");
		showImg.src =
			imagesArray[selectedImg !== undefined ? selectedImg : currentSelectedImg];
		selectedImg = currentSelectedImg;
	});
}

// FUNCION PARA AGREGAR O REMOVER ATRIBUTO ESTILO
function addRemoveAnimation() {
	showImg.setAttribute("style", imgStyles);
	setTimeout(() => {
		showImg.setAttribute("style", "");
	}, 500);
}
//FIN SLIDER

//Google maps
function iniciarMap(){
    var coord = {lat: -33.3696454, lng: -70.4683196};
    var map = new google.maps.Map(document.getElementById('map'),{
        zoom: 15,
        center: coord
    });
    var marker = new google.maps.Marker({
        position: coord,
        map: map
    });
}