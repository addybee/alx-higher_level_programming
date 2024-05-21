#!/usr/bin/node

const api = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;
const request = require('request');

request.get(api, (error, response) => {
  if (error) throw error;
  console.log(JSON.parse(response.body).title);
});
