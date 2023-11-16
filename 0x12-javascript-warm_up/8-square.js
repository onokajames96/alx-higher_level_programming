#!/usr/bin/node
const arg = process.argv[2];

if (isNaN(arg)) {
  console.log('Missing size');
} else {
  let k = 0;
  while (k < arg) {
    let str = '';
    let i = 0;
    while (i < arg) {
      str += 'X';
      i++;
    }

    console.log(str);
    k++;
  }
}
