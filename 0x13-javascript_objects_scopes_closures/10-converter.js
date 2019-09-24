#!/usr/bin/node

exports.converter = function (base) {
  function numberConverter (n) {
    return n.toString(base);
  }
  return numberConverter;
};
