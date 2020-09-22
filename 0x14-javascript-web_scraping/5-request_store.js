#!/usr/bin/node
const fs = require('fs');
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
const fileStream = fs.createWriteStream(process.argv[3]);
request(options).pipe(fileStream);
