// Initializes the calculator by setting up event listeners and bindings
var input;

function calculator() {
    input = document.querySelector(".calculator .form-control");

    const textAppendButtons = document.querySelectorAll(".text-append");
    textAppendButtons.forEach(btn => {
        btn.addEventListener("click", pushText);
    });

    const clearButton = document.querySelector("#btn_clear");
    clearButton.addEventListener("click", clear);

    const backspaceButton = document.querySelector("#btn_backspace");
    backspaceButton.addEventListener("click", popText);
}

// Appends text from clicked buttons to the input field
function pushText(event) {
    // If the input contains any alphabetical characters (Checks for 'SYNTAX ERROR'), clear the input
    if (/[a-zA-Z]/.test(input.value)) {
        input.value = "";
    }
    input.value += event.target.value;
}

// Removes the last character from the input field
function popText(event) {
    input.value = input.value.slice(0, -1);
}

// Clears the input field
function clear(event) {
    input.value = "";
}

// Executes the 'calculator' function when the window finishes loading
window.addEventListener("load", calculator);