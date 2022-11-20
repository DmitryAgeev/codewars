/*
We need a function that can transform a number (integer) into a string.

What ways of achieving this do you know?

Examples (input --> output):
123  --> "123"
999  --> "999"
-100 --> "-100"
 */

function numberToString(num) {
    // return `${num}`;
    return num.toString();
}

console.log(numberToString(123)) // 123
console.log(numberToString(0)) // 0
console.log(numberToString(-100)) // -100