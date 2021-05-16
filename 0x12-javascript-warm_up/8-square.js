#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let line = '';
    for (let t = 0; t < size; t++) line += 'X';
    console.log(line);
  }
}
