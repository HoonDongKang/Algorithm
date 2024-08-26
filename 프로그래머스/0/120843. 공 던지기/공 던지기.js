function solution(numbers, k) {
  if (numbers.length >= k * 2) return numbers[k];
  numbers = Array(k * 2)
    .fill(numbers)
    .flat();

  console.log(numbers);
  return numbers[k * 2 - 2];
}