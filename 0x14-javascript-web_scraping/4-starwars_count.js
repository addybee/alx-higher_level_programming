#!/usr/bin/node

const api = process.argv[2];
const request = require('request');
const wedgeAntilles = 'https://swapi-api.alx-tools.com/api/people/18/';

request.get(api, (error, response) => {
  if (error) throw error;
  const results = JSON.parse(response.body).results;
  let count = 0;
  for (let index = 0; index < results.length; index++) {
    for (let idx = 0; idx < results[index].characters.length; idx++) {
      if (results[index].characters[idx] === wedgeAntilles) count++;
    }
  }
  console.log(count);
});
