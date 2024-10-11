function solution(a, b, n) {
  let count = 0;
  let rest = 0;

  while (n >= a) {
    count += Math.floor(n / a) * b;

    rest += n % a;

    n = Math.floor(n / a) * b;

    n += rest;
    rest = 0;
  }

  return count;
}