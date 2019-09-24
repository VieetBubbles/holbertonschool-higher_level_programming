#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  const len = list.length;

  for (let i = 0; i < len; i++) {
    if (list[i] === searchElement) {
      count += 1;
    }
  }
  return count;
};
