#!/usr/bin/node
exports.callMeMoby = function (n, func) {
  let i = 0;
  for (i = 0; i < n; i++) {
    func();
    }
};
