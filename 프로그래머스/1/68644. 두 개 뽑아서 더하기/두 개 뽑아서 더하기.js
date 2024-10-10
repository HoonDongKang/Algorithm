function solution(numbers) {
  let arr = [];
  numbers.forEach((num, idx) => {
    for (let i = idx + 1; i < numbers.length; i++) {
      arr.push(num + numbers[i]);
    }
  });
  return Array.from(new Set(arr)).sort((a, b) => a - b);
}
