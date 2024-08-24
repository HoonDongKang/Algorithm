function solution(numbers) {
  numbers = numbers.sort((a, b) => b - a);
    
  const num1 = numbers[0] * numbers[1];
  const num2 = numbers[numbers.length - 1] * numbers[numbers.length - 2];

  return num1 > num2 ? num1 : num2;
}