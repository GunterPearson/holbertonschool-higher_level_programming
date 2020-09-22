#!/usr/bin/node
const request = require('request');
const options = {
  url: process.argv[2],
  method: 'GET',
  headers: {
    Accept: 'application/json',
    'Accept-Charset': 'utf-8',
    'User-Agent': 'gunter'
  }
};
let i = 0;
request(options, function (err, res, body) {
  if (err) console.log(err);
  const json = JSON.parse(body);
  for (const index in json.results) {
    for (const list in json.results[index].characters) {
      if (list == 18) {
        i += 1;
      }
    }
  }
  console.log(i - 1);
});
