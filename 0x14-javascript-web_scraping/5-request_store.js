#!/usr/bin/node

const webUrl = process.argv[2];
const file = process.argv[3];
const fs = require('fs');
const request = require('request');

request(webUrl).pipe(fs.createWriteStream(file, 'utf8'));
