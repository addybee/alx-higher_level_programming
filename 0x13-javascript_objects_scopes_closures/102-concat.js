#!/usr/bin/node

const fs = require('fs');

const { argv } = require('node:process');
const [, , file1, file2, file3] = argv;
if (file1 && file2 && file3) {
  // Read content from the first source file
  fs.readFile(file1, 'utf8', (err, data1) => {
    if (err) {
      console.error(`Error reading ${file1}: ${err.message}`);
      return;
    }

    // Read content from the second source file
    fs.readFile(file2, 'utf8', (err, data2) => {
      if (err) {
        console.error(`Error reading ${file2}: ${err.message}`);
        return;
      }

      // Concatenate the contents of both files
      const result = data1 + data2;

      // Write the concatenated content to the destination file
      fs.writeFile(file3, result, (err) => {
        if (err) {
          console.error(`Error writing to ${file3}: ${err.message}`);
          return;
        }
      });
    });
  });
}