#!/usr/bin/node

const array1 = require('./100-data.js').list;
const map1 = array1.map(function (x, index) {
  return x * index;
});

console.log(array1);
console.log(map1);
