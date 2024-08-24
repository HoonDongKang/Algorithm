function getDivisor(n) {
  let index = 1;
  let arr = [];

  while (index <= n) {
    if (n % index === 0) arr.push(index);
    index++;
  }

  return arr.length;
}

function solution(n) {
  return Array.from({ length: n }, (_, i) => i + 1).filter(
    (number) => getDivisor(number) >= 3
  ).length;
}
