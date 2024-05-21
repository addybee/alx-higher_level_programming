#!/usr/bin/node

const api = process.argv[2];
const request = require('request');

request
  .get(api)
  .on('response', (response) => { console.log('code: ', response.statusCode); });
