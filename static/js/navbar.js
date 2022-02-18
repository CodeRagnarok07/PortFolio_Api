const navbotton = document.querySelector("#navboton")
const navmenu = document.querySelector("#navmenu")

navbotton.addEventListener('click', () => { // al hacer click en el elemento despliege
  navmenu.classList.toggle("hidden") // le agrega la clase hidden al objeto itens
})