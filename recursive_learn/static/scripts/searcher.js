const percentage_element = document.getElementById("progress");
percentage_element.style.width = percentage_element.innerHTML;

const message_percentage = document.querySelector(".message_percentage");
const number_percentage = Number(percentage_element.innerHTML.replace('%', ''));

if (number_percentage ==  0) {
    message_percentage.innerHTML = '¡Bienvenido! Preparado para comenzar a realizar ejercicios de recursividad.';
} else if (number_percentage <= 33) {
    message_percentage.innerHTML = 'Vas muy bien. Seguro que ya estás empezando a entender la recursividad.';
} else if (number_percentage <= 66) {
    message_percentage.innerHTML = '¡Animo! Ya te queda menos para ser un experto en recursividad.';
} else if (number_percentage < 100) {
    message_percentage.innerHTML = '¡Magnífico! Ya te manejas como pez en el agua con la recursividad.';
} else {
    message_percentage.innerHTML = '¡Espectacular! Ya has realizado todos los ejercicios. Ya das mejores saltos de fe que cierto personaje de cierta hermandad.';
}

const searcher = document.getElementById("searcher");
searcher.setAttribute('size',searcher.getAttribute('placeholder').length);