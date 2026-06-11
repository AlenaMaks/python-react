/*
    примитивный калькулятор HTML + JavaScript с мат. операторами

    Реализовано:
    - ввод чисел с помощью кнопок;
    - ввод только одной математической операции (+, -, *, /) в выражении;
    - вычисление результата через отдельные функции add(), sub(), mul(), div();
    - вывод выполненных вычислений в историю;
    - очистка всего ввода (C);
    - удаление последнего символа (Delete);
    - поддержка вещественных чисел через ".";
    - защита от повторного ввода точки в одном числе;
    - запрет ввода нескольких операций в одном выражении;
    (сделала обработку, чтобы символы операций не вводились подряд, для возможности масштабирования)
    - запрет ввода операции в начале выражения;
    - обработка ведущих нулей (04 заменяется на 4);
    - защита от вычисления незавершённого выражения (12+, 5*);
    - обработка деления на ноль;
    - автоматическое отображение нуля после точки в истории для красоты
    (например, 12.+3 отображается как 12.0+3).

    Ограничения:
    - не поддерживаются сложные выражения вида 2+3*4;
    - не поддерживаются отрицательные числа.
    (забыла заложить их, когда продумывала логику, в задании вроде нет как обязательного условия :")
*/

const display = document.getElementById('display');
const history = document.getElementById('history');

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
    } 
    else {
        let lastNumber = "";
        for (let i = currentInput.length - 1; i >= 0; i--) {
            if (['+', '-', '*', '/'].includes(currentInput[i])) break;
            lastNumber = currentInput[i] + lastNumber;
        }
        if (lastNumber === "0") {
            currentInput = currentInput.slice(0, -1) + num; // также для корректной обработки второго числа
        }
        else {
            currentInput += num;
        }
    }
    updateDisplay();
}

// функция добавления оператора в поле ввода
function appendOperation(char) {
    if (currentInput === "") return;
    if (['+', '-', '/', '*'].includes(currentInput.slice(-1))) return;
    for (let i = 0; i < currentInput.length; i++) {
        if (['+', '-', '/', '*'].includes(currentInput[i])) {
            return; // не добавляем знак операции если уже есть одна операция в вычислении
        }
    }
    currentInput += char; //добавлем если в поле ввода уже есть число и пердпоследний элемент не операция
    updateDisplay();
}

// кнопка очистки
function clearAll() {
    currentInput = "";
    updateDisplay();
}

// кнопка удаления последнего символа
function backspace() {
    if (currentInput != "") {
        currentInput = currentInput.slice(0, -1) // кроме последнего элемента
    }
    updateDisplay();
}

// кнопка точки 
function appendDot() {
    if (currentInput === "") return
    if (['+', '-', '*', '/', '.'].includes(currentInput.slice(-1))) return

    let lastNumber = "";
    for (let i = currentInput.length - 1; i >= 0; i--) {
        if (['+', '-', '*', '/'].includes(currentInput[i])) break
        lastNumber = currentInput[i] + lastNumber;
    }
    if (!lastNumber.includes('.')) {
        currentInput += '.'; // добавляем если только в последнем числе не было точек
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

// обращается к элементу класса и очищает ввод
document.getElementById('clearAll').addEventListener('click', clearAll);
// тоже обращается, но удаляет последний элмент только
document.getElementById('backspace').addEventListener('click', backspace);
// точка
document.getElementById('dot').addEventListener('click', appendDot);
// равно, функция ниже
document.getElementById('equals').addEventListener('click', operResult);

function add(a, b) {
    return a + b;
}
function sub(a, b) {
    return a - b;
}
function mul(a, b) {
    return a * b;
}
function div(a, b) {
    return a / b;
}

function operResult() {
    let operation = '';
    if (['+', '-', '*', '/'].includes(currentInput.slice(-1))) return; // не считаем если одно число
    for (let i = 0; i < currentInput.length; i++) {
        if (['+', '-', '*', '/'].includes(currentInput[i])) {
            operation = currentInput[i];
            break;
        }
    }
    if (operation === '') return; // если только число то ничего не делаем
    let parts = currentInput.split(operation); // разделяем по операции на две части
    let a = Number(parts[0]);
    let b = Number(parts[1]);

    let result;
    switch (operation) {
        case '+':
            result = add(a, b);
            break;
        case '-':
            result = sub(a, b);
            break;
        case '*':
            result = mul(a, b);
            break;
        case '/':
            if (b === 0) {
                addToHistory("Ошибка: деление на 0");
                currentInput = "";
                updateDisplay();
                return;
            }
            result = div(a, b);
            break;
    }
    let partsForHistory = currentInput.split(operation);
    if (partsForHistory[0].endsWith('.')) {
        partsForHistory[0] += '0';
    }
    if (partsForHistory[1].endsWith('.')) {
        partsForHistory[1] += '0';
    }
    let expression = partsForHistory[0] + operation + partsForHistory[1]; 
    // обработка 0 после . если ничего не было поставлено

    addToHistory(expression + " = " + result);
    currentInput = ""; // можно убрать чтобы не очищалось окно
    updateDisplay();
}

// работа с историей и вывод туда
function addToHistory(text) {
    history.append(text);
    history.append(document.createElement('br'));
}