#!/usr/bin/node
function add (a, b) {
  const num1 = process.argv[2];
  const num2 = process.argv[3];
  console.log(Number(num1) + Number(num2));
}
add(process.argv[2], process.argv[3]);
