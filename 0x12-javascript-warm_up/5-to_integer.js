#!/usr/bin/node
const num1 = process.argv[2];
if (!isNaN(Number(num1))) {
  console.log('My number: ' + Math.trunc(num1));
} else {
  console.log('Not a number');
}
