#!/usr/bin/node

const http = require('request');

http.get(process.argv[2], function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code:', response.statusCode);
  }
});
