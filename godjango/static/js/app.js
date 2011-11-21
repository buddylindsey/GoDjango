(function() {
  var list, number, other, square;
  list = [1, 2, 3];
  number = 5;
  square = function(x) {
    return x * x;
  };
  if (list[0] === 1) {
    document.write('hello');
  }
  other = 'hello';
  if (other === 'hello') {
    document.write(other);
  } else {
    document.write('world');
  }
}).call(this);
