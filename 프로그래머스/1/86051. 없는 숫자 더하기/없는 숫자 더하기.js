function solution(numbers) {
  const arr = Array.from({ length: 10 }, (_, i) => i);
  return arr
    .filter((el) => !numbers.includes(el))
    .reduce((acc, cur) => (acc += cur), 0);
}