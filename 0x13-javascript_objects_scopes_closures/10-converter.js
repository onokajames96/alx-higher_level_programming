#!/usr/bin/node
// number convertion
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
