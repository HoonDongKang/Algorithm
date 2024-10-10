function solution(numbers) {
  let result = '';

  for (let i = 1; i < numbers.length; i++) {
    result += String(i).repeat(numbers[i] / 2);
  }

  result += '0';

  for (let i = numbers.length - 1; i > 0; i--) {
    result += String(i).repeat(numbers[i] / 2);
  }

  return result;
}
