function solution(numbers, direction) {
  if (direction === 'right') {
    return [numbers.pop(), ...numbers];
  }
  if (direction === 'left') {
    const number = numbers.shift();
    return [...numbers, number];
  }
}