let a = Math.floor(Math.random() * 100);
let step1
let step2
let step3

// (a > 10 ? a : a * 2)
switch (true) {
    case (a > 10):
        step1 = a
        break
    default:
        step1 = a * 2
}

switch (true) {
    case (step1 > 5):
        step2 = (2 * a) + 1
        break
    // (a < 3 ? 1 : 2 * (a - 2))
    case (a < 3):
        step2 = 1
        break
    default:
        step2 = 2 * (a - 2)
}

switch (true) {
    case (step2 > 4):
        step3 = 5
        break
    //(a % 2 == 0 ? 6 : 7)
    case (a % 2 == 0):
        step3 = 6
        break
    default:
        step3 = 7
}

console.log("Значение a: ", a)
console.log("Ответ: ", step3)

// (a > 10 ? a : a * 2) > 5 ? (2 * a) + 1 : (a < 3 ? 1 : 2 * (a - 2)) > 4 ? 5 : (a % 2 == 0 ? 6 : 7);