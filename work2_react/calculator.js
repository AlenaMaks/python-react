const display = document.getElementById('display');

// ночальное значение поля ввода
let currentInput = "" 

// функция обновления поля ввода, чтобы там отражались введенные символы
function updateDisplay() {
    display.value = currentInput;
}

// функция добавления цифры в поле ввода
function appendNumber(num) {
    if (currentInput === "") {
        currentInput = num;
    } else {
        currentInput += num; // формируем массив введённых цифр
    }
    updateDisplay();
}

// функция добавления оператора в поле ввода
function appendOperation(char) {
    if (currentInput != "" && !['+', '-', '/', '*'].includes(currentInput.slice(-1))) {
        currentInput += char; //добавлем если в поле ввода уже есть число и пердпоследний элемент не операция
    }
    updateDisplay();
}

// обращается к элементу класса и достает какое число на нажатой кнопке и передает в функцию
const numButtons = document.querySelectorAll('.num');
numButtons.forEach(btn => {
    btn.addEventListener('click', () => {
        appendNumber(btn.textContent);
    });
});

// обращается к элементу класса и достает какая операция на нажатой кнопке и передает в функцию
document.getElementById('add').addEventListener('click', () => {
    appendOperation('+');
});
document.getElementById('sub').addEventListener('click', () => {
    appendOperation('-');
});
document.getElementById('mul').addEventListener('click', () => {
    appendOperation('*');
});
document.getElementById('div').addEventListener('click', () => {
    appendOperation('/');
});
