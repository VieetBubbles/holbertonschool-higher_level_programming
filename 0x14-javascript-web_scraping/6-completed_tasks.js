#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const newDict = {};
    const list = JSON.parse(body);

    for (let i = 1; i < list.length; i++) {
      const key = list[i].userId;
      if (list[i].completed === true) {
        // if new dictionary at id is empty then fill in 1st value as 1.
        if (!newDict[key]) {
          newDict[key] = 1;

        // increase value whenever same id and complete is true shows up
        } else {
          newDict[key] += 1;
        }
      }
    }
    console.log(newDict);
  }
});
