#!/usr/bin/node
function factorial (n) {
  if (isNaN(Number(n))) {
    return 1;
  }
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}
console.log(factorial(process.argv[2]));
