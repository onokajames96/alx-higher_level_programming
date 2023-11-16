#!/usr/bin/node
const arg = process.argv;
if (isNaN(Number(arg[2]))) {
  console.log('Missing number of occurrences');
} else {
  for (let y = 0; y < arg[2]; y++) {
    console.log('C is fun');
  }
}
