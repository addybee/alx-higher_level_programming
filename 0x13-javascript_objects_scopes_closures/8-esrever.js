#!/usr/bin/node

exports.esrever = function (list) {
  const len = list.length;

  for (let index = 0; index < (len / 2); index++) {
    const temp = list[index];
    list[index] = list[len - index - 1];
    list[len - index - 1] = temp;
  }
  return (list);
};
