#!/usr/bin/node
const argNum = process.argv[2];

if (argNum === undefined) {
  console.log('No argument');
} else {
  console.log(argNum);
}
