#!/usr/bin/node
const arg = process.argv;
const numOne = parseInt(arg[2]);
const numTwo = parseInt(arg[3]);
function add (a, b) {
  console.log(a + b);
}
add(numOne, numTwo);
