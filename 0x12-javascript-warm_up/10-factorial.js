#!/usr/bin/node
const arg = parseInt(process.argv[2]);
function Factorial (num) {
  if (isNaN(num) || num === 1) {
    return (1);
  } else {
    return (num * Factorial(num - 1));
  }
}
console.log(Factorial(arg));
