// obtengo las imagenes de la API
let images;

fetch("http://localhost:8000/imagenes")
  .then(response => response.json())
  .then(data => {
    images = data.imagenes;
    console.log(images);
    // Mostrar la primera imagen al cargar la página
    showImage(currentIndex);
  })
  .catch(error => {
    console.error("Error:", error);
  });

// VISUALIZADOR
let currentIndex = 0;

function showImage(index) {
  const imageElement = document.getElementById("current-image");
  imageElement.src = "../" + images[index];
}

function showNextImage() {
  currentIndex = (currentIndex + 1) % images.length;
  showImage(currentIndex);
}

function showPreviousImage() {
  currentIndex = (currentIndex - 1 + images.length) % images.length;
  showImage(currentIndex);
}