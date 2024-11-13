function solution(elements) {
  const uniqueSums = new Set();
  const n = elements.length;

  for (let length = 1; length <= n; length++) {
      for (let start = 0; start < n; start++) {
          let sum = 0;
          for (let i = 0; i < length; i++) {
              sum += elements[(start + i) % n];
          }
          uniqueSums.add(sum);
      }
  }

  return uniqueSums.size;
}