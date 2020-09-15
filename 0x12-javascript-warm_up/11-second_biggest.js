#!/usr/bin/node
const arg = process.argv;
arg.splice(0, 2);
function second () {
  if (arg.length < 2) {
    return (0);
  } else {
    const ret = arg.sort((a, b) => a - b);
    console.log(ret);
    return (parseInt(ret.splice(-2, 1)));
  }
}
console.log(second(arg));
