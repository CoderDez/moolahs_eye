
var form, input, buttons;

function calculator() {
    form = document.getElementsByClassName("calculator");
    input = form.getElementsByTagName("input");
    buttons = form.getElementsByTagName("button")
    configureEventListeners()
}

function configureEventListeners() {
    buttons.forEach(function(btn) {
        if ( !Number.isNaN(btn.value) || "+-x/.()".contains(btn.value) ) {
            btn.addEventListener("click", pushText);
        }
        else if (btn.value == "del") {
            btn.addEventListener("click", popText);
        }
        else if (btn.value == "ac") {
            btn.addEventListener("click", clear);
        }
    })
}

// event handler
function pushText() {
    if (/[a-z][A-Z]/.test(input.value)) {
        input.value = "";
        input.value += target.value;
    }
}

function popText() {
    input.value = input.value.slice(0, -1);
}

function clear() {
    input.value = "";
}



window.addEventListener("load", calculator)