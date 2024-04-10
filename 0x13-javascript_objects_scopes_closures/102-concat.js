#!/usr/bin/node

const fs = require('fs');

let str = ''
fs.open('fileA', 'r', (err, file) => {
  if (err) throw err;
	str = file + "\n";
  console.log('File opened successfully!');
});


fs.open('fileB', 'r', (err, file) => {
  if (err) throw err;
	str += file
  console.log('File opened successfully!');
});

fs.writeFile('fileC', str, (err) => {
  if (err) throw err;
  console.log('Data written to file!');
});
