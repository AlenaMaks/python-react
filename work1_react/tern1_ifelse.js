let a = Math.floor(Math.random() * 100); 
let step1
let step2
let step3

if (a > 10) {
    step1 = a
}
else step1 = a*2
if (step1 > 5) {
    step2 = (2 * a) + 1
    console.log("Значение a: ", a)
    console.log("Ответ: ", step2)
}
else {
    if (a < 3) {
        step2 = 1
    }
    else step2 = 2 * (a - 2)
    if (step2 > 4) {
        step3 = 5
    }
    else {
        if (a % 2 == 0) {
        step3 = 6
        }
        else step3 = 7
    }
    console.log("Значение a: ", a)
    console.log("Ответ: ", step3)
}
// БЫЛО ошибка была в неправильной логике if else (step2 > 4)
// и то что выводила обязательно step3, хотя вычисление могло закончится на step2
// else {
//     if (a < 3) {
//         step2 = 1
//     }
//     else step2 = 2 * (a - 2)
// }
// if (step2 > 4) {
//     step3 = 5
// }
// else {
//     if (a % 2 == 0) {
//         step3 = 6
//     }
//     else step3 = 7
// }
// console.log("Значение a: ", a)
// console.log("Ответ: ", step3)

// исходник (a > 10 ? a : a * 2) > 5 ? (2 * a) + 1 : (a < 3 ? 1 : 2 * (a - 2)) > 4 ? 5 : (a % 2 == 0 ? 6 : 7);
// логика
// (a > 10 ? a : a * 2) если > 5 тогда (2 * a) + 1 иначе (a < 3 ? 1 : 2 * (a - 2)) > 4 ? 5 : (a % 2 == 0 ? 6 : 7)
// (a < 3 ? 1 : 2 * (a - 2)) > 4 тогда 5 иначе (a % 2 == 0 ? 6 : 7)