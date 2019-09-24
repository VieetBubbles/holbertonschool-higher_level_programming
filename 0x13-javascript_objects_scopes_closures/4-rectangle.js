#!/usr/bin/node

class Rectangle {
  // initialize the class
  constructor (w, h) {
    if ((w = parseInt(w)) > 0 && (h = parseInt(h)) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // The Methods of the class Rectangle
  // Method to print Rectangle
  print () {
    let rArray = [];
    for (let h = 0; h < this.height; h++) {
      rArray = [];
      for (let w = 0; w < this.width; w++) {
        rArray.push('X');
      }
      console.log(rArray.join(''));
    }
  }

  // Method to sqp the width and height values
  rotate () {
    let temp = 0;

    temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // Methid that doubles the width and height values
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
