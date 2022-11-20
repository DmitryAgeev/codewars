/*
Very simple, given an integer or a floating-point number, find its opposite.

Examples:

1: -1
14: -14
-34: 34
 */

function opposite(number) {
    return number ? -number : 0;
    // return -number;
}

console.log(opposite(1)) // -1
console.log(opposite(0)) // 0
console.log(opposite(4.25)) // -4.25