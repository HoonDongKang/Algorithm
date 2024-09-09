function solution(a, d, included) {
  return included
    .map((inc, i) => (inc ? a + i * d : null))
    .filter((val) => val !== null)
    .reduce((acc, cur) => (acc += cur), 0);
}
