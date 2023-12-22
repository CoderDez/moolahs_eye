
function calculator() {
    input = document.querySelector(".calculator .form-control");

    const textAppendButtons = document.querySelectorAll(".text-append");
    textAppendButtons.forEach(btn => {
        btn.addEventListener("click", pushText);
    })

    const clearButton = document.querySelector("#btn_clear");
    clearButton.addEventListener("click", clear)

    const backspaceButton = document.querySelector("#btn_backspace");
    backspaceButton.addEventListener("click", popText);
}

function pushText(event) {
    if (/[a-zA-Z]/.test(input.value)) {
        input.value = "";
    }
    input.value += event.target.value;
}

function popText(event) {
    input.value = input.value.slice(0, -1);
}

function clear(event) {
    input.value = "";
}



window.addEventListener("load", calculator)