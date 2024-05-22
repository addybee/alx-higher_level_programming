#!/usr/bin/node

const ID = process.argv[2];
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${ID}`;

request.get(url, (_, response) => {
  const filmData = JSON.parse(response.body);
  filmData.characters.forEach(peopleUrl => {
    request.get(peopleUrl, (__, resp) => {
      console.log(JSON.parse(resp.body).name);
    });
  });
});
