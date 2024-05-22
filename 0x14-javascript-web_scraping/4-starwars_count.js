#!/usr/bin/node

const api = process.argv[2];
const request = require('request');
const ID = '18';

request.get(api, (error, response) => {
  if (error) throw error;
  const results = JSON.parse(response.body).results;
  console.log(results.reduce((acc, result) => acc + result.characters.filter(character => character.includes(ID)).length, 0));
});
