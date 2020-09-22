#!/usr/bin/node
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, response, body) {
  if (err) console.log(err);
  const characters = JSON.parse(body).characters;
  characters.forEach((charac) => {
    request(charac, function (err, response, body) {
      if (err) console.log(err);
      const name = JSON.parse(body).name;
      console.log(name);
    });
  });
});
