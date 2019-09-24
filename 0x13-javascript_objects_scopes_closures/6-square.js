#!/usr/bin/node

const oldSquare = require('./5-square.js');

class Square extends oldSquare {
  charPrint (c) {
    if (typeof c === 'undefined') {
      c = 'X';
    }
    for (let w = 0; w < this.width; w++) {
      console.log(c.repeat(this.height));
    }
  }
}
module.exports = Square;
