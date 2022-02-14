const despliege =  document.querySelector("#despliege")
const itens =  document.querySelector("#itens")


despliege.addEventListener('click', ()=> { // al hacer click en el elemento despliege
    console.log("hiso click ")
    itens.classList.toggle("hidden") // le agrega la clase hidden al objeto itens
})