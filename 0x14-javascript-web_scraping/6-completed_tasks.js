#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) console.log(err);
  const todos = JSON.parse(body);
  const done = {};
  todos.forEach((todo) => {
    if (todo.completed && done[todo.userId] === undefined) {
      done[todo.userId] = 1;
    } else if (todo.completed) {
      done[todo.userId] += 1;
    }
  });
  console.log(done);
});
