let a = Math.floor(Math.random() * 100); // ответ не 5, если a = 0, 1, 2
let step1
let step2
let step3

// (a > 10 ? a : a * 2)
if (a > 10) {
    step1 = a
}
else step1 = a*2
if (step1 > 5) {
    step2 = (2 * a) + 1
}
// (a < 3 ? 1 : 2 * (a - 2))
else {
    if (a < 3) {
        step2 = 1
    }
    else step2 = 2 * (a - 2)
}
if (step2 > 4) {
    step3 = 5
}
// (a % 2 == 0 ? 6 : 7)
else {
    if (a % 2 == 0) {
        step3 = 6
    }
    else step3 = 7
}

console.log("Значение a: ", a)
console.log("Ответ: ", step3)

// (a > 10 ? a : a * 2) > 5 ? (2 * a) + 1 : (a < 3 ? 1 : 2 * (a - 2)) > 4 ? 5 : (a % 2 == 0 ? 6 : 7);