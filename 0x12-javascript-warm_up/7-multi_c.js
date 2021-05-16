#!/usr/bin/node
const x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
  console.log('Missing Number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
