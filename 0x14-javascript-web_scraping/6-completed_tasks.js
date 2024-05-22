#!/usr/bin/node

const webUrl = process.argv[2];
const request = require('request');

request.get(webUrl, (__, response) => {
  const todosDone = {};
  JSON.parse(response.body).forEach(todo => {
    if (todo.completed) {
      todosDone[todo.userId] = (todosDone[todo.userId] || 0) + 1;
    }
  });
  console.log(todosDone);
});
