function factorial(n) {
  return n !== 0 ? n * factorial(n - 1) : 1;
}

function solution(n) {
  let index = 1;

  while (n >= factorial(index)) index++;

  return index - 1;
}