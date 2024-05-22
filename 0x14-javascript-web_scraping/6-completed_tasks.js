#!/usr/bin/node

const webUrl = process.argv[2];
const request = require('request');
const userUrl = 'https://jsonplaceholder.typicode.com/users';
request.get(`${webUrl}/?completed=true`, (error, response) => {
  if (error) throw error;
  const todos = JSON.parse(response.body);
  const result = {};
  request.get(userUrl, (err, resp) => {
    if (err) throw err;
    const users = JSON.parse(resp.body);

    for (const user of users) {
      let count = 0;
      for (const todo of todos) {
        if (user.id === todo.userId) count++;
      }
      if (count > 0) result[user.id] = count;
    }

    console.log(result);
  });
});
