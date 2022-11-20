/*
Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
 */

// function even_or_odd(number) {
//     if (number % 2 === 0) {
//         return 'Even'
//     } else {
//         return 'Odd'
//     }
// }

function evenOrOdd(number) {
    return number % 2 ? "Odd" : "Even";
}

console.log(evenOrOdd(2)) // 'Even'
console.log(evenOrOdd(7)) // 'Odd'