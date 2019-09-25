#!/usr/bin/node

const request = require('request');

request.get('https://swapi.co/api/films/' + process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    // When receiving data from a web server, the data is always a string.
    // Parse the data with JSON.parse(), and the data becomes a JavaScript object.
    console.log(JSON.parse(body).title);
  }
});
