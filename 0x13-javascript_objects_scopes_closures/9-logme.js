#!/usr/bin/node
// keep track of the number of arguments printed
let count = 0;

exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count++;
};
