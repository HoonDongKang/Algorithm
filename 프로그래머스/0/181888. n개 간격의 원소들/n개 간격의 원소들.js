function solution(numbers, n) {
  let position = 0;
  return numbers.reduce((acc) => {
    if (position < numbers.length) {
      acc.push(numbers[position]);
    }
    position += n;
    return acc;
  }, []);
}
