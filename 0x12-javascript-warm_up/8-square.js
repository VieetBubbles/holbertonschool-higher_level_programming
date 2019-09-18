#!/usr/bin/node
const times = process.argv[2];
let i = 0;
let j = 0;
if (!isNaN(Number(process.argv[2]))) {
  for (i = 0; i < Number(times); i++) {
    const myArray = [];
    for (j = 0; j < Number(times); j++) {
      myArray.push('X');
    }
    console.log(myArray.join(''));
  }
} else {
  console.log('Missing size');
}
