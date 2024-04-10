#!/usr/bin/node

const square5 = require('./5-square.js');

class Square extends square5 {
  charPrint (c) {
    if (!c) super.print();
    else {
      for (let h = 0; h < this.height; h++) {
        let element = '';
        for (let w = 0; w < this.width; w++) element += c;
        console.log(element);
      }
    }
  }
}
module.exports = Square;
