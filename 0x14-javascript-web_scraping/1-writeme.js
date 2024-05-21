#!/usr/bin/node

const file = process.argv[2];
const message = process.argv[3];
const fs = require('fs');

fs.writeFile(file, message, 'utf8', (err) => {
  if (err) console.log(err);
});
