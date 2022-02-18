navbotton = document.querySelector("#navboton")
navmenu = document.querySelector("#navmenu")

navbotton.addEventListener("click", () => {
    navmenu.classList.toggle("hidden")
})