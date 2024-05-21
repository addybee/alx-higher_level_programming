#!/usr/bin/node

const api = process.argv[2];
const request = require('request');

request.get(api, (error, response, body) => {
  if (error) throw error;
  console.log('code: ', response.statusCode);
});
