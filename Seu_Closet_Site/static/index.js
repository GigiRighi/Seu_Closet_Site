function scrollToCloset() {
    document.getElementById("closet").scrollIntoView({ behavior: "smooth" });
}

function addItem(item) {
    const lista = document.getElementById("lista-look");

    const li = document.createElement("li");
    li.textContent = item;

    lista.appendChild(li);
}

function limparLook() {
    document.getElementById("lista-look").innerHTML = "";
}
