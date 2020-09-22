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
request(options, function (err, response, body) {
  if (err) console.log(err);
  const films = JSON.parse(body).results;
  let count = 0;
  for (const index in films) {
    const filmChars = films[index].characters;
    for (const char in filmChars) {
      if (filmChars[char].includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
