/*
Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'
 */

function solution(str){
    // slow solution
    // return str.split("").reverse().join("");

    let result = "";

    for(let i = 0; i < str.length; i++) {
        result += str[str.length-1-i];
    }

    return result;
}

console.log(solution('world')) // -1
console.log(solution('')) // 0
console.log(solution('h')) // -4.25