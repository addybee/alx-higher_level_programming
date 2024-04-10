#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};
Object.values(dict).forEach((key) => {
  if (!Object.prototype.hasOwnProperty.call(newDict, key)) { newDict[key] = []; }
});

for (const key in dict) {
  newDict[dict[key]].push(key);
}
console.log(newDict);
