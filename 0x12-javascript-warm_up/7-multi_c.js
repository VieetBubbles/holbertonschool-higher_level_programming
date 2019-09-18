#!/usr/bin/node
const times = process.argv[2];
let i = 0;
if (!process.argv[2]) {
  console.log('Missing number of occurrences');
} for (i = 0; i < Number(times); i++) {
  console.log('C is fun');
}
