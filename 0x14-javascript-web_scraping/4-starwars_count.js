#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let count = 0;
    // const episodes = res.body.results;
    // const episodes = JSON.parse(body)['results'];
    const episodes = JSON.parse(body).results;
    for (let i = 0; i < episodes.length; i++) {
      // for (let c = 0; c < episodes[i]['characters'].length; c++) {
      for (let c = 0; c < episodes[i].characters.length; c++) {
        // if (episodes[i]['characters'][c].includes('/18/')) {
        if (episodes[i].characters[c].includes('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
