#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + id,
  method: 'GET',
  headers: {
    Accept: 'application/json',
    'Accept-Charset': 'utf-8',
    'User-Agent': 'gunter'
  }
};
request(options, function (err, res, body) {
  const json = JSON.parse(body);
  console.log(json.title);
});
