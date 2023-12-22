
function calculator() {
    input = document.querySelector(".calculator .form-control");
    console.log(input)
    const textAppendButtons = document.querySelectorAll(".text-append");
    textAppendButtons.forEach(btn => {
        btn.addEventListener("click", pushText);
    })

    const clearButton = document.querySelector("#btn_clear");
    clearButton.addEventListener("click", clear)

    const backspaceButton = document.querySelector("#btn_backspace");
    backspaceButton.addEventListener("click", popText);
}

function pushText() {
    if (/[a-z][A-Z]/.test(input.value)) {
        input.value = "";
    }
    console.log("pushing");

    console.log(input.value)
    console.log(event.target.value)
    input.value += event.target.value;
}

function popText() {
    input.value = input.value.slice(0, -1);
}

function clear() {
    input.value = "";
}



window.addEventListener("load", calculator)